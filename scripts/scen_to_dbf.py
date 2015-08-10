#!/usr/bin/env python
import sys
from ScenarioDbRecord_pb2 import ScenarioDbRecord


def main():
	import sys
	record = ScenarioDbRecord()
	with open(sys.argv[1], "rb") as f:
		record.ParseFromString(f.read())

	print(record)
	print(record.strings)


if __name__ == "__main__":
	main()
