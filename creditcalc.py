from math import log, pow, ceil
import argparse
import sys


def incorrect_parameters():
    print('Incorrect parameters')
    exit()


def overpayment(a, n, p):
    print('Overpayment =', ceil(a * n - p))


def diff_payment(p, n, i):
    # differentiated payment: credit principal, count of periods,
    # credit interest
    i = i / (12 * 100)
    o = 0
    for m in range(1, n + 1):
        d = ceil(p / n + i * (p - p * (m - 1) / n))
        o += d
        print(f'Month {m}: paid out {d}')
    print('Overpayment = ', o - p)


def ann_payment(p, n, i):
    # annuity payment: credit principal, count of periods,
    # credit interest
    i = i / (12 * 100)
    a = ceil(p * (i * pow(1 + i, n) / (pow(1 + i, n) - 1)))
    print(f'Your annuity payment = {a}!')
    overpayment(a, n, p)


def principal(a, n, i):
    i = i / (12 * 100)
    p = a / (i * pow(1 + i, n) / (pow(1 + i, n) - 1))
    print(f'Your credit principal = {ceil(p)}!')
    overpayment(a, n, p)


def repay(p, a, i):
    i = i / (12 * 100)
    n = ceil(log(a / (a - i * p), 1 + i))
    print('You need', f' 1 year' if n // 12 == 1 else (f' {n // 12} years' if n > 12 else ''),
          f' {n} months' if n < 12 else (f' and {n % 12} months' if n % 12 != 0 else ''),
          ' to repay this credit!', sep='')
    overpayment(a, n, p)


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type",
                    help='the type of payments: "annuity" or "diff"')
parser.add_argument("-p", "--payment", type=int,
                    help="monthly payment")
parser.add_argument("-pr", "--principal", type=int,
                    help="principal")
parser.add_argument("-per", "--periods", type=int,
                    help="parameter denotes the number of months and/or years needed to repay the credit")
parser.add_argument("-i", "--interest", type=float,
                    help="specified without a percent sign")
args = parser.parse_args()
if len(sys.argv) < 4:
    incorrect_parameters()
if not (args.type == 'annuity' or args.type == 'diff'):
    incorrect_parameters()
if args.payment is not None and args.type == 'diff':
    incorrect_parameters()
if args.interest is None and args.type == 'annuity':
    incorrect_parameters()
if args.type == 'diff' and (args.payment is None):
    diff_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and (args.payment is None):
    ann_payment(args.principal, args.periods, args.interest)
elif args.type == 'annuity' and (args.principal is None):
    principal(args.payment, args.periods, args.interest)
elif args.type == 'annuity' and (args.periods is None):
    repay(args.principal, args.payment, args.interest)
else:
    exit()
exit()
