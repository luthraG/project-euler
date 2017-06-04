'''
Find all the primes lesser than or equal to specified number
'''


def find_prime(upper_limit):
    primes = {}

    for y in range(2, upper_limit):
        primes[y] = True

    for x in range(2, upper_limit):
        if (x in primes):
            for z in range(x, (upper_limit), x):
                if (x != z and z in primes):
                    del(primes[z])

    return list(primes.keys())


def main():
    num = int(input('Enter number upto which primes are required = '))

    if (num < 0):
        print('Enter valid number')
    else:
        print('Prime numbers upto ' + str(num) +
              ' are = ' + str(find_prime(num)))

if __name__ == '__main__':
    main()
