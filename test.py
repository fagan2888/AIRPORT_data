import re
infile = 'd:\hedge\Desktop\\address_list.txt'
f = open(infile, 'r')
addr = f.readline()
while addr:
    addr = f.readline()
    m = re.search('#', addr)
    if addr.replace('\n', '') == '' or m != None:
        print addr
    else:
        print addr