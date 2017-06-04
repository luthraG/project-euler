'''
Problem Id : 1
Problem Statement : If we list all the natural numbers below 10 that are
    multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_multiple_3_and_5(upper_limit):
    retVal = 0
    if upper_limit > 0:
        for x in range(1, upper_limit):
            if (x % 3 == 0 or x % 5 == 0):
                retVal += x
        return retVal
    else:
        return retVal


def main():
    num = int(input('Enter the number = '))
    print('Sum of all multiples of 3 and 5 below : ' + str(num) +
          ' is : ' + str(sum_multiple_3_and_5(num)))

if __name__ == '__main__':
    main()
