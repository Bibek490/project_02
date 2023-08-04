bank_name=str(input("enter the bank you want to join.."))

account_creation=str(input("enter your name ?"))
P=float(input("enter the amount you want to depsoite.."))

T=float(input("enter the years you want to despot the money"))
R=float(input("enter the intrest rate you want.."))

interest=(P*T*R)/100

my_withdrawn="i want to join in the {}.My bank info is {}.At 2012 AD i created my account with the principal {} with the intreat rate {} at the time of {}. i got intreast {}."

print(my_withdrawn.format(bank_name,account_creation,P,T,R,interest))