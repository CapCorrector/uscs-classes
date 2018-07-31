import os.path
from nameko.rpc import rpc, RpcProxy

class File():
	name = "FileService"
	@rpc
	def getFileContents(self, fname):
		fname = '/app/' + fname
		if os.path.isfile(fname):
			f = open(fname, 'r')
			fcont = f.read()
			f.close()
			return fcont
		else:
			return 'There is no such file ' + fname

class FRPC():
	name = "FRPC"
	
	fs = RpcProxy("FileService")
	@rpc
	def remote_file(self, fname):
		return self.fs.getFileContents(fname)
