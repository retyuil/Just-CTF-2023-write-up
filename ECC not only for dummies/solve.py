#!/usr/bin/env python3
import secrets
import hashlib
from time import time
from pow import *
import socket 
q1 = "c[0] + c[1] + c[2]"
q2 = "c[0] + c[1] + c[2] + c[3]"
q3 = "c[0] + c[1] + c[2] + c[3] + c[4]"
q4 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5]"
q5 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6]"
q6 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7]"
q7 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8]"
q8 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8] + c[9]"
q9 = "c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8] + c[9] + c[10]"

question = [q1,q2,q3,q4,q5,q6,q7,q8,q9]

def verify_hash(prefix, answer):
    h = hashlib.sha256()
    h.update((prefix + answer).encode())
    bits = ''.join(bin(i)[2:].zfill(8) for i in h.digest())
    return bits.startswith('0' * 22)


def solve_hash(prefix):
    print(f'''
    sha256({prefix} + ???) == {'0'*22}({22})...
    ''')
    last = int(time())
    i = 0
    while not verify_hash(prefix, str(i)):
        if i % 1000000 == 0:
            print(i)
        i += 1
    print(int(time()) - last, 'seconds')
    print(f"sha256({prefix} + {i}) == {'0'*22}({22})")
    return(str(i))



"""
solve_hash("OM9FFVbxo7RYa2nP")
"""

HOST = 'eccnotonlyfordummies.nc.jctf.pro'
PORT = 1337

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

response = client.recv(4096)
response = response.decode()
print(response)
hashe = response.split("+")[0].split("(")[1]
hashe = hashe.replace(" ","")
print(hashe)
print(len(hashe))
decode_hash = solve_hash(hashe)
print(decode_hash.encode("utf-8"))
client.send((decode_hash + "\n").encode("utf-8"))
response = client.recv(4096)
response = response.decode()
print(response)
cpt_question = 0
binaire = "1 1 1"
binaire1 = "1 0 0"
binaire2 = "1 0 1"
binaire3 = "0 0 0"
fausse_reponse = []
laste_reponse = 0
solution = ""
for i in range(11):
    print("Sended : ", (question[cpt_question] + "\n").encode("utf-8"))
    client.send((question[cpt_question] + "\n").encode("utf-8"))
    response = client.recv(4096)
    response = response.decode()
    print("Response : ", response)
    chiffre = response.split(":")[1].split("\n")[0]
    chiffre = chiffre.replace(" ","")
    if "False" in response or "True" in response:
        fausse_reponse.append(str(i))
    else:
        if laste_reponse == 0:
            if "0" in  chiffre:
                solution = binaire3
            if "1" in  chiffre:
                solution = binaire1
            if "2" in  chiffre:
                solution = binaire2
            if "3" in  chiffre:
                solution = binaire
            laste_reponse = chiffre
        else:
            if chiffre == laste_reponse:
                solution = solution + " 0"
            else: 
                solution = solution + " 1"
            laste_reponse = chiffre


        cpt_question += 1
solution = solution + " 1"
print("solution : ", solution)
client.send((solution + "\n").encode("utf-8"))
print("Sended : ", (solution + "\n").encode("utf-8"))
response = client.recv(4096)
response = response.decode()
print("Response : ", response)

fausse_reponse = " ".join(fausse_reponse)
client.send((fausse_reponse + "\n").encode("utf-8"))
print("Sended : ", (fausse_reponse + "\n").encode("utf-8"))
response = client.recv(4096)
response = response.decode()
print("Response : ", response)