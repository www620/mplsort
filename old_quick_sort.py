import copy
from data import *

def old_quick_sort(a):
	frames = [a[:]]
	na = copy.deepcopy(a)
	qs(na, 0, b - 1, frames)
	frames.append(na)
	return frames

def qs(a, l, r, frames):
	if l < r:
		i = l
		j = r
		a[i].color = 'red'
		a[j].color = 'black'
		while i < j:
			while (a[j].value >= a[l].value and i < j):
				frames.append(copy.deepcopy(a))
				a[j].color = a[j].c
				j -= 1
				a[j].color = 'black'
			while (a[i].value <= a[l].value and i < j):
				frames.append(copy.deepcopy(a))
				a[i].color = a[i].c
				i += 1
				a[i].color = 'red'
			if (i < j):
				frames.append(copy.deepcopy(a))
				a[i], a[j] = a[j], a[i]
				a[i].color, a[j].color = a[j].color, a[i].color

		a[i].color = a[i].c
		a[j].color = a[j].c
		a[i], a[l] = a[l], a[i]
		qs(a, l, i - 1, frames)
		qs(a, i + 1, r, frames)
