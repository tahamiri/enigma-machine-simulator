import random

alefba = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

r1 = list(alefba)
random.shuffle(r1)
r1 = "".join(r1)

r2 = list(alefba)
random.shuffle(r2)
r2 = "".join(r2)

r3 = list(alefba)
random.shuffle(r3)
r3 = "".join(r3)

r4 = list(alefba)
random.shuffle(r4)
r4 = "".join(r4)

r5 = list(alefba)
random.shuffle(r5)
r5 = "".join(r5)



f = open("rotors.txt", "w")
f.writelines([r1,"\n",r2,"\n",r3,"\n",r4,"\n",r5])
f.close()