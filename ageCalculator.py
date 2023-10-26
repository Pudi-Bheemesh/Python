import datetime as dt

user_year = int(input("Enter your date of birth: "))
a = dt.datetime.now()
pres_year = int(a.strftime("%Y"))
age = pres_year - user_year
print("your age is ",age)
if 0 < age <= 6:
    print("you are a baby")
elif 7 <= age <= 13:
    print("you are a child")
elif 14 <= age <= 17:
    print("you are a teenager")
elif 18 <= age <= 59:
    print("you are a adult")
elif age >= 60:
    print("you are a senior citizen")

future_date_after_2yrs = a + dt.timedelta(days = 730)
 
future_date_after_2days = a + dt.timedelta(days = 2)
 
# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

past_date_before_2yrs = a - dt.timedelta(days = 730)
 
# for two hours
past_date_before_2hours = a - dt.timedelta(hours = 2)
 
 
# printing calculated past_dates
print('past_date_before_2yrs:', str(past_date_before_2yrs))
print('past_date_before_2hours:', str(past_date_before_2hours))