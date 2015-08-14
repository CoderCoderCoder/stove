package pegasus

import (
	"github.com/jinzhu/gorm"
	_ "github.com/mattn/go-sqlite3"
	"time"
)

var db = openDB()

func openDB() gorm.DB {
	db, err := gorm.Open("sqlite3", "db/pegasus.db")
	if err != nil {
		panic(err)
	}

	db.SingularTable(true)
	return db
}

type Achieve struct {
	ID               int32
	AccountID        int64
	AchieveID        int32

	Progress         int32
	AckProgress      int32
	CompletionCount  int32
	Active           bool
	// started_count doesn't seem to be used
	DateGiven        time.Time
	DateCompleted    time.Time
	// do_not_ack is also not used
}

type Booster struct {
	ID          int64
	AccountID   int64
	BoosterType int
	Opened      bool
	Cards       []BoosterCard
}

type BoosterCard struct {
	ID        int64
	BoosterID int64
	CardID    int32
	Premium   int32
}

type FavoriteHero struct {
	ID           int64
	AccountID    int64
	ClassID      int32
	CardID       int32
	Premium      int32
}

type Deck struct {
	ID           int64
	AccountID    int64
	DeckType     int
	Name         string
	HeroID       int32
	HeroPremium  int32
	CardBackID   int32
	LastModified time.Time
	Cards        []DeckCard
}

type DeckCard struct {
	ID      int64
	DeckID  int64
	CardID  int32
	Premium int32
	Num     int32
}

type DbfAchieve struct {
	ID          int32
	AchType     string
	Triggered   string
	AchQuota    int
	Race        int
	Reward      string
	RewardData1 int
	RewardData2 int
	CardSet     int
	Event       string
	NameEnus    string
}

type DbfCard struct {
	ID            int32
	NoteMiniGuid  string
	IsCollectible bool
	NameEnus      string
	ClassID       int32
}

type DbfCardBack struct {
	ID       int32
	Data1    int
	source   string
	NameEnus string
}

type SeasonProgress struct {
	ID        int
	AccountID int64

	StarLevel            int
	Stars                int
	LevelStart, LevelEnd int
	LegendRank           int
	SeasonWins           int
	Streak               int
}

type AccountLicense struct {
	ID        int64
	AccountID int64
	LicenseID int64
}

type License struct {
	ID        int64
	ProductID int
}

type DbfLocalizedStringValue struct {
	ID     int
	Locale int32
	Value  string
}

type DbfLocalizedString struct {
	ID     int
	Key	   string
	Values []DbfLocalizedStringValue
}

type DbfBrawlScenario struct {
	ID                            int32
	NoteDesc                      string
	NumPlayers                    int32
	Player1HeroCardID             int64
	Player2HeroCardID             int64
	IsExpert                      bool
	AdventureId                   int32
	AdventureModeId               int32
	WingId                        int32
	SortOrder                     int32
	ClientPlayer2HeroCardId       int64
	TavernBrawlTexture            string
	TavernBrawlTexturePhone       string
	TavernBrawlTexturePhoneOffset []float32
	Strings                       DbfLocalizedString
	RulesID                       int32
	RuleType                      int
	RuleData1                     int64
	RuleData2                     int64
	RuleData3                     int64
}
