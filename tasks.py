from datetime import datetime
from invoke import task
import timeframe


@task(optional=['start_date', 'end_date', 'total_hours', 'hours_per_day', 'progress_target', 'colour'])
def calculate(ctx, start_date=None, end_date=None, total_hours=None, hours_per_day=None, progress_target=None,
              colour=None):
    timeframe_calc = timeframe.TimeCalculator()

    def set_attribute_if_not_none(attribute, value):
        if value is not None:
            setattr(timeframe_calc, attribute, value)

    set_attribute_if_not_none('starting_date', datetime.strptime(start_date,
                                                                 "%d-%m-%Y") if start_date is not None else timeframe_calc.get_user_input_starting_date())
    set_attribute_if_not_none('ending_date', datetime.strptime(end_date,
                                                               "%d-%m-%Y") if end_date is not None else timeframe_calc.get_user_input_end_date())

    if total_hours is not None:
        total_hours = int(total_hours)
        timeframe_calc.required_hours = timeframe_calc.hours_left = total_hours
    else:
        timeframe_calc.get_user_input_hours()

    set_attribute_if_not_none('hours_per_day',
                              int(hours_per_day) if hours_per_day is not None else timeframe_calc.get_user_input_hours_per_day())
    set_attribute_if_not_none('progress_target', progress_target)
    set_attribute_if_not_none('colour', colour.upper())

    timeframe_calc.display_progress()
