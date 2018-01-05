#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/bin/python
# -*- coding: utf-8 -*-
# <bitbar.title>Fuzzy Clock (Swedish)</bitbar.title>
# <bitbar.author>Dylan Evans</bitbar.author>
# <bitbar.author.github>whonut</bitbar.author.github>
# <bitbar.desc>Display the current system time in a 'fuzzy' manner, rounding to the nearest 5 minutes and using Swedish words.</bitbar.desc>
# <bitbar.version>1.0</bitbar.version>
#
# 1 second refresh rate may be overkill. Wording & formatting of the time may
# also be easily altered below.

from __future__ import absolute_import, division, print_function, unicode_literals
from time import localtime, strftime, struct_time
import locale


def round_to_nearest_five(n):
    '''Round the float n to the nearest 5.'''
    return int(5 * round(n / 5))


def next_hour(hour):
    # modulo before adding one so that 11 => 12 and not 0
    return (hour % 12) + 1


def fuzzy_time(struct_time=localtime()):
    '''Return the current 'fuzzy time' (rounded to the nearest 5 minutes) as a
       string.'''

    # Split it into hours & minutes and rounding the minutes to make the time
    # 'fuzzy'. Use 12-hour clock.
    hour = (struct_time.tm_hour % 12) or 12
    minute = struct_time.tm_min + (struct_time.tm_sec / 60)
    rounded_min = round_to_nearest_five(minute)
    if rounded_min == 60:
        rounded_min = 0
        hour = next_hour(hour)

    num_word = {1: "ett", 2: "två", 3: "tre", 4: "fyra", 5: "fem", 6: "sex",
                7: "sju", 8: "åtta", 9: "nio", 10: "tio", 11: "elva",
                12: "tolv", 20: "tjugo"}

    # Work out what to display and display it.
    if rounded_min == 0:
        return "klockan {hr}".format(hr=num_word[hour])
    elif rounded_min == 15:
        return "kvart över {hr}".format(hr=num_word[hour])
    elif rounded_min == 25:
        return "fem i halv {hr}".format(hr=num_word[next_hour(hour)])
    elif rounded_min < 30:
        return "{min} över {hr}".format(min=num_word[rounded_min],
                                        hr=num_word[hour])
    elif rounded_min == 30:
        return "halv {hr}".format(hr=num_word[next_hour(hour)])
    elif rounded_min == 35:
        return "fem över halv {hr}".format(hr=num_word[next_hour(hour)])
    elif rounded_min == 45:
        return "kvart i {hr}".format(hr=num_word[next_hour(hour)])
    else:
        return "{min} i {hr}".format(min=num_word[60-rounded_min],
                                      hr=num_word[next_hour(hour)])

if __name__ == '__main__':
    locale.setlocale(locale.LC_ALL, str('sv_SE.UTF-8'))
    day_abbrev = strftime('%A').decode('utf-8').rstrip('dag')
    unpadded_date = strftime('%d %b').lstrip('0')
    display_string = '{time}, {day} {date}'.format(time=fuzzy_time(),
                                                   day=day_abbrev,
                                                   date=unpadded_date).lower()
    print(display_string)
    print('---')
    print(strftime('%H:%M'))
