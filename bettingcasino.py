import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET =1

symbols = {
  "A ":2,
  "B" :4,
  "C" :6,
  "D" :8
  
}
ROWS = 3
COLS = 3

symbol_count= {
  "A ":2,
  "B" :4,
  "C" :6,
  "D" :8
}
symbol_value = {
  "A":2,
  "B": 4,
  "C":6,
  "D":8
}

     


def get_slot_machine_spin(rows,cols,symbols):
  all_symbols = [] #list
  for symbols,symbol_count in symbols.items ():#key and value
    for _ in range (symbol_count):#anonymous variable dont care count 
      all_symbols.append(symbols)#append add to the list
      
    columns = []
    for _ in range (cols):
      column =[]
      current_symbols = all_symbols[:] #copy of all symbols 
      for _ in range(rows): 
      
       value =random.choices(current_symbols)
       
       current_symbols.remove(value)
       column.append(value)
       
       columns.append(column)
       
    return columns 
  
def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i ,column in enumerate (columns): #enumerate gives index 0,1,2
      if i != len(columns) -1 :
       print(column[row], end="|" )
      else:
        print(column[row], end="")
        
    print()#prints new line at the end 


def deposit():
  while True:
    amount = input("what would you like to deposit ? $")
    if amount.isdigit():
      amount =int(amount)
      if amount > 0:
        break
      else: 
        print("amount must be geater than zero")
    else:
          print("please enter a number")


  return amount



def get_number_of_lines():

  while True:
   lines = input("Enter no of lines to bet on  (1 - " + str(MAX_LINES) + ")?  ")

   if lines.isdigit():
      lines =int(lines)
      if 1 <= lines <=MAX_LINES:
        break
      else: 
        print("enter valid number of lines")
  else:
       print("enter valid no:")

  return lines

def get_bet():

  while True:
    amount = input("how much would you like to bet on each line? $")
    if amount.isdigit():
      amount =int(amount)
      if MIN_BET <= amount <=MAX_BET:
        break
      else: 
        print(f"amount must be between ${MIN_BET} - ${MAX_BET}." )
    else:
          print("please enter a number")


  return amount
  



def Main():
 balance =  deposit()
 lines = get_number_of_lines()

 while True:

  bet = get_bet()
  total_bet = bet * lines
  if bet > balance:

   print(f"you do not have enough amount to place your bet : Account balance is ${balance}")
  else:
    break

 print(f"You are betting ${bet} on line {lines}. Possible win : ${total_bet} \n Balance is = ${balance- bet}")

#  print(f" your balance is : ${balance}  line ${lines} ")
slots =get_slot_machine_spin(ROWS,COLS,symbol_count)
print_slot_machine(slots)


Main()


       



