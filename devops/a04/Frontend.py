from nameko.standalone.rpc import ClusterRpcProxy
from nameko.web.handlers import http 

config = {
	'AMQP_URI': "pyamqp://test:test@10.0.0.3"
}

class HttpService:
	name = "http_service"
	@http('GET', '/get/<value>')
	def get_method(self, request, value):
		with ClusterRpcProxy(config) as cluster_rpc:
			return cluster_rpc.FRPC.remote_file(value)
