import argparse
import math
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", '--type')
    parser.add_argument("-pn", '--principal', type=int)
    parser.add_argument('-pm', '--payment', type=float)
    parser.add_argument('-pr', '--periods', type=int)
    parser.add_argument('--interest', type=float)
    args = parser.parse_args()
    loan_type = args.type
    interest = args.interest
    loan_principal = args.principal
    payment = args.payment
    periods = args.periods
    if loan_type != 'diff' and loan_type != 'annuity':
        print('Incorrect parameters')
        exit(0)
    if loan_type == 'diff':
        if payment is not None:
            print('Incorrect parameters')
            exit(0)
    if interest is None:
        print('Incorrect parameters')
        exit(0)
    if len(sys.argv) < 5:
        print('Incorrect parameters')
        exit(0)
    if interest is not None:
        if interest < 0:
            print('Incorrect parameters')
            exit(0)
    if loan_principal is not None:
        if loan_principal < 0:
            print('Incorrect parameters')
            exit(0)
    if payment is not None:
        if payment < 0:
            print('Incorrect parameters')
            exit(0)
    if periods is not None:
        if periods < 0:
            print('Incorrect parameters')
            exit(0)
    interest = interest / (12 * 100)
    if loan_type == 'annuity':
        if payment is None and periods is not None and loan_principal is not None:
            payment = math.ceil(annuity_payment(loan_principal, periods, interest))
            print(f'Your monthly payment: {payment}!')
        elif payment is not None and periods is None and loan_principal is not None:
            periods = math.ceil(months_num(loan_principal, payment, interest))
            years = periods // 12
            months = periods - years * 12
            if years == 0:
                if months == 1:
                    print(f'It will take {months} months to repay this loan!')
                else:
                    print(f'It will take {months} month to repay this loan!')
            else:
                if months == 1:
                    print(f'It will take {years} years and {months} month to repay this loan!')
                elif months == 0:
                    print(f'It will take {years} years to repay this loan!')
                else:
                    print(f'It will take {years} years and {months} months to repay this loan!')
        elif payment is not None and periods is not None and loan_principal is None:
            loan_principal = loan_principal_calc(payment, periods, interest)
            print(f'Your loan principal = {loan_principal}!')
        print(f'\nOverpayment = {math.ceil(payment * periods - loan_principal)}')
    else:
        mth_diff_pay(loan_principal, interest, periods)


def mth_diff_pay(loan_pr, i, per):
    total_pay = 0
    for month in range(1, per + 1):
        mth_pay = math.ceil(loan_pr / per + i * (loan_pr - (loan_pr * (month - 1) / per)))
        print(f'Month {month}: payment is {mth_pay}')
        total_pay += mth_pay
    print(f'\nOverpayment = {total_pay - loan_pr}')


def months_num(loan_principal, payment, interest):
    return math.log(payment / (payment - interest * loan_principal), 1 + interest)


def annuity_payment(loan_principal, periods, interest):
    return loan_principal * interest * (1 + interest) ** periods / ((1 + interest) ** periods - 1)


def loan_principal_calc(payment, periods, interest):
    return payment / (interest * (1 + interest) ** periods / ((1 + interest) ** periods - 1))


if __name__ == "__main__":
    main()
