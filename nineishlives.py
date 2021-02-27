import random
print('Welcome to NINE lives')


def isletterin(letter,lisp,lisp2):
    l3=[]
    for i in range(len(lisp)):
        if lisp[i]== letter:
            l3.append(i)
    if len(l3)>0:
        for i in l3:
            lisp2[i]=letter
        return 1
randomword=['pizza','roman','healthy','cart','difficult','margerine']
rchoice=random.choice(randomword)
rchoicelist =list(rchoice)
guesslist= list(len(rchoicelist)*'*')
count=0

difficulty = input('Select your difficulty level \n1. Easy \n2. Medium \n3. Hard\n')
di = int(difficulty)
if di ==2:
    lives= 6
elif di == 3:
    lives = 3
else:
    lives = 9
while 1:
    print(guesslist)
    print('you have ' + str(lives) + ' lives left')
    if lives != 0:
        if '*' in guesslist:
            usrguess = input('Guess the letter \n')
            k=isletterin(usrguess,rchoicelist,guesslist)
            if k != 1:
                lives=lives-1
        else:
            print ('you won with '+ str(lives) +' lives left')
            break
    else:
        print('you lost, the word was '+ rchoice)
        for i in guesslist:
            if i == '*':
                count+=1
        print('you guessed '+str(len(guesslist)-count)+' letters right')

        break