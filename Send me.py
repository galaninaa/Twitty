import SimpleHTTPServer
import SocketServer

port = 8989

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("",port),Handler)

print "serving at port ",port
httpd.serve_forever()
