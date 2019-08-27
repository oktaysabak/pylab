def collatz(number):
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        else:
            print(3 * number +1)
            return 3 * number + 1
print('Enter number: ')
while True:
    try:
        number = int(input())
        if number != 1 and number >1:
            collatz(number)
        else:
            print('program finished')
            break
    except:
        print('write an integer please')

