# Program to modify the time in a subtitle file (.srt)

import sys
import re

def offset(s, seconds, milliseconds, count):
    HOURS = 0
    MINUTES = 1
    SECONDS = 2
    MILLIS = 3
    s = s.replace(',', ':')
    x = s.split(':')
    values = [0, 0, 0, 0]
    for index in range(len(values)):
        values[index] = int(x[index])
 #   if count >= 50:
 #       if count <= 55:
 #           print(values)
    values[MILLIS] += milliseconds
    values[SECONDS] += seconds
 #   if count >= 50:
 #       if count <= 55:
 #           print(values)
    # max value that each unit may contain
    MAX_VALUES = [24, 60, 60, 1000]
    for index in range(len(values)-1, 0, -1):
        while values[index] >= MAX_VALUES[index]:
            values[index] -= MAX_VALUES[index]
            values[index-1] += 1
        while values[index] < 0:
            values[index] += MAX_VALUES[index]
            values[index-1] -= 1
    if (values[HOURS] < 0): # something is wrong
        for index in range(0, len(values)):
            values[index] = 0
#    if count >= 50:
#        if count <= 55:
#            print(values)
    result = '{:02d}:{:02d}:{:02d},{:03d}'
    return result.format(values[HOURS] , values[MINUTES] , values[SECONDS] , values[MILLIS] )

n = len(sys.argv)
#print(n)
if n != 4:
    print("srcFile dstFile offset")
    print("offset should be sec,milleseconds. Can be negative")
    quit()

# when I type python .\strOffset.py src.srt dst.srt offset
# if i use 1,001 as the offset, the leading zeros are removed 
# and it becomes 1,1
patterns = ['\d+,\d\d\d', '\d+,\d\d', '\d+,\d', '-\d+,\d\d\d', '-\d+,\d\d', '-\d+,\d']
#direction = [1, 1, 1, -1, -1, 1]
found = False
for index in range(len(patterns)):
    if re.match(patterns[index], sys.argv[3]):
        m = re.search(patterns[index], sys.argv[3])
        x = m.group(0).split(',')
        seconds = int(x[0])
        milliseconds = int(x[1])
        if seconds < 0:
            milliseconds = -milliseconds
        found = True
        break
if not found:
    print("Can't calculate the offset")
    quit()

print(seconds)
print(milliseconds)
sourceFile = open(sys.argv[1], "r")
lines = sourceFile.readlines()
destinationFile = open(sys.argv[2], "w")
newLines = []

count = 0
for line in lines:
    if re.match('\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d', line):
        x = line.split(' --> ')
        s = offset(x[0], seconds, milliseconds, count) + ' --> ' + offset(x[1], seconds, milliseconds, count) + '\n'
        newLines.append(s)
        count = count + 1
    else:
        newLines.append(line)

destinationFile.writelines(newLines)
print("number of lines modified: " + str(count))





