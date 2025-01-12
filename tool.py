#!/usr/bin/env python3
import sys
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("script", type=str)
args = parser.parse_args()

if not os.path.exists(args.script):
	sys.stderr.write(f"'{args.script}' not a file")

with open(args.script, "rb") as h:
	contents = h.read().decode('utf-8')

code_string = "+".join([f"chr({ord(x)})" for x in contents])
code_string = f"{code_string}"

script_string = "+".join([f"chr({ord(x)})" for x in "<script>"])
script_string = f"{script_string}"
exec_string = "+".join([f"chr({ord(x)})" for x in "exec"])
exec_string = f"{exec_string}"
res = input("Python3 or Python (3/0): ")
if res == "3":
    res = "python3"
else:
    res = "python"
print(f'{res} -c "exec(compile({code_string}, {script_string}, {exec_string}))"')
