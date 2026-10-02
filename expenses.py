expenses = []
total = 0
while True:
    new_expenses = input('entre the expense : ')

    if new_expenses== "done":
      break

    amount= float(input("entre the amount : $"))

    expense_details = [new_expenses, amount]
    print()
    expenses.append(expense_details)

    for new_expense in expenses:
       print(new_expense[0], new_expense[1])
       print()

for new_expense in expenses:
   total = total + new_expense[1]
print()


while True:
   print ("1 .Add expennse")
   print ("2 .view expenses")
   print ("3 .show total")
   print("4 . exit")
   choice = input("entre your choice ")

   if choice == '4':
     break
     print()

   if choice == '2':
      for expense in expenses:
         print(expense[0],expense[1])
         print()
   if choice =='3':
      for new_expense in expenses:
          total = total + new_expense[1]
       
      print("total expenses", total)
      print()
   if choice == '1':
      new_expense= input('entre the expense ')
      amount = float(input('entre the amount'))

      expense_details = [new_expenses, amount]
      expenses.append(expense_details)
      print()

