seconds_per_minute = 60
seconds_per_hour = 60 * 60
seconds_per_day = 60 * 60 * 24
seconds_per_year = 60 * 60 * 24 * 365


def format_duration(seconds):
    years = seconds / seconds_per_year
    seconds = seconds % seconds_per_year

    days = seconds / seconds_per_day
    seconds = seconds % seconds_per_day

    hours = seconds / seconds_per_hour
    seconds = seconds % seconds_per_hour

    minutes = seconds / seconds_per_minute
    seconds = seconds % seconds_per_minute
    return round(years), round(days), round(hours), round(minutes), round(seconds)


print(format_duration(3662))
