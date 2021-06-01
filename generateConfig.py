#!/usr/bin/env python3

import json
import sys

def replaceItem(v):
	if not isinstance(v, str):
		return v
	val = v.split("/");
	if not len(val) == 3:
		return v
	if val[1] in vals:
		new = vals[val[1]]
	else:
		new = val[2]

	if val[0] == "$s":
		return str(new)
	if val[0] == "$i":
		return int(new)

	return val[2]

def handleItem(k, v):
	if isinstance(v, dict):
		return iterateConfig(v)
	elif isinstance(v, list):
		new = []
		for i in v:
			new.append(handleItem("", i))
		return new
	else:
		return replaceItem(v)

def iterateConfig(cfg):
	for k, v in cfg.items():
		cfg[k] = handleItem(k, v)
	return cfg

if not len(sys.argv) == 3:
	exit(0)

with open(sys.argv[1]) as json_file:
	schema = json.load(json_file)

with open(sys.argv[2]) as json_file:
	vals = json.load(json_file)

print(iterateConfig(schema))

