import os
pid=os.fork()
if pid==0:
	print('haha1...')
else:
	print('haha2...')

