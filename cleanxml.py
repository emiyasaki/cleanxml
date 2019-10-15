import sys
import os
import re

def main():
  filepath = sys.argv[1]

  if not os.path.isfile(filepath):
    print("could't find file {}, exiting...".format(filepath))
    sys.exit()

  out = open('output' + filepath, 'w')
  with open(filepath) as fp:
    count = 1
    for line in fp:
      count += 1
      node = line
      p = re.compile('[^ -~]+')
      match = p.match(line)
      # match = re.match('DaylightSaveInfo', line)
      if match:
        print("line {} found, skipping".format(line.strip()))
        node = ""
      out.write(node)
  print('{} lines read, closing file'.format(count))
  out.close()

if __name__ == '__main__':
  main()