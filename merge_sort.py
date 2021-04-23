import copy
from data import *

def merge_sort(a):
	frames = [a[:]]
	na = copy.deepcopy(a)
	ms(na, 0, b - 1, frames)
	frames.append(na)
	return frames

def ms(a, l, r, frames):
	if l < r:
		m = (l + r) // 2
		ms(a, l, m, frames)
		ms(a, m + 1, r, frames)

		b = []
		i = l
		j = m + 1
		a[i].color = 'red'
		a[j].color = 'black'

		for n in range(l, r + 1):
			frames.append(copy.deepcopy(a))
			if j > r or i <= m and a[i].value <= a[j].value:
				b.append(a[i])
				a[i].color = a[i].c
				i += 1
				if (i <= m):
					a[i].color = 'red'
			else:
				b.append(a[j])
				a[j].color = a[j].c
				j += 1
				if (j <= r):
					a[j].color = 'black'

		a[m].color = a[m].c
		a[r].color = a[r].c
	
		for k in range(l, r + 1):
			a[k] = b[k - l]