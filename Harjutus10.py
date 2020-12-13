#Mattias Rannamäe IT-20
#09.12.2020
#Harjutus10


#regulaaravaldised


import re

fh = open('ip.txt')
for line in fh:
    if re.search('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$', line):
         print(line,end='')

