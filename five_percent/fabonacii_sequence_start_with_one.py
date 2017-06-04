'''
Generates the fabonacii sequence whoes first term starts with 1
'''


def generate_fabonacii_sequence(upper_limit):
    f_one = 1
    f_two = 2
    f_prev_minus_one = f_two
    f_prev_minus_two = f_one
    fabonacii = []

    if (upper_limit == 1):
        fabonacii.append(f_one)
    else:
        fabonacii.append(f_one)
        fabonacii.append(f_two)
        for x in range(1, (upper_limit - 1)):
            tmp = f_prev_minus_one + f_prev_minus_two
            fabonacii.append(tmp)
            f_prev_minus_two = f_prev_minus_one
            f_prev_minus_one = tmp

    return fabonacii


def main():
    num = int(input('Enter num for which first N fabonacii num are req = '))

    if (num < 0):
        print('Enetr valid number')
    else:
        print('First ' + str(num) + ' fabonacii numbers are : ' +
              str(generate_fabonacii_sequence(num)))

if __name__ == '__main__':
    main()
