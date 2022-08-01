# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def validate_pin(pin):  # pin taken as a string
    pin_length = len(pin)  # assigns length of pin to pin_length
    if not pin.isdecimal():  # if pin contains values other than digits
        return False
    else:   # if pin contains only digits
        if int(pin) < 0:
            int(pin) * -1  # turns any negative pin into a positive pin
        elif pin_length == 4 or pin_length == 6:
            return True
        else:
            return False
