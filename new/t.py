f = open('train' + '.tsv', 'r', encoding='utf-8')
r = f.readlines()
for it in f:
	if len(it.split('\t')) < 3:
		print(it)
# end_time = time.time()