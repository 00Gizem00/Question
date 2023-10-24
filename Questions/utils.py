import re

telpattern = r'^0 \(\d{3}\) \d{3} \d{2} \d{2}$'

def is_phone_number_correct(user_input):
    if re.match(telpattern, user_input):
        return True
    return False