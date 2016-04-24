#!/bin/env python
#coding:utf-8

import socket
import binascii

def login(url,port):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(30)
	s.connect((url,port))

	_header = "46494e53"
	_len = "0000000C"
	_command = "00000000"
	_code = "00000000"
	_client = "00000000"
	_session = _header + _len + _command + _code + _client
	
	s.send(binascii.unhexlify(_session))
	result = s.recv(1024)
	
	if len(result) > 23:
		r_header = binascii.b2a_hex(result[:4])
		ip = binascii.b2a_hex(result[23])
		if str(r_header) == str(_header): 
			print "login successful",
			print "result end ip:{0}".format(int(ip,16))
			return True
	return False


login("220.161.188.250",9600)
