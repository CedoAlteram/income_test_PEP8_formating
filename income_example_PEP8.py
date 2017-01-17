import sys

grossWages = sys.argv[1]
taxableInterest = sys.argv[2]
dividends = sys.argv[3]
qualifiedDividends = sys.argv[4]
iraDeduction = sys.argv[5]
studentLoanInterest = sys.argv[6]

income = (grossWages
          + taxableInterest
          + (dividends - qualifiedDividends)
          - iraDeduction
          - studentLoanInterest)

print(income)