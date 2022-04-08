def find_happy_number(num):
    # TODO: Write your code here
    def calculation(num):
        return sum([int(digit)**2 for digit in str(num)])
    
    fast = num

    while calculation(num) and calculation(calculation(num)):
        num = calculation(num)
        fast = calculation(calculation(fast))

        if num == 1:
            return True

        if num == fast:
            return False






def main():
  print(find_happy_number(19))
  print(find_happy_number(12))


main()
