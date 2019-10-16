import sys
import os
import re
import datetime

def main():
  filepath = sys.argv[1]

  if not os.path.isfile(filepath):
    print("could't find file {}, exiting...".format(filepath))
    sys.exit()

  out = open('output' + filepath, 'w')
  with open(filepath) as fp:
    count = 1
    start = datetime.datetime.now().replace(microsecond=0)
    for line in fp:
      count += 1
      node = line
      # p = re.search(r'[^ -~]+', line, re.A)
      p = re.search(r'\x07', line, re.A)
      # p = re.search('DaylightSaveInfo', line, re.I)
      if p:
        print("line {} found, skipping".format(line.strip()))
        node = ""
      out.write(node)
    finish = datetime.datetime.now().replace(microsecond=0)
  print('{} lines read in {}, closing file'.format(count, finish-start))
  out.close()

if __name__ == '__main__':
  main()