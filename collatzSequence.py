def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3 * number + 1
        
try:
    num=int(input('Enter a number: '))
    while num != 1:
        print(num, end=' ')
        num=collatz(num)
    print(1)
except ValueError:
    print("Enter a valid integer.")