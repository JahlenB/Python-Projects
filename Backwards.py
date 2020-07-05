print('This program will take the user\'s input and write it backwards')
print('Input text below')
string = input()

for char in range(len(string) -1, -1, -1):
    print(string[char], end="")
print("\n")
