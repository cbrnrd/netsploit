import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.bind(("0.0.0.0", sys.argv[1]))
    print "Listening on port {}".format(sys.argv[1])
except:
    print "Failed to bind to {}".format(sys.argv[1])
    sys.exit(1)
    
sock.listen(5)
while True:
    try:
        connection, address = s.accept()
        buf = connection.recv(256)
        print buf
    except KeyboardInterrupt:
        print "\nExiting"
        exit(0)
