import random
import time

def generator(length,typePass):
    count = 0
    pwd = ""
    if typePass == '1':
        while count < length:
            k = chr(random.randint(48,57))
            pwd += k
            count += 1
    elif typePass == '2':
        while count < length:
            p = random.randint(0,1)
            if p == 0:
                k = chr(random.randint(65,90))
            else:
                k = chr(random.randint(97,122))
            pwd += k
            count += 1
    elif typePass == '3':
        while count < length:
            p = random.randint(0,2)
            if p == 0:
                k = chr(random.randint(65,90))
            elif p == 1:
                k = chr(random.randint(48,57))
            else:
                k = chr(random.randint(97,122))
            pwd += k
            count += 1
    elif typePass == '4':
        while count < length:
            p = random.randint(0,3)
            if p == 0:
                k = chr(random.randint(65,90))
            elif p == 1:
                k = chr(random.randint(48,57))
            elif p == 2:
                k = chr(random.randint(33,47))
            else:
                k = chr(random.randint(97,122))
            pwd += k
            count += 1
    else:
        print("Password Type Either 1, 2, 3 or 4!")

    print(f"\nPassword: {pwd}")

time.sleep(1)
print("\nType of password: \n[1] Digits only \n[2] Letters only \n[3] Digits & Letters mixture \n[4] Digits & Letters & Special characters \nMinimum Password Length is 4\n")
passType = input("Type of password: ")
length = int(input("Length of passowrd: "))
time.sleep(1)

if passType.isdigit() and length > 4:
    generator(length,passType)
else:
    print("ERROR: Make Sure the Length Of Password Is Greater Than 4 And That The Type Is An Integer")