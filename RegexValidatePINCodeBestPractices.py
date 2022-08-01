def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()  # if pin = 4 or 6 and pin contains positive digits only return True
                                                 # otherwise, return False
