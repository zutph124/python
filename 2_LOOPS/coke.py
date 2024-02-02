amount_due = 50

def calc():
  global amount_due
  print("Amount due: ", amount_due)
  insert = int(input("Insert coin: "))
  
  values = [25,10,5]
  if insert in values:
     amount_due = amount_due - insert

while (amount_due <= 50 and amount_due > 0) :
  calc()

print("Change Owned:", abs(amount_due))
