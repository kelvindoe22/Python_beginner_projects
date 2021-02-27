import random
k=list(range(1,16))
rn=random.choice(k)

lives=3
print('Enter a number between 1-15\nGuess the number the computer has chosen\n')
while 1:
    user_input=input()
    if int(user_input) == rn:
        print('That was the correct number')
        break
    elif int(user_input) != rn:
        lives=lives-1
        if rn>int(user_input) and lives !=0:
            print ('try again but higher')
        elif rn<int(user_input) and lives !=0:
            print('try again but lower')
        else:
            print(f'you lost. The number was {rn}')
            break

input()
    
