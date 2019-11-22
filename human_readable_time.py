# https://www.codewars.com/kata/52685f7382004e774f0001f7
#
# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable
# format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)


def convert(seconds):
    # set our definitions
    seconds_per_minute = 60
    seconds_per_hour = 60 * 60

    # calculate each period

    hours = int(seconds / seconds_per_hour)
    seconds = seconds - (hours * seconds_per_hour)

    minutes = int(seconds / seconds_per_minute)
    seconds = seconds - (minutes * seconds_per_minute)

    # store as a dictionary to convert later
    return {'hours': str(round(hours)) + ' ',
            'minutes': str(round(minutes)) + ' ',
            'seconds': str(round(seconds)) + ' '}


def make_readable(n):
    input_duration = convert(n)
    h = "{:0>2d}".format(int(input_duration['hours']))
    m = "{:0>2d}".format(int(input_duration['minutes']))
    s = "{:0>2d}".format(int(input_duration['seconds']))
    answer = str(h) + ':' + str(m) + ':' + str(s)
    return answer


print(make_readable(359999))
