##with open('names.txt') as fd:
##    line = fd.readline()
##    while line:
##        print(line.strip())
##        line = fd.readline()

##class ManagedFiles:
##    def __init__(self, filename, mode='r'):
##        self._filename = filename
##        self._mode = mode
##
##    def __enter__(self):
##        print('enter...')
##        self._open_file = open(self._filename, self._mode)
##        return self._open_file
##
##    def __exit__(self, *args):
##        print('exit...')
##        print(args)
##        self._open_file.close()
##
##with ManagedFiles('names.txt') as fd:
##    line = fd.readline()
##    while line:
##        print(line.strip())
##        line = fd.readline()
##        
##print('='*40)
##print('Done')

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode='r'):
    print('enter...')
    fd = open(filename, mode)
    yield fd
    print('exit...')
    fd.close()

with open_file('names.txt') as fd:
    line = fd.readline()
    while line:
        print(line.strip())
        line = fd.readline()
