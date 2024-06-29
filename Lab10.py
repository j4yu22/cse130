# 1. Name:
#      Jay Underwood
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      This program calculates the number of days between two given dates, accounting for leap years and validating input.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was implementing the input validation to make sure the user enters valid dates and handling edge cases such as leap years and invalid months or days. There was also some trouble shooting when the dates were the same.
# 5. How long did it take for you to complete the assignment?
#      About 4 hours total


def is_leap_year(year):
    """Determine if a year is a leap year.
    
    Parameters:
        year (int): The year to check.
    
    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    assert isinstance(year, int), "Year must be an integer"
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

def days_in_month(month, year):
    """Return the number of days in a given month of a given year.
    
    Parameters:
        month (int): The month (1-12).
        year (int): The year.
    
    Returns:
        int: The number of days in the month.
    """
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28

def days_between_dates(start_date, end_date):
    """Calculate the number of days between two dates.
    
    Parameters:
        start_date (tuple): The start date as (year, month, day).
        end_date (tuple): The end date as (year, month, day).
    
    Returns:
        int: The number of days between the dates.
    """
    start_year, start_month, start_day = start_date
    end_year, end_month, end_day = end_date
    
    assert start_year >= 1753, "Year must be 1753 or later"
    assert end_year >= 1753, "Year must be 1753 or later"
    
    if (start_year, start_month, start_day) > (end_year, end_month, end_day):
        return "End date must be after start date"

    if (start_year, start_month, start_day) == (end_year, end_month, end_day):
        return 0

    total_days = 0

    if start_year == end_year:
        if start_month == end_month:
            total_days = end_day - start_day
        else:
            total_days += days_in_month(start_month, start_year) - start_day + 1
            for month in range(start_month + 1, end_month):
                total_days += days_in_month(month, start_year)
            total_days += end_day
    else:
        total_days += days_in_month(start_month, start_year) - start_day + 1
        for month in range(start_month + 1, 13):
            total_days += days_in_month(month, start_year)
        
        for year in range(start_year + 1, end_year):
            total_days += 366 if is_leap_year(year) else 365

        for month in range(1, end_month):
            total_days += days_in_month(month, end_year)
        total_days += end_day

    return total_days

def get_valid_date(prompt):
    """Prompt the user for a valid date.
    
    Parameters:
        prompt (str): The prompt message.
    
    Returns:
        tuple: The date as (year, month, day).
    """
    while True:
        try:
            year = int(input(f"{prompt} year: "))
            assert year >= 1753, "Year must be 1753 or later"
            month = int(input(f"{prompt} month: "))
            assert 1 <= month <= 12, "Month must be between 1 and 12"
            day = int(input(f"{prompt} day: "))
            assert 1 <= day <= days_in_month(month, year), f"Day must be between 1 and {days_in_month(month, year)}"
            return (year, month, day)
        except (ValueError, AssertionError) as e:
            print(f"Invalid input: {e}. Please try again.")

def main():
    print("Enter the start date:")
    start_date = get_valid_date("Start")
    print("Enter the end date:")
    end_date = get_valid_date("End")
    
    days = days_between_dates(start_date, end_date)
    if isinstance(days, str):
        print(days)
    else:
        print(f"There are {days} days between {start_date} and {end_date}")

if __name__ == "__main__":
    main()
