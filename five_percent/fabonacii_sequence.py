'''
Given a number N, this generates a fabonacii sequence of first N terms
'''


def generate_fabonacii_sequence(upper_limit):
    f_zero = 0
    f_one = 1
    f_prev_minus_one = f_one
    f_prev_minus_two = f_zero
    fabonacii = []

    if (upper_limit == 1):
        fabonacii.append(f_zero)
    else:
        fabonacii.append(f_zero)
        fabonacii.append(f_one)
        for x in range(1, (upper_limit - 1)):
            fabonacii.append(f_prev_minus_two + f_prev_minus_one)
            f_prev_minus_two = f_prev_minus_one
            f_prev_minus_one = x

    return fabonacii


def main():
    num = int(input('Enter the number to generate first N fabonacii num = '))

    if (num < 0):
        print('Enetr valid number')
    else:
        print('First ' + str(num) + ' fabonacci nums are : ' +
              str(generate_fabonacii_sequence(num)))

if __name__ == '__main__':
    main()
