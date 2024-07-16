import datetime
import math
from dateutil.relativedelta import relativedelta
def monthly_details():
    customer_id = input("Customer Id:- ")
    customer_name = str(input("Customer Name:-"))
    amount = int(input("Amount:-"))
    months = int(input("Months:-"))
    interest = amount*months*0.03
    total_amount = int(amount+interest)
    emi = math.ceil(total_amount/months)
    print(amount,total_amount, months,emi)
    issue_date = datetime.date.today()
    last_emi_date = relativedelta(months=months)
    print(issue_date,issue_date+last_emi_date)
    paper_charges = int(amount*0.01)
    print(paper_charges)
    
x = monthly_details()

