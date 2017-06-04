'''
Given a number, this returns the fabonacii number
'''


def generate_fabonacii(upper_limit):
    if (upper_limit < 0):
        return 0
    elif (upper_limit == 0):
        return 0
    elif (upper_limit == 1):
        return 1
    else:
        val1 = generate_fabonacii(upper_limit - 1)
        val2 = generate_fabonacii(upper_limit - 2)
        return (val1 + val2)


def main():
    num = int(input('Enter the number below which fabonacii number'
                    + 'needs to be generated = '))

    if (num < 0):
        print('Enter a valid non negative number')
    else:
        print('Fabonacii number below : ' + str(num) +
              ' are : ' + str(generate_fabonacii(num)))

if __name__ == '__main__':
    main()
