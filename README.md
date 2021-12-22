# Python 3

## Packages

- pyyaml
- Mastodon.py

```
pip3 install pyyaml Mastodon.py
```

# Synopsis

```
./pixietooth [-h] -f TOKEN_FILE [-i INSTANCE] file [file ...]
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
