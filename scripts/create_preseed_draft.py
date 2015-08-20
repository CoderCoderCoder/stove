#!/usr/bin/env python
"""
Preseed a draft
"""
import sqlite3
import sys
from datetime import datetime

SLOT_CHOICES = [
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
	("Boulderfist Ogre", "Arcane Shot", "Arcane Explosion"),
]

def main():
	if len(sys.argv) < 2:
		sys.stderr.write("USAGE: %s [dbfile]\n" % (sys.argv[0]))
		exit(1)
	dbfile = sys.argv[1]

	connection = sqlite3.connect(dbfile)
	cursor = connection.cursor()

	values = []
	for slot, choices in enumerate(SLOT_CHOICES):
		for card_name in choices:
			cursor.execute("SELECT id FROM dbf_card WHERE name_enus = ?", (card_name,))
			card_id, = cursor.fetchone()
			values.append((None, slot, card_id))
	connection.executemany("INSERT INTO preseed_draft_choice VALUES (?, ?, ?)", values)

	connection.commit()
	connection.close()


if __name__ == "__main__":
	main()
