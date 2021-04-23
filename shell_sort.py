import copy
from data import *

def shell_sort(a):
	frames = [a[:]]
	na = copy.deepcopy(a)

	di = b // 2
	while di >= 1:
		for i in range(di):
			for j in range(i + di, b, di):
				k = j
				na[k].color = 'red'
				while k > i and na[k - di].value > na[k].value:
					frames.append(copy.deepcopy(na))
					na[k - di], na[k] = na[k], na[k - di]
					k -= di
				frames.append(copy.deepcopy(na))
				na[k].color = na[k].c
		di //= 2

	frames.append(na)
	return frames
