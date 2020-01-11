#!/usr/bin/env python3
import sys
import fire


EP = "equal-principal-payment"
EP_LST = [EP, "equal-principal", "ep", "epp"]
EL = "equal-loan-payment"
EL_LST = [EL, "equal-loan", "el", "elp"]


def calculate(loan_amount, interest_rate, years=1, payment_type=EP):
    """A mortgage payment calculator."""

    print(
        f"Loan Amount: {loan_amount}, Interest Rate: {interest_rate}, Years: {years}, Loan Type: {payment_type}")
    print("*"*80)
    months = years * 12
    mir = interest_rate / 12
    if payment_type in EP_LST:
        equal_princial_payment(loan_amount, mir, months)
    else:
        print(f"unknown payment type: {payment_type}")
        sys.exit(1)


def equal_princial_payment(la, mir, months):
    mn = round(la / months, 2)

    t1 = la
    t2 = 0
    for i in range(1, months+1):
        mi = round(t1 * mir, 2)
        t2 += mi
        t1 -= mn
        print(f"[{i}],\t Payment: {round(mn + mi, 2)},\t Interest: {mi}")

    print("*"*80)
    print(f"Total Payment: {round(la+t2, 2)},\t Total Interest: {t2}")
    print("*"*80)


if __name__ == '__main__':
    fire.Fire(calculate)
