# Python 3

## Packages

- pyyaml
- Mastodon.py

```
pip3 install pyyaml Mastodon.py
```

# Usage

```
usage: pixietooth [-h] -f TOKEN_FILE [-i INSTANCE] [-s] file [file ...]

Post to a Pixelfed instance with YAML files

positional arguments:
  file                  YAML file describing the post (UTF-8)

optional arguments:
  -h, --help            show this help message and exit
  -f TOKEN_FILE, --token-file TOKEN_FILE
                        A file containing a Pixelfed access token
  -i INSTANCE, --instance INSTANCE
                        A Pixelfed instance (https://pixelfed.social by default)
  -s, --sensitive       Sensitive/NSFW content
```

# Description

Supply a file contaning an access token, optionally an instance
(<https://pixelfed.social> by default), and one or more YAML files describing
Pixelfed posts.

An example of such a file:

```yml
text: |
  Barcelona, Spain

  #barcelona #spain #travel #travelspain #travelbarcelona

items:
  - /home/desenvolvedor/Pictures/barcelona/barcelona_001.jpg
  - /home/desenvolvedor/Pictures/barcelona/barcelona_002.jpg
  - /home/desenvolvedor/Pictures/barcelona/barcelona_003.jpg
  - /home/desenvolvedor/Pictures/barcelona/barcelona_004.jpg
```
