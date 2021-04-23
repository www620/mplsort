import copy
from random import randint
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from data import *
from quick_sort import quick_sort
from merge_sort import merge_sort
from shell_sort import shell_sort
from heap_sort import heap_sort
from old_quick_sort import old_quick_sort

def rand(n):
	if n == 0:
		a = [Data(i + 1) for i in range(b)]
		for i in range(b):
			j = randint(i, b - 1)
			a[i], a[j] = a[j], a[i]

	elif n == 1:
		a = [Data(i) for i in range(b, 0, -1)]

	elif n == 2:
		r = b // 4
		a = [Data((i // r + 1) * r) for i in range(b)]
		for i in range(b):
			j = randint(i, b - 1)
			a[i], a[j] = a[j], a[i]

	elif n == 3:
		a = [Data(i + 1) for i in range(b)]
		i = randint(0, b - 1)
		j = randint(0, b - 1)
		while i == j:
			j = randint(0, b - 1)
		a[i], a[j] = a[j], a[i]

	elif n == 4:
		a = [Data(i + 1) for i in range(b)]
		for i in range(b):
			a[i // 2], a[i]= a[i], a[i // 2]

	return a

def main():
	"""主函数"""
	a = rand(0)

	sorts = [
		quick_sort,
		# old_quick_sort,
		# merge_sort,
		# shell_sort,
		# # heap_sort
	]

	titles = [
		'quick sort'
		# 'old_quick_sort',
		# 'merge sort',
		# 'shell sort',
		# 'heap sort'
	]

	frames = []
	axs = []

	for func in sorts:
		frames.append(func(a[:]))

	lf = max([len(i) for i in frames])
	fig = plt.figure(1, figsize=(16, 9))
	for i in range(len(sorts)):
		n = fig.add_subplot(111 + i)
		n.set_xticks([])
		n.set_yticks([])
		axs.append(n)
		

	def update(n):
		"""播放一帧动画"""
		bars = []
		for i in range(len(sorts)):
			if(len(frames[i]) > n):
				axs[i].cla()
				axs[i].set_title(titles[i])
				axs[i].set_xticks([])
				axs[i].set_yticks([])
				bars += axs[i].bar(
					list(range(b)),
					[d.value for d in frames[i][n]],
					1,
					color=[d.color for d in frames[i][n]]
				)
		return bars

	anim = animation.FuncAnimation(fig, update, frames=lf + 50, interval=1)
	anim.save(r'G:\python_work\mplsort\video\quick_sort.gif', fps=60)
	# plt.show()

main()