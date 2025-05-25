def addDigits(num):
    if num == 0:
        return 0
    return 1 + (num - 1) % 9
    #while num >= 10:
      #  temp_sum = 0
      #  for digit in str(num):
      #      temp_sum += int(digit)
      #  num = temp_sum
   # return num


number = 97
print(addDigits(number))