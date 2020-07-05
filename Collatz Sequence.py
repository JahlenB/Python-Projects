print('Enter a number:')
number = input()

def collatz():
    global number
    if ((int(number)) % 2 == 0):
        print (str(int(number)//2))
        number = int(int(number)//2)
    else:
        print (str((3 * int(number)) + 1))
        number = int((3 * int(number)) + 1)

try:
    while int(number)!=1:
        collatz()

except ValueError:
    print('You must enter a number')
