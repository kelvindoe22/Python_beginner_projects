import random
import string
combo = string.ascii_letters+string.digits+string.punctuation


def check_pass(p):
    for i in range(len(p)):
        if p[i] in string.ascii_uppercase:
            return 1
def check_num(p):
    for i in range(len(p)):
        if p[i] in string.digits:
            return 1

def createpass():
    password=[]
    password.clear()
    for num in range(8):
        k = random.choice(combo)
        password.append(k)
    return ''.join(password)

def check(pw):
    passtest = check_pass(pw)
    pastest2 = check_num(pw)
    if passtest == 1 and pastest2 == 1:
        return 1


while 1:
    pw= createpass()
    k=check(pw)
    if k == 1:
        print ('pass created '+ pw)
        ip=input('enter 1 if you want a new one or any letter to exit\n')
        if ip !='1':
            break
        else:
            pass
    else:
        pass