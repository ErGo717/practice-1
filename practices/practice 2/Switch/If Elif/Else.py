day = 6
match day:
  case 1:
    print("Mon")
  case 2:
    print("Tue")
  case 3:
    print("Wed")
  case 4:
    print("Thu")
  case 5:
    print("Fri")
  case 6:
    print("Sat")
  case 7:
    print("Sun")



day = 2
match day:
  case 6: #if
    print("It is Saturday")
  case 7: #elif
    print("It is Sunday")
  case _: #else
    print("Waiting for the weekend")



day = 7
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("It is a school day")
  case 6 | 7:
    print("Weekend time!")


month = 6
day = 3
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 6:
    print("A weekday in June")
  case _:
    print("No match found")

day = 5
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Ohhh no,school")
  case 6 | 7:
    print("Week days")