import sys
import os
import re

infile = sys.argv[1]
sections = sys.argv[2:]
listFileName = 'list.txt'
listFile = open(listFileName, 'w')
start = '0'
files = []

def splice(start, end):
    cut = start.replace(':','.') + '_' + end.replace(':','.') + '_' + infile
    os.system('ffmpeg -ss ' + start + ' -i "' + infile + '" -to ' + end + ' -c copy "' + cut + '"')
    listFile.write('file ' + cut + '\n')
    files.append(cut)

for section in sections:
    times = re.findall('[0-9]+:+[0-9]+', section)
    end = times[0]
    splice(start, end)
    start = times[1]

splice(end,'99999')
listFile.close()
os.system('ffmpeg -f concat -i ' + listFileName + ' -c copy cut_' + infile)

os.remove(listFileName)
for f in files:
    os.remove(f)