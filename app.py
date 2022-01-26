#!/usr/local/bin/python3 
# Kevin Lizarazo
# simple 2020 tax calculator for those with W2s and freelance business income

from tabulate import tabulate

print("\nThis tax calculator assumes your income is from two sources:\n\n  1. W-2 (full withholding) \n  2. Schedule C (assuming no quarterly taxes paid) \n\nPlease fill out the prompts below.\n")

# get info
w2_wages = int(input('Enter your wages (W-2, box 1): '))
w2_tax_withheld = int(input('Enter your federal tax withheld (W-2, box 2): '))
sl_input = int(input('Enter student loan interest payments: ') or 0)
sc_net = int(input('Enter your business net income: '))

# calculate income, adjustments, deductions
total_income = w2_wages + sc_net
self_employment_tax = sc_net * .9235 * .153
modified_agi = total_income - (self_employment_tax * .5)
if modified_agi < 85000:
    studentloan_interest = sl_input - ((modified_agi - 70000) / 15000 * sl_input)
else: studentloan_interest = 0
qbid = sc_net * .9235 * .2

adjustments = studentloan_interest + (self_employment_tax * .5)
deductions = qbid + 12200

adjusted_income = total_income - adjustments
taxable_income = adjusted_income - deductions

# calculate tax
regular_tax = (9700 * .1) + (29775 * .12) + ((taxable_income - 9700 - 29775) * .22)
total_tax = regular_tax + self_employment_tax
TAX_BALANCE = round(total_tax - w2_tax_withheld, 2)

# RELAY INFO
if TAX_BALANCE > 0:
    refund_or_owe = 'YOU OWE:'
else:
    refund_or_owe = 'YOUR REFUND:'

l = [['Total income', total_income], ['Adjusted income', adjusted_income], ['Taxable income', taxable_income], ['Regular tax', regular_tax], ['Self-employment tax', self_employment_tax], ['Total tax', total_tax], ['Federal tax withheld', w2_tax_withheld], [refund_or_owe, abs(TAX_BALANCE)] ]
table = tabulate(l, headers=['Category', 'Amount'], tablefmt='fancy_grid', floatfmt=".2f")
print('\n'); print(table); print('\n')
