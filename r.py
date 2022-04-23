
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
