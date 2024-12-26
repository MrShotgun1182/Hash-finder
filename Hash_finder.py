import hashlib

i = 1
a = "my text"
number = int(input("last numbers in hash: "))

while True:
    a += str(i)
    i += 1
    byte_message = bytes(a, 'utf-8')
    test = hashlib.sha256(byte_message).hexdigest()
    if number == test[-2:]: 
        print(test, "this str is true: ", a)
        break

a = input ()
