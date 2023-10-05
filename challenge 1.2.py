#Write a program that determines whether a year entered by the user is a leap year or not using if -elif-else statements.
def checkleapyear(y):
  if y % 4 == 0:
    if y % 100 == 0:
      if y % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
y = 2024
if (checkleapyear(y)):
  print("The given year is leap year")
else:
  print("The given year is not a leap year")
