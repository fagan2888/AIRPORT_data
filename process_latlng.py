file_name='latlng2.csv'
f=open(file_name,'r')
text=f.read()
full_text = text.decode('GBK').split('\n')


out_file='second_part_latlng.csv'
f=open(out_file,'w')
f.truncate()
f.close()
f=open(out_file,'a')
i=0
f.write('No,latlng\n')
for line in full_text:
    if line == '':
        break
    parts=line.replace(',,',', ,').replace(',,',', ,').split(',')
    lng=parts[2]
    lat=parts[3]
    if lng!=' ':
        string=str(i)+',"'+lng+','+lat+'"'+'\n'
        print string,
        f.write(string)
        i += 1
