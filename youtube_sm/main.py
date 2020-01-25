import time
import os
import sys

from .src.commands import Commands
from .src.tools import (
	print_debug)

def getpath():
	if os.name == 'nt':
		path = os.path.expanduser('~') + '/.youtube_sm/'
	else:
		if os.uname().sysname == 'Linux' or os.uname().sysname == 'Darwin':
			path = os.environ['HOME'] + '/.cache/youtube_sm/'
	return path

def main():
	# Init variable
	# Path of the cache
	print_debug('Hello :)')
	try:
		path = getpath()
	except KeyError:
		print_debug('HOME is not set', 1)
		exit()
	print_debug('Path: {}'.format(path))
	try:
		os.makedirs(path + 'data/')
	except:
		print_debug('Data already exist or can\'t be create', 1)
	del sys.argv[0]
	cmd = Commands(path)
	cmd.parser()
	cmd.router()
