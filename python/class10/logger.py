def process(fd, processor):
	next(processor)
	while True:
		line = fd.readline().strip()
		if not line:
			break
		processor.send(line)

def printer():
	while True:
		line = (yield)
		print(line)

def filter(keyword):
	while True:
		line = (yield)
		if keyword in line:
			print(line)

#f = open('short_log')
#process(f, printer())
#process(f, filter('stylesheet'))
#f.close()

with open('short_log') as fd:
	process(fd, filter('stylesheet'))
