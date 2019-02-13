"""
You can cd to the directory of that file and use python3
 key_value.storage.py --key {key} 
 to read all values from the key 
 or python3 key_value storage.py --key {key} --val {val} to write value to the key
 in your command line
 """

import argparse
import os
from tempfile import gettempdir
STORAGE_PATH = os.path.join(gettempdir(), 'storage.data')


def storage_init(STORAGE_PATH):
	""" Function that creates key-val storage from the file """
	storage = dict()
	parsed_keys=set()
	if not os.path.exists(STORAGE_PATH):
		with open(STORAGE_PATH, 'w') as f:
			pass
	with open(STORAGE_PATH, 'r+') as f:
		for line in f:
			key, value = line.split()
			if key in parsed_keys:
				storage[str(key)] += ', ' + value
			else:
				storage[str(key)] = value
			parsed_keys.add(str(key))
	return storage
		
		
def print_values(key:str,storage:dict):
	""" Function that print value(s) from requested key """
	if key in storage.keys():
		return storage[str(key)]
			
			
def parse_arguments(storage:dict):
	""" Function that parse arguments from the command line """
	parser = 														argparse.ArgumentParser(description='key_value_storage')

	parser.add_argument('--key', action = "store", dest="keys")
	parser.add_argument('--val', action = "store", dest="values")
	args = parser.parse_args()
	args = vars(args)
	if args['values'] is None:
		print(print_values(args['keys'], storage))
	else:
		with open(STORAGE_PATH, 'a') as f:
			f.write(args['keys']+' '+args['values']+'\n')
	return None
if __name__ == '__main__':
	storage = storage_init(STORAGE_PATH)
	parse_arguments(storage)
