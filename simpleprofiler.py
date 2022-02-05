import logging

import time

logging.basicConfig(filename='exec-time.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def timeis(func):
	'''Decorator that reports the execution time.'''

	def wrap(*args, **kwargs):
		start = time.time() * 1000
		result = func(*args, **kwargs)
		### multiplying by 1000 will give in milliseconds
		end = time.time() * 1000
		logger.info(func.__name__, end - start)
		print(func.__name__, end - start)
		return result

	return wrap


@timeis
def countdown(n):
	'''Counts down'''
	for i in range(100000):
		continue
	while n > 0:
		n -= 1


countdown(5)
countdown(1000)