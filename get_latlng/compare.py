#coding:utf-8
import re
infile='T+A.csv'
#infile='address.txt'
outfile='compare.csv'
f=open(infile,'r')
lines=f.read().split('\r')
def output(string):
    f=open(outfile,'a')
    f.write(string.decode('utf-8').encode('GBK'))
    f.close()


f=open(outfile,'w')
f.close()
for line in lines[1:]:
    #print line
    print line
    try:
        alng=re.findall('\d+\.\d+',line.split(',')[9])[0]
        tlng=re.findall('\d+\.\d+',line.split(',')[13])[0]
        print alng,tlng
        a = float(alng[:7])
        t = float(tlng[:7])
        if abs(a-t)<=0.02:
            print '>'
            output(line+',1\n')
        else:
            output(line+',0\n')
    except:
        output(line+',0\n')
        pass
f.close()
