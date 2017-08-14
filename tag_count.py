import urllib.request
import sys

depth = 0
tag_count = 0
for character in urllib.request.urlopen(sys.argv[1]).read():
  if chr(character) == '<':
    depth += 1
  elif chr(character) == '>' and depth >= 0:
    depth -= 1
    tag_count += 1

print('Tag count is ' + str(tag_count))