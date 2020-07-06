spam = []

try:
    while True:
        print('Enter item ' + str(len(spam)+1) + '. Press enter to stop')
        name = input()
        if name =="":
            break
        spam = spam + [name]

    for i in range(len(spam)-1):
        print (spam[i], end=", ")

    print ('and ' + spam[-1])

except IndexError:
    print('You didn\'t enter data!')
