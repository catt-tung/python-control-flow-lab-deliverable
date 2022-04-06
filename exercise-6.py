# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

input_month = input("Enter the month of the year (Jan - Dec): ")
input_day = int(input("Enter the day of the month: "))

winter = ["Dec", "Jan", "Feb", "Mar"]
spring = ["Apr", "May"]
summer = ["Jun", "Jul", "Aug", "Sep"]
fall = ["Oct", "Nov"]

if input_month in winter:
  if input_month == "Jan" or input_month == "Feb":
    print(f"{input_month} {input_day} is in winter.")
  elif input_month == "Dec":
    if input_day >= 21:
      print(f"{input_month} {input_day} is in winter.")
    else:
      print(f"{input_month} {input_day} is in fall.")
  elif input_month == "Mar":
    if input_day <= 19:
      print(f"{input_month} {input_day} is in winter.")
    else:
      print(f"{input_month} {input_day} is in spring.")
elif input_month in spring:
  print(f"{input_month} {input_day} is in spring.")
elif input_month in summer:
  if input_month == "Jul" or input_month == "Aug":
    print(f"{input_month} {input_day} is in summer.")
  elif input_month == "Jun":
    if input_day >= 21:
      print(f"{input_month} {input_day} is in summer.")
    else:
      print(f"{input_month} {input_day} is in spring.")
  elif input_month == "Sep":
    if input_day <= 21:
      print(f"{input_month} {input_day} is in summer.")
    else:
      print(f"{input_month} {input_day} is in fall.")
else:
  print(f"{input_month} {input_day} is in fall.")