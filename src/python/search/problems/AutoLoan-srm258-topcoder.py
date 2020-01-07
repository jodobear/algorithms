'''AutoLoan - SRM 258 - Topcoder
Problem Statement:
Auto dealerships frequently advertise tempting loan offers in order to make it easier for people to afford the "car of their dreams". A typical sales tactic is to show you various cars, and then talk in terms of what your monthly payment would be, to say nothing of how much you are actually paying for the car, how much interest you pay, or how long you have to make payments.

A typical auto loan is calculated using a fixed interest rate, and is set up so that you make the same monthly payment for a set period of time in order to fully pay off the balance. The balance of your loan starts out as the sticker price of the car. Each month, the monthly interest is added to your balance, and the amount of your payment is subtracted from your balance. (The payment is subtracted after the interest is added.) The monthly interest rate is 1/12 of the yearly interest rate. Thus, if your annual percentage rate is 12%, then 1% of the remaining balance would be charged as interest each month.

You have been checking out some of the cars at your local dealership, TopAuto. An excited salesman has just approached you, shouting about how you can have the car you are looking at for a payment of only monthlyPayment for only loanTerm months! You are to return a double indicating the annual percentage rate of the loan, assuming that the initial balance of the loan is price.

Definitions:
Class:	AutoLoan
Method:	interestRate
Parameters:	double, double, int
Returns:	double
Method signature:	double interestRate(double price, double monthlyPayment, int loanTerm)
(be sure your method is public)

Notes:
-	Because of the way interest is compounded monthly, the actual interest accrued over the course of a year is not necessarily the same as (balance * yearly interest rate). In fact, it's usually more.
-	In a real situation, information like this would typically need to be disclosed, but since you aren't at a point of signing any paperwork, the salesman has no legal obligation to tell you anything.
-	The return value must be within 1e-9 absolute or relative error of the actual result.

Constraints:
-	price will be between 1 and 1000000, inclusive.
-	monthlyPayment will be between 0 and price / 2, inclusive.
-	loanTerm will be between 1 and 600, inclusive.
-	The resulting interest rate will be between 0 and 100, inclusive.

Examples:
0)
6800
100
68
Returns: 1.3322616182218813E-13

Noting that 68 payments of 100 equals the total price of 6800, so there is no interest.
1)
2000
510
4
Returns: 9.56205462458368

Here, we do pay a little interest. At 9.562% annual interest, that means each month we pay 0.7968% of the balance in interest. Our payment schedule looks like this:

Month   | + Interest | - Payment | = Balance
--------------------------------------------
        |            |           |  2000.00
    1   |     15.94  |   510.00  |  1505.94
    2   |     12.00  |   510.00  |  1007.94
    3   |      8.03  |   510.00  |   505.97
    4   |      4.03  |   510.00  |     0.00

2)
15000
364
48
Returns: 7.687856394581649

This is similar to what purchasing a new car with no money down might look like, if you make payments for 4 years.
'''

def calculate_interest(p, m, n):
    '''Calculate annual compound interest.
    Max loan term is 600 so, we can iterate up to 600 times and if we pay off the loan before the loan term then our interest is too low and if we are still left with loan after the loan term then our interest is too high.
    This can then be solved with doing a binary search to find the correct(closest) interest rate.

    Let the monthly compounding factor, c = 1 + interestRate / 1200 (Thus, for 12% interest, c = 1.01),
    m = monthlyPayment,
    p = price,
    n = loanTerm

    Then, m * (c ^ n - 1) = p * c ^ n * (c - 1).
    '''
    if p == m * n:
        return 0
    lo = 0
    hi = 100
    while (lo < hi):
        mid = lo + (hi - lo) / 2
        c = 1 + (mid / 1200)
        monthly_payment_calc = m * (c ** (n - 1))
        principal_payment_cal = p * c ** (n * (c - 1))
        if monthly_payment_calc == principal_payment_cal:
            return mid
        elif monthly_payment_calc > principal_payment_cal:
            hi = mid
        else:
            lo = mid
    return lo

p = int(input())
m = int(input())
n = int(input())

print(calculate_interest(p, m, n))
