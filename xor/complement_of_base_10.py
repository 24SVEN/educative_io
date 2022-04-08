def calculate_bitwise_complement(n):
    # TODO: Write your code here

    complement = 1

    num = n
    count = 0
    #this is basically taking a number for ex 8 and converting it to bit
    #then shifting to right until it is 0
    #1000
    #100
    #10
    #1
    #0

    #count ends up being 4

    #alternative and more intuitive if interviewer allows bit
    #count = len(bin(n))-2
    #need to subtract 2 since bin retruns 0b in the beginnning of string.
    while num != 0 :
        count+=1
        num = num>> 1

    
    
    for i in range(count):
        n = (complement ^ n)
        complement = complement << 1

    return n

def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()