

num = int(input("Input a number to reverse: "))

reversed_num = 0
while num > 0:
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10

print("Result:", reversed_num)