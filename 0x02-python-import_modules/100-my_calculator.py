#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, o, b = int(argv[1]), argv[2], int(argv[3])
    oper = {'+': add, '-': sub, '*': mul, '/': div}
    if o not in oper:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print('{} {} {} = {}'.format(a, o, b, oper[o](a, b)))
