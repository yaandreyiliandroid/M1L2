import random
passwords = "123456,7,8,9,0,/,*,+,-"
nhguhgu = int(input("какаю длина пароля тебе нужна?")) 
symbol = ""

for i in range(nhguhgu):
    symbol + random.choice(passwords)

print(passwords)

