package pegasus

import (
	"github.com/HearthSim/hs-proto/go"
	"github.com/golang/protobuf/proto"
	"log"
)

type Store struct{
}

func (s *Store) Init(sess *Session) {
	sess.RegisterUtilHandler(1, 237, OnGetBattlePayConfig)
	sess.RegisterUtilHandler(1, 255, OnGetBattlePayStatus)
}

func OnGetBattlePayConfig(s *Session, body []byte) ([]byte, error) {
	log.Printf("\n\n\n\n>D>D>D>OnGetBattlePayConfig")
	res := hsproto.PegasusUtil_BattlePayConfigResponse{}

	// Hardcode US Dollars until we setup the DB to handle other currencies
	res.Currency = proto.Int32(1)
	res.Unavailable = proto.Bool(false)
	res.SecsBeforeAutoCancel = proto.Int32(10)
	// Todo: Find a way to integrate this into our current DB structure
	res.GoldCostArena = proto.Int64(150)

	bundles := []Bundle{}
	db.Find(&bundles)
	log.Printf("\n\n\n\n######%+v", bundles)
	for _, bundle := range bundles {

		var bundleItems = []*hsproto.PegasusUtil_BundleItem{}
		products := []Product{}
		db.Model(&bundle).Association("Items").Find(&products)
		log.Printf("\n\n\n\n<<<<<%+v", products)
		for _, items := range products{
			productType := hsproto.PegasusUtil_ProductType(items.ProductType)
			bundleItems = append(bundleItems, &hsproto.PegasusUtil_BundleItem{
				ProductType:	&productType,
				Data:			proto.Int32(items.ProductData),
				Quantity:		proto.Int32(items.Quantity),
			})
		}
		log.Printf("\n\n\n\n^^^^^^^%+v", bundleItems)

		res.Bundles = append(res.Bundles, &hsproto.PegasusUtil_Bundle{
			Id:					proto.String(bundle.ProductID),
			// Hardcode $1 until price data is implemented in DB
			Cost:				proto.Float64(1.00),
			AppleId:			proto.String(bundle.AppleID),
			AmazonId:			proto.String(bundle.AmazonID),
			GooglePlayId:		proto.String(bundle.GoogleID),
			// Hardcode 1 (0 causes issues) until price data is implemented in DB
			GoldCost: proto.Int64(1),
			ProductEventName:	proto.String(bundle.EventName),
			Items: 				bundleItems,
		})

		log.Printf("\n\n\n\n$$$$$$%+v", res.Bundles[0].Items)


	}
	log.Printf("\n\n\n\n>>>>%+v", res)
	return EncodeUtilResponse(238, &res)
}

func OnGetBattlePayStatus(s *Session, body []byte) ([]byte, error) {
	res := hsproto.PegasusUtil_BattlePayStatusResponse{}
	status := hsproto.PegasusUtil_BattlePayStatusResponse_PS_READY
	res.Status = &status
	res.BattlePayAvailable = proto.Bool(true)
	return EncodeUtilResponse(265, &res)
}
