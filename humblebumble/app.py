import sys

while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
counter = 0
while counter < 24:
    counter = counter + 1
    if counter % 2 == 0:
        continue
    print(counter)
print('-----------')
while True:
    print('type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed ' + response + ' ')

