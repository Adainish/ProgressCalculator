from datetime import datetime, timedelta
import time
from tqdm import tqdm


class TimeCalculator:
    def __init__(self):
        self.starting_date = None
        self.ending_date = None
        self.required_hours = None
        self.hours_left = None
        self.hours_per_day = None
        self.progress_target = 'Progress'
        self.colour = 'WHITE'

    def get_user_input_dates(self):
        start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
        end_date_str = input("Enter the ending date (YYYY-MM-DD): ")
        self.starting_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        self.ending_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    def get_user_input_starting_date(self):
        start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
        self.starting_date = datetime.strptime(start_date_str, "%Y-%m-%d")

    def get_user_input_end_date(self):
        end_date_str = input("Enter the ending date (YYYY-MM-DD): ")
        self.ending_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    def get_user_input_hours(self):
        self.required_hours = int(input("Enter the required hours: "))
        self.hours_left = self.required_hours

    def get_user_input_hours_per_day(self):
        self.hours_per_day = int(input("Enter the hours counted per day: "))

    def date_range(self, start_date, end_date):
        delta = end_date - start_date
        for i in range(delta.days + 1):
            current_date = start_date + timedelta(days=i)
            if current_date.weekday() < 5:  # 0-4 corresponds to Monday to Friday
                yield current_date

    def calculate_time_left(self) -> int:
        total_hours = 0
        for current_date in self.date_range(self.starting_date, self.ending_date):
            if current_date >= datetime.today():
                break
            total_hours += min(self.hours_per_day, self.hours_left)
            self.hours_left -= min(self.hours_per_day, self.hours_left)
        return total_hours

    def display_progress(self):
        total_hours = self.calculate_time_left()
        with tqdm(total=self.required_hours, desc=self.progress_target, colour=self.colour) as pbar:
            for _ in range(total_hours):
                time.sleep(0.001)
                pbar.update()
