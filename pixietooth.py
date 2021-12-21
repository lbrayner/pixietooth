from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

import argparse

parser = argparse.ArgumentParser(description="Post to a Pixelfed instance")
parser.add_argument("file",nargs="+",help="YAML file describing the post")
args = parser.parse_args()

names = args.file

# print("%s" % names) # TODO debug
for name in names:
    stream = open(name,"r",encoding="utf-8")
    post = load(stream,Loader=Loader)
    print(post) # TODO debug
