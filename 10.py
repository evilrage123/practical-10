# Binary to decimal
fh = open('practical10.txt', 'w')
number = input('Enter the number base 2: ')
from_base = 2
answer = int(number, from_base)
fh.write(str(answer))
fh.write('\n')

# Decimal to binary
number = int(input('Enter the number from base 10: '))
answer = bin(number)
fh.write(str(answer[2:]))
