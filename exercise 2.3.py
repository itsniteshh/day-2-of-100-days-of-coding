# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
remaining_age = 90 - int(age)
print(f"Remaining age: {remaining_age}")

remaining_days = (remaining_age * 365) 
print(f"Remaining days: {remaining_days}")

remaining_weeks= remaining_days / 7
print(f"Remaining weeks: {remaining_weeks}")

remaining_months = remaining_days / 30
print(f"Remaining months: {remaining_months}")

print(f"You have a total of {remaining_days} days remaining, {remaining_months} remaining months and {remaining_weeks} remaining weeks.")






