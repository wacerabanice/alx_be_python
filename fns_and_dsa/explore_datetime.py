from datetime import datetime, timedelta

def display_current_datetime():
    # Save current date and time inside current_date
    current_date = datetime.now()
    # Print formatted output: YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Save future date inside future_date
    future_date = datetime.now() + timedelta(days=days)
    # Print formatted output: YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)

if __name__ == "__main__":
    main()
