import copy
from data import *

def heap_sort(a):
	frames = [a[:]]
	na = copy.deepcopy(a)
	for child in range(b // 2 - 1, -1, -1):
		heap_adjust(na, child, b, frames)
	for child in range(b - 1, 0, -1):
		na[child], na[0] = na[0], na[child]
		heap_adjust(na, 0, child, frames)
	frames.append(na)
	return frames

def heap_adjust(a, i, j, frames):
	child = i * 2 + 1
	while child < j:
		if child + 1 < j and a[child].value < a[child + 1].value:
			child += 1
		frames.append(copy.deepcopy(a))
		
		if a[child].value > a[i].value:
			a[child].color = 'black'
			a[i].color = 'red'
			a[i], a[child] = a[child], a[i]
			frames.append(copy.deepcopy(a))
			a[child].color = a[child].c
			a[i].color = a[i].c
			i = child
			child = child * 2 + 1
		else:
			break

		