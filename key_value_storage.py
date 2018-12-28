#избавиться от перезаписи
#import библиотек
import argparse
import os
from tempfile import gettempdir
storage_path=os.path.join(gettempdir(), 'storage.data')
a=dict()
c=set()
if not os.path.exists(storage_path):
	with open(storage_path, 'w') as f:
		pass
with open(storage_path, 'r+') as f:
	#словарь
	for line in f:
		key, value=line.split()
		if key in c:
			a[str(key)]+=', ' + value
		else:
			a[str(key)]=value
		c.add(key)
	#функция отвечает за вывод
	def print_values(key):
		global a
		if key in a.keys():
			print(a[str(key)])
		else:
			print(None)
	parser = 														argparse.ArgumentParser(description='key-value storage')

	parser.add_argument('--key', action="store", dest="keys")
	parser.add_argument('--val', action="store", dest="values")
	args = parser.parse_args()
	args=vars(args)
	if args['values']==None:
		print_values(args['keys'])
	else:
		f.write(args['keys']+' '+args['values']+'\n')