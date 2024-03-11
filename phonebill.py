def my_phone_bill(dailybill, days_in_a_month):
    monthly_bill = dailybill * days_in_a_month
    return monthly_bill

dailybill = float(input("Enter your daily Bill: "))
days = int(input ("Days used in the month: "))

monthly_Bill = my_phone_bill(dailybill, days)

print(monthly_Bill)


    