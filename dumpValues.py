#!/usr/bin/env python3

import json
import sys

vals = {
}

def dumpItem(v):
	if not isinstance(v, str):
		return
	val = v.split("/");
	if not len(val) == 3:
		return
	if val[1] in vals:
		new = vals[val[1]]
	else:
		new = val[2]

	if val[0] == "$s":
		vals[val[1]] = str(val[2])
	if val[0] == "$i":
		vals[val[1]] = int(val[2])

def handleItem(k, v):
	if isinstance(v, dict):
		iterateConfig(v)
	elif isinstance(v, list):
		for i in v:
			handleItem("", i)
	else:
		dumpItem(v)

def iterateConfig(cfg):
	for k, v in cfg.items():
		handleItem(k, v)

if not len(sys.argv) == 2:
	exit(0)

with open(sys.argv[1]) as json_file:
	schema = json.load(json_file)

iterateConfig(schema)
print(json.dumps(vals, indent = 4))
