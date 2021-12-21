from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from mastodon import Mastodon
import argparse

parser = argparse.ArgumentParser(description="Post to a Pixelfed instance")
parser.add_argument("file",nargs="+",help="YAML file describing the post")
args = parser.parse_args()

names = args.file

# TODO as parameter
with open("/home/desenvolvedor/other/git/pixietooth/.personal_access_token","r") as file:
    personal_access_token = file.read().rstrip()

mastodon = Mastodon(
    access_token = personal_access_token,
    api_base_url = "https://pixelfed.social/" # TODO as parameter
)

for name in names:
    stream = open(name,"r",encoding="utf-8")
    post = load(stream,Loader=Loader)
    ids = []
    for item in post["items"]:
        media = mastodon.media_post(media_file=item)
        ids.append(media["id"])
    mastodon.status_post(post["text"],media_ids=ids)
