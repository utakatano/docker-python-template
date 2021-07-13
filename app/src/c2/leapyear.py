year = int(input("what year? "))

# determine if it is leap year
is_leap = False

# (1) leap year if it is divided by 4
# if year % 4 == 0:
#     # (2) not leap year if it is divided by 100
#     if year % 100 == 0:
#         # (3) leap year if it is divided by 400
#         if year % 400 == 0:
#             is_leap = True
#         else:
#             is_leap = False
#     else:
#         is_leap = True
# else:
#     is_leap = False

is_leap = (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0))

# display the result
if is_leap:
    print("This year is leap year")
else:
    print("This year is not leap year")