# https://www.codewars.com/kata/52742f58faf5485cae000b9a
#
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of
# seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is
# expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# format_duration(62)    # returns "1 minute and 2 seconds"
# format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"


def convert(seconds):
    # set our definitions
    seconds_per_minute = 60
    seconds_per_hour = 60 * 60
    seconds_per_day = 60 * 60 * 24
    seconds_per_year = 60 * 60 * 24 * 365

    # calculate each period
    years = int(seconds / seconds_per_year)
    seconds = seconds - (years * seconds_per_year)

    days = int(seconds / seconds_per_day)
    seconds = seconds - (days * seconds_per_day)

    hours = int(seconds / seconds_per_hour)
    seconds = seconds - (hours * seconds_per_hour)

    minutes = int(seconds / seconds_per_minute)
    seconds = seconds - (minutes * seconds_per_minute)

    # store as a dictionary to convert later
    return {'years': str(round(years)) + ' ',
            'days': str(round(days)) + ' ',
            'hours': str(round(hours)) + ' ',
            'minutes': str(round(minutes)) + ' ',
            'seconds': str(round(seconds)) + ' '}


def format_duration(input_integer: int):
    # edge case for zero duration
    if input_integer == 0:
        return 'now'
    # run the calculation
    input_duration = convert(input_integer)
    answer = []
    # remove entries from the dictionary where the value is zero
    squashed = {x: y for x, y in input_duration.items() if y != '0 '}
    # start generating our answer sentence
    for x, y in squashed.items():
        answer.append(y)
        answer.append(x)
    # if there are more than 2 entries we need an and
    if len(answer) > 2:
        answer.insert(len(answer)-2, ' and ')
    # if there are more than 6 entries, we need some commas, in the right places
    if len(answer) > 6:
        for x in range(int((len(answer)-4)/2)):
            answer.insert((x * 3)+2, ', ')
    # if the value is 1 then remove the terminal 's' from the subsequent word
    for x in range(len(answer)):
        if answer[x] == '1 ':
            answer[x+1] = answer[x+1][:-1]
    # return the answer as a string
    return ''.join(answer)


print(format_duration(15731080))
