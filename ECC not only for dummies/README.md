# ECC not only for dummies

This challenge is dealing with Error correction code.

We have to guess 11 bits. To do that we can ask 11 question but in the 11 response 3 will be false.

This time we can't bruteforce the challenge because we need to crack a sha-256 at each attemp wich take around 12 secondes and we need to wait 5 secondes between each questions.

Luckily for us when the server is lying it always send a boolean. 
So we can ask the following question : 
```

c[0] + c[1] + c[2]
if the response is a boolean we know that the server is lying so we repeat the question
else we ask : 
c[0] + c[1] + c[2] + c[3]
if the answer is higher than the previous one we know that : 

c[3] == True. 

if the answer is a boolean we ask the same question.

...
...

we ask : 
c[0] + c[1] + c[2] + c[3] + c[4] + c[5] + c[6] + c[7] + c[8] + c[9]

The answer is either a boolean either we are at the last question.

```

with this technique we know the value of the bit 3,4,5,6,7,8,9

We just have to try all the possibilites for the bit 0,1,2,10
which takes on average 16 trials