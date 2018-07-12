# this file used to cut the district into 10*10 squares

f=open('final.csv','r')

all_line=f.readlines()
lnglat=[]
lng_max=104.1606
lng_min=103.9905
lnstep=(lng_max-lng_min)/10

lat_max=30.72388
lat_min=30.5265
lastep=(lat_max-lat_min)/10

array=[[0]*10 for i in range(10)]
print array
flag=0
for line in all_line[1:]:
    lng=float(line.split(',')[7])
    lat=float(line.split(',')[8])
    #print lng,lat,
    for i in range(10):
        for j in range(10):
            if lng<lng_min+(i+1)*lnstep and lat<lat_min+(j+1)*lastep:
                array[9-j][i]+=1
                print i*10+j
                flag=1
                break
        if flag==1:
            flag=0
            break
for i in range(10):
    print str(array[i])[1:-1]

