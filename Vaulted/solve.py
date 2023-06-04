import coincurve
from coincurve import PublicKey
def sign_message(private_key, message):
    # Convertir la clé privée en une instance de coincurve.PrivateKey
    
    # Signer le message en utilisant la clé privée
    signature = private_key.sign(message)
    
    # Récupérer les composantes de la signature
    
    return signature

# Clé privée pour la signature (à titre d'exemple)
private_key = coincurve.PrivateKey(b"mael")
public_key = private_key.public_key

# Message à signer
message = b'get_flag'

signature = sign_message(private_key,message)
print("Signature : ",signature.hex())
is_valid = public_key.verify(signature, message)




is_valid = public_key.verify(signature, message)


pubkey1 = public_key.format(compressed=True).hex()
pubkey1 = PublicKey(bytes.fromhex(pubkey1))

pubkey2 = public_key.format(compressed=False).hex()
pubkey2 = PublicKey(bytes.fromhex(pubkey2))

pubkey3 = PublicKey(bytes.fromhex("06a36b5d06272edb5c9c074fccae7054cbd2a8c92bff317a9c177949ffef0a705f28ba48250ffafb5f8792de21c1b5f8d93f5338f1338efeb65121531617804b7c"))
print((pubkey1.format(compressed=True).hex()))
print((pubkey2.format(compressed=True).hex()))
print((pubkey3.format(compressed=True).hex()))


is_valid1 = pubkey1.verify(signature,message)
is_valid2 = pubkey2.verify(signature,message)
is_valid3 = pubkey3.verify(signature,message)

print(is_valid1,is_valid2,is_valid3)