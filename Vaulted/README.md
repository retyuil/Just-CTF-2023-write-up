
# Vaulted Crypto

This challenge ask us to provide 3 valid signature for the message get_flag by using public key present in a list.

Fortunately we can add one public key of our choice in the public key's list 

Firstly I tried to crack the 3 public keys provided by using sage math.

But all the key were generated securely.

By reading the source code of the librairie coincurve used in the challenge, I noticed that there is three ways to define a public key : compressed , non compressed, hybrid.

No matter the method you choose , the Publickey object define is the same, so the three different key will be present in the public key list. 

We just have to add one of the key to the list of public key, sign the message with our key and to provide our couples of key and signature :

```
{"method" : "enroll", "pubkey" : "02a36b5d06272edb5c9c074fccae7054cbd2a8c92bff317a9c177949ffef0a705f"}
{"method" : "get_flag" , "pubkeys" : ["02a36b5d06272edb5c9c074fccae7054cbd2a8c92bff317a9c177949ffef0a705f" , "04a36b5d06272edb5c9c074fccae7054cbd2a8c92bff317a9c177949ffef0a705f28ba48250ffafb5f8792de21c1b5f8d93f5338f1338efeb65121531617804b7c", "06a36b5d06272edb5c9c074fccae7054cbd2a8c92bff317a9c177949ffef0a705f28ba48250ffafb5f8792de21c1b5f8d93f5338f1338efeb65121531617804b7c"], "signatures" : ["30440220503289f83fe93fe8803c1e3ccddf2a331ff31f73d38cdc79d7b2369ae085dcd502205860e9a16fb2f8c70a44ce9b5a110837b26ff093941d4583467ec5df31ec4ba3", "30440220503289f83fe93fe8803c1e3ccddf2a331ff31f73d38cdc79d7b2369ae085dcd502205860e9a16fb2f8c70a44ce9b5a110837b26ff093941d4583467ec5df31ec4ba3", "30440220503289f83fe93fe8803c1e3ccddf2a331ff31f73d38cdc79d7b2369ae085dcd502205860e9a16fb2f8c70a44ce9b5a110837b26ff093941d4583467ec5df31ec4ba3"]}
```

Not really a crypto chall, but still interesting. 