#!/usr/bin/env python3
import sys
import fire

EP = "equal-principal-payment"
EP_LST = [EP, "equal-principal", "ep", "epp"]
EL = "equal-loan-payment"
EL_LST = [EL, "equal-loan", "el", "elp"]
LINE = "{:<6}{:<16}{:<16}{:<16}{:<16}"


def calculate(loan_amount, interest_rate, years=1, payment_type=EP):
    """A mortgage payment calculator."""

    print(
        f"Loan Amount: {loan_amount}, Interest Rate: {interest_rate}, Years: {years}, Loan Type: {payment_type}"
    )
    print("*" * 80)
    months = years * 12
    mir = interest_rate / 12
    if payment_type in EP_LST:
        equal_princial_payment(loan_amount, mir, months)
    elif payment_type in EL_LST:
        equal_loan_payment(loan_amount, mir, months)
    else:
        print(f"unknown payment type: {payment_type}")
        sys.exit(1)


def equal_princial_payment(la, mir, months):
    mn = la / months

    t1 = la
    t2 = 0
    for i in range(1, months + 1):
        if i % 20 == 1:
            print("")
            print(
                LINE.format(
                    *"Month Payment Principal Interest LoanAmount".split()))
            print("-" * 80)
        mi = t1 * mir
        t2 += mi
        t1 = t1 - mn
        if i == months:
            print(
                LINE.format(i, round(mn + mi, 2), round(mn, 2),
                            round(mi + t1, 2), 0))
        else:
            print(
                LINE.format(i, round(mn + mi, 2), round(mn, 2), round(mi, 2),
                            round(t1, 2)))

    print("*" * 80)
    print(
        f"Total Payment: {round(la+t2, 2)},\t Total Interest: {round(t2, 2)}")
    print("*" * 80)


def equal_loan_payment(la, mir, months):
    month_payment = elp_cal(la, mir, months, 0, la * mir)
    elp_display(la, mir, month_payment, months)


def elp_display(la, mir, mp, months):
    s = 0
    for i in range(1, months + 1):
        if i % 20 == 1:
            print("")
            print(
                LINE.format(
                    *"Month Payment Principal Interest LoanAmount".split()))
            print("-" * 80)
        mi = la * mir
        s += mi
        p = mp - mi
        la = la - p
        if i == months:
            print(
                LINE.format(i, round(mp, 2), round(p, 2), round(mi + la, 2),
                            0))
        else:
            print(
                LINE.format(i, round(mp, 2), round(p, 2), round(mi, 2),
                            round(la, 2)))

    print("*" * 80)
    print(
        f"Total Payment: {round(mp * months, 2)},\t Total Interest: {round(s, 2)}"
    )
    print("*" * 80)


def elp_cal(la, mir, months, left, right):
    m = (left + right) / 2
    r = la / months + m
    if abs(right - left) < 0.1:
        return r

    s = la
    i = 0
    while i < months and s > r:
        t = s * mir
        s = s - (r - t)
        i += 1

    if i < months:
        return elp_cal(la, mir, months, left, m)

    if abs(s) > 0.1:
        return elp_cal(la, mir, months, m, right)

    return r


if __name__ == '__main__':
    fire.Fire(calculate)
