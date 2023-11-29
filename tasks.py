from datetime import datetime
from invoke import task

import timeframe


@task(optional=['start_date', 'end_date', 'total_hours', 'hours_per_day', 'progress_target', 'colour'])
def calculate(ctx, start_date=None, end_date=None, total_hours=None, hours_per_day=None, progress_target=None, colour=None):
    timeframe_calc = timeframe.TimeCalculator()
    if start_date is not None:
        timeframe_calc.starting_date = datetime.strptime(start_date, "%d-%m-%Y")
    else:
        timeframe_calc.get_user_input_starting_date()
    if end_date is not None:
        timeframe_calc.ending_date = datetime.strptime(end_date, "%d-%m-%Y")
    else:
        timeframe_calc.get_user_input_end_date()
    if total_hours is not None:
        total_hours = int(total_hours)
        timeframe_calc.required_hours = total_hours
        timeframe_calc.hours_left = total_hours
    else:
        timeframe_calc.get_user_input_hours()
    if hours_per_day is not None:
        timeframe_calc.hours_per_day = int(hours_per_day)
    else:
        timeframe_calc.get_user_input_hours_per_day()
    if progress_target is not None:
        timeframe_calc.progress_target = progress_target
    if colour is not None:
        timeframe_calc.colour = colour.upper()
    timeframe_calc.display_progress()

