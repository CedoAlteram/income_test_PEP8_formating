import sys

grossWages = int(sys.argv[1])
taxableInterest = int(sys.argv[2])
dividends = int(sys.argv[3])
qualifiedDividends = int(sys.argv[4])
iraDeduction = int(sys.argv[5])
studentLoanInterest = int(sys.argv[6])

income = (grossWages
          + taxableInterest
          + (dividends - qualifiedDividends)
          - iraDeduction
          - studentLoanInterest)

print(income)

if income > 100000:
    print("income is > %s" %income)
else:
    print("income is > {}, and that's ok" .format(income))
