#!/usr/bin/python
f=open("conv_83135D47D2671519820824540.txt","r")
f2=open("list.txt","w+")
t_data=f.readlines()
data=[]
for i in t_data:
	#print i
	a=i.split("\t")
	#print a
	flag=0
	for k in a:
		if (k.rstrip()=='Bos taurus'):
			flag=1
	if(flag==1):
		data.append(i)
		f2.write("%s"%str(i))
f2.close()
f.close()