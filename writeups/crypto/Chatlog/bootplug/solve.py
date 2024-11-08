from Crypto.Util.number import long_to_bytes as b2l
import owiener
import re

chat_log = open('chat.log','r').read()

params = re.findall(r'[0-9]{20,}',chat_log) # capture long digit sequences
n, e, ct = map(lambda x:int(x), params) # convert digit sequences to long types (integers)

d = owiener.attack(e, n) # run attack to recover private key
assert not d is None, "Attack failed" # assert that the private key was found

m = pow(ct, d, n) # decrypt ciphertext
message = b2l(m) # decode message
flag = re.findall(b'EPT\{.*\}', message)[0].decode() # regex the flag

print(flag) # print flag 🥳