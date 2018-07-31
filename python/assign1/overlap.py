def overlap(r1,r2):
	r1l=string_prep(r1)
	r2l=string_prep(r2)
	[x11, y11, x12, y12] = r1l
	[x21, y21, x22, y22] = r2l
	xl = min(x12,x22) - max(x11,x21)
	yl = min(y12,y22) - max(y11,y21)
	sq = xl * yl
	print(sq)

def string_prep(str):
	r = []
	for ch in ['[',']',',']:
		str = str.replace(ch, '')
	for num in str.split():
		result = r.append(float(num))
	return r


r1 = '[3.4, 3.6, 7.1, 8.5]'
r2 = '[5.3, 2.0, 10.7, 7.4]'
overlap(r1, r2)
