#!/usr/bin/env python
"""
Preseed a draft
"""
import sqlite3
import sys
import random
sys.path.append("../fireplace")
sys.path.append("./fireplace")
print (sys.path)
import fireplace
import fireplace.cards

SLOT_CHOICES = [
	"Inner Rage",
	"Execute",
	"Execute",
	"Whirlwind",
	"Whirlwind",
	"Armorsmith",
	"Armorsmith",
	"Battle Rage",
	"Battle Rage",
	"Cruel Taskmaster",
	"Cruel Taskmaster",
	"Fiery War Axe",
	"Fiery War Axe",
	"Slam",
	"Slam",
	"Unstable Ghoul",
	"Unstable Ghoul",
	"Acolyte of Pain",
	"Acolyte of Pain",
	"Frothing Berserker",
	"Frothing Berserker",
	"Shield Block",
	"Warsong Commander",
	"Warsong Commander",
	"Death's Bite",
	"Death's Bite",
	"Gnomish Inventor",
	"Gnomish Inventor",
	"Grim Patron",
	"Grim Patron",
	"Emperor Thaurissan",
]

def get_rarity_and_type(card_name):
	cs = fireplace.cards.filter(name=card_name, collectible=True)
	if len(cs) > 1:
		import pdb; pdb.set_trace()
	c = getattr(fireplace.cards, cs[0])
	return c.rarity, c.type


def main():
	if len(sys.argv) < 2:
		sys.stderr.write("USAGE: %s [dbfile]\n" % (sys.argv[0]))
		exit(1)
	dbfile = sys.argv[1]

	connection = sqlite3.connect(dbfile)
	cursor = connection.cursor()

	values = []
	random.shuffle(SLOT_CHOICES)
	for slot, card_name in enumerate(SLOT_CHOICES):
		cursor.execute("SELECT id, class_id FROM dbf_card WHERE name_enus = ?", (card_name,))
		card_id, class_id = cursor.fetchone()
		rarity, card_type = get_rarity_and_type(card_name)
		p = []
		for p_id, p_name in cursor.execute(("SELECT id, name_enus FROM dbf_card WHERE " +
			"is_collectible = 1 AND hero_power_id = 0 AND crafting_event = \"always\" AND (class_id = 10 OR class_id = 0)")):
			p_r, p_t = get_rarity_and_type(p_name)
			#print(card_name, card_type, p_name, p_t, card_type == p_t)
			if p_r == rarity and p_name != card_name:
				p.append((p_id, p_r))
		random.shuffle(p)
		p = p[:2]
		p.append((card_id, rarity))
		random.shuffle(p)
		for c_i, c_r in p:
			cursor.execute("SELECT name_enus FROM dbf_card WHERE id = ?", (c_i,))
			c_n, = cursor.fetchone()
			#print(c_n, c_r, end='\t\t')
			values.append((None, slot, c_i))
		print ('pick', card_name)
		#print('')
	connection.executemany("INSERT INTO preseed_draft_choice VALUES (?, ?, ?)", values)

	connection.commit()
	connection.close()


if __name__ == "__main__":
	main()
