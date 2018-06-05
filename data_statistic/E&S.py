infile='arrive_time_list.csv'
f=open(infile,'r')
lines=f.readlines()
f.close()
time_list=[[0]*19 for i in range(8)]
for line in lines[1:]:
    infos=line.split(',')
    date=int(infos[0].split('/')[-1])
    arrive_hour=int(infos[2].split(':')[0])
    if arrive_hour<5:
        arrive_hour+=24
    print date,arrive_hour
    for i in range(8):
        if date==i+20:
            for j in range(19):
                if arrive_hour==j+9:
                    time_list[i][j]+=1


f=open('everyday.csv','w')

for i in range(len(time_list)):
    print time_list[i]
    f.write(str(time_list[i])[1:-1]+'\n')
f.close()