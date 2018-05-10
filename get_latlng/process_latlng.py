import os
import re

path = os.path.abspath(os.path.join(os.path.dirname("__file__"), os.path.pardir))


#infile=path+'\\data\\final.csv'
infile=path+'\\data\\oneday.csv'
f=open(infile,'r')
text=f.read()
full_text = text.decode('GBK').encode('utf-8').split('\n')


#out_file=path+'\\data\\for_visual_GBK.csv'
out_file=path+'\\data\\oneday_visual.csv'

f=open(out_file,'w')
f.truncate()
f.close()
f=open(out_file,'a')
i=0
f.write(full_text[0].decode('utf-8').encode('GBK')+',latlng,\n')  #
for line in full_text[1:]:  # to ignore the first row
    if line == '':
        break
    latlng=re.findall('\d+\.\d+,\d+\.\d+',line)[0]
    line=line+',"'+latlng+'",'+'\n'
    f.write(line.decode('utf-8').encode('GBK'))
f.close()


'''
parts=line.split(',')
lng=parts[2]
lat=parts[3]
if lng!=' ':
    string=str(i)+',"'+lng+','+lat+'"'+'\n'
    print string,
    f.write(string)
    i += 1
'''