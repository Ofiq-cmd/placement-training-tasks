days = int(input("enter allowed days: "))
return_days = int(input("enter returned after the days: "))
late = return_days - days
print("late days: ", late)
fine = late*5
print("fine: ", fine)