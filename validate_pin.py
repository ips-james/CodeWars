# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits
# or exactly 6 digits.
#
# If the function is passed a valid PIN string, return true, else return false.
import re


def validate_pin(pin):
    # return true or false
    if re.fullmatch('[0-9]{4}|[0-9]{6}', str(pin)):
        return True
    else:
        return False


# print(validate_pin(-123))
print(validate_pin(1234.0))
