from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from mastodon import Mastodon
import argparse

parser = argparse.ArgumentParser(description="Post to a Pixelfed instance with YAML files",
        prog="pixietooth")
parser.add_argument("-f","--token-file",
        help="A file containing a Pixelfed access token",
        required=True)
parser.add_argument("-i","--instance",
        help="A Pixelfed instance (https://pixelfed.social by default)",
        default="https://pixelfed.social")
parser.add_argument("file",nargs="+",help="YAML file describing the post (UTF-8)")
args = parser.parse_args()

token_file = args.token_file
instance = args.instance
names = args.file

with open(token_file,"r") as file:
    personal_access_token = file.read().rstrip()

mastodon = Mastodon(
    access_token = personal_access_token,
    api_base_url = instance
)

for name in names:
    stream = open(name,"r",encoding="UTF-8")
    post = load(stream,Loader=Loader)
    ids = []
    for item in post["items"]:
        media = mastodon.media_post(media_file=item)
        ids.append(media["id"])
    mastodon.status_post(post["text"],media_ids=ids)
