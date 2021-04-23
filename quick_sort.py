import copy
from data import *

def quick_sort(a):
	frames = [a[:]]
	na = copy.deepcopy(a)
	qs(na, 0, b - 1, frames)
	frames.append(na)
	return frames

def qs(a, l, r, frames):
	if l < r:
		i = l
		j = r
		m = a[(l + r) // 2].value
		a[i].color = 'red'
		a[j].color = 'black'
		while i <= j:
			while (a[i].value < m):
				frames.append(copy.deepcopy(a))
				a[i].color = a[i].c
				i += 1
				a[i].color = 'red'
			while (a[j].value > m):
				frames.append(copy.deepcopy(a))
				a[j].color = a[j].c
				j -= 1
				a[j].color = 'black'
			if (i <= j):
				frames.append(copy.deepcopy(a))
				a[i], a[j] = a[j], a[i]
				a[i].color = a[i].c
				i += 1
				a[i].color = 'red'
				a[j].color = a[j].c
				j -= 1
				a[j].color = 'black'

		a[i].color = a[i].c
		a[j].color = a[j].c
		qs(a, l, j, frames)
		qs(a, i, r, frames)
