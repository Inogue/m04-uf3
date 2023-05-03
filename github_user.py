#!/usr/bin/python3

import request
import sys

print(len(sys.argv))

if len(sys.argv) < 2:
	print("Error: Falta el nombre de usuario")
	print("\t"+sys.argv[0]+" NOMBRE_USUARIO")
	exit()

api_url = "https://api.github.com/users/"+sys.argv[1]

response = request.get(api_url)

info = response.json()

print(info)
