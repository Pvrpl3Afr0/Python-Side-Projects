#Test Password generator

import random #imports the random.sample func

s = "abcdefhijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
passlen = int(input("How many characters would you like in your password?"))
p = "".join(random.sample(s,passlen ))
print(p)

#I learned how to use the .join func by looking it up, the rest is
#self explanatory.
