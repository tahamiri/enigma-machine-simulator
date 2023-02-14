from apscheduler.schedulers.blocking import BlockingScheduler
import random
sched = BlockingScheduler()

f = open("rotors.txt", "r")
r1 = f.readline()
r2 = f.readline()
r3 = f.readline()
r4 = f.readline()
r5 = f.readline()
f.close()

r1 = r1[0:53]
r2 = r2[0:53]
r3 = r3[0:53]
r4 = r4[0:53]
r5 = r5[0:53]
q = [r1 , r2 , r3 , r4 , r5]

a = int(input("baraye tanzimat dasti adad 0 va baraye tanzimat khodkar adad 1 ra vared konid:\n"))
n1 = 0
n2 = 0
n3 = 0
o = []
for i in range(0 , 53):
    o.append(i)

if a == 0:
    z = int(input("jeyegah1(adadi az 1 ta 5 vared konid, entekhab adad 1 yani shoma rotor1 ra dar jayegah1 migozarid):\n"))
    if z == 1:
        n1 = r1
    elif z == 2:
        n1 = r2
    elif z == 3:
        n1 = r3
    elif z == 4:
        n1 = r4
    elif z == 5:
        n1 = r5
    else:
        print("az aval run kon va bein 1 ta 5 vared kon.")
    x = int(input("jeyegah2(adadi az 1 ta 5 vared konid, entekhab adad 1 yani shoma rotor1 ra dar jayegah2 migozarid):\n"))
    if x == z:
        print("az aval run kon va tekrari vared nakon.")
    elif x == 1:
        n2 = r1
    elif x == 2:
        n2 = r2
    elif x == 3:
        n2 = r3
    elif x == 4:
        n2 = r4
    elif x == 5:
        n2 = r5
    else:
        print("az aval run kon va bein 1 ta 5 vared kon.")
    y = int(input("jeyegah2(adadi az 1 ta 5 vared konid, entekhab adad 1 yani shoma rotor1 ra dar jayegah2 migozarid):\n"))
    if y == z or y == x:
        print("az aval run kon va tekrari vared nakon.")
    elif y == 1:
        n3 = r1
    elif y == 2:
        n3 = r2
    elif y == 3:
        n3 = r3
    elif y == 4:
        n3 = r4
    elif y == 5:
        n3 = r5
    else:
        print("az aval run kon va bein 1 ta 5 vared kon.")
    print("tarz gharar gereftan rotor ha:\n")
    z = int(input("rotor1 az chandomin character aghaz shavad?(lotfan bein 1 ta 53 entekhab konid):\n"))
    n1 = n1[(z-1):] + n1[0:(z-1)]
    z = int(input("rotor2 az chandomin character aghaz shavad?(lotfan bein 1 ta 53 entekhab konid):\n"))
    n2 = n2[(z-1):] + n2[0:(z-1)]
    z = int(input("rotor3 az chandomin character aghaz shavad?(lotfan bein 1 ta 53 entekhab konid):\n"))
    n3 = n3[(z-1):] + n3[0:(z-1)]
    f = open("setting.txt", "w")
    f.writelines([n1,"\n",n2,"\n",n3])
    f.close()


elif a == 1:
    @sched.scheduled_job('interval', seconds=3600)
    def timed_job():
        random.shuffle(q)
        n1 = q[0]
        n2 = q[1]
        n3 = q[2]
        random.shuffle(o)
        n1 = n1[o[0]:] + n1[0:o[0]]
        n3 = n3[o[1]:] + n3[0:o[1]]
        n3 = n3[o[2]:] + n3[0:o[2]]
        
        f = open("setting.txt", "w")
        f.writelines([n1,"\n",n2,"\n",n3])
        f.close()
    sched.start()

else:
    print("az aval run kon adad bein 1 , 0 bede.")
