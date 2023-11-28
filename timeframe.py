from datetime import datetime, timedelta
from tqdm import tqdm


class TimeCalculator:
    def __init__(self):
        self.starting_date = None
        self.ending_date = None
        self.required_hours = None
        self.hours_left = None

    def get_user_input_dates(self):
        start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
        end_date_str = input("Enter the ending date (YYYY-MM-DD): ")
        self.starting_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        self.ending_date = datetime.strptime(end_date_str, "%Y-%m-%d")

    def get_user_input_hours(self):
        self.required_hours = int(input("Enter the required hours: "))
        self.hours_left = self.required_hours

    def is_weekday(self, date: datetime) -> bool:
        return date.weekday() < 5  # 0-4 corresponds to Monday to Friday

    def calculate_time_left(self) -> int:
        current_date = self.starting_date
        total_hours = 0
        while current_date <= self.ending_date:
            if current_date >= datetime.today():
                break
            if self.is_weekday(current_date):
                total_hours += min(8, self.hours_left)
                self.hours_left -= min(8, self.hours_left)
            current_date += timedelta(days=1)
        return total_hours

    def display_progress(self):
        total_hours = self.calculate_time_left()
        with tqdm(total=self.required_hours, desc='Progress') as pbar:
            for _ in range(total_hours):
                pbar.update()
