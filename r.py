
data = []
count = 0
with open('original.txt','r') as f:
	for line in f:
		data.append(line)
		count = count + 1
        if count % 1000 == 0:
		         print(len(data))
print('the file have done','all of this have', len(data),'datas')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print ('the avarge of comment',sum_len/len(data))

new = []
for d in data :
	if len (d) < 100 :
		 new.append(d)
print('all of this have',len(new),'comments lens smaller than 100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('all of this have',len(good),'comments lens smaller than 100')