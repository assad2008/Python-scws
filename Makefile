all:
	gcc scws.c -shared -o _scws.so -I /usr/include/python2.6 -I/usr/local/scws/include/scws -fPIC -lscws
clean:
	rm _scws.so
