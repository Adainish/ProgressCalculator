from invoke import task

import timeframe


@task
def calculate(ct):
    timeframe_calc = timeframe.TimeCalculator()
    timeframe_calc.get_user_input_dates()
    timeframe_calc.get_user_input_hours()
    timeframe_calc.display_progress()

