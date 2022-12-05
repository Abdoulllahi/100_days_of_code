'''
 # @ Author: Abdou Lahi DIOP
 # @ Create Time: 2022-12-05 22:19:31
 # @ Modified by: Abdou Lahi DIOP
 # @ Modified time: 2022-12-05 22:27:24
 # @ Description:
 '''

def is_leap(year):
    """_summary_

    Args:
        year (int): the year we want to check if it is leap or not
    Returns:
        _boolean_: true or false
    """    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (is_leap(year)):
        month_days[1] = 29
    return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)