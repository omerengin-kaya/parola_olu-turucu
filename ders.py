import random

karakterler =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunluğu = int(input("parolanin uzunluğunu girin: "))

parola =""

for i in range(parola_uzunluğu):
    
    parola += random.choice(karakterler)

print("Parola: " + parola)

