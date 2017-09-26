def time_word(time):
    """Convert time to text."""

    times = {'00': '', '01': 'one', '02': 'two', '03': 'three', '04': 'four', '05': 'five', '06': 'six',
             '07': 'seven', '08': 'eight', '09': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve',
             '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen',
             '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'fourty', '50': 'fifty'}

    time = time.split(':')
    hours = time[0]
    minutes = time[1]
    ending = ""
    final = []

    if hours == "00" and minutes == "00":
        return "midnight"

    if hours == "12:00" and minutes == "00":
        return "noon"

    if int(time[0]) < 12:
        ending = "am"

    if int(time[0]) >= 12:
        ending = "pm"

    if int(hours) > 20:
        result = times[hours[0] + "0"]
        result = result + times["0" + hours[1]]
        final.append(result)

    if int(hours) <= 20:
        result = times[hours]
        final.append(result)

    if int(minutes) > 20:
        result = times[minutes[0] + "0"]
        final.append(result)

        if "0" + minutes[1] != "00":
            result = times["0" + minutes[1]]
            final.append(result)

    if int(minutes) < 10:
        if minutes == "00":
            result = "o'clock"
            final.append(result)

        else:
            result = "oh " + times[minutes]
            final.append(result)

    elif int(minutes) <= 20:
        result = times[minutes]
        final.append(result)

    final.append(ending)
    return " ".join(final)

assert time_word("01:00") == "one o'clock am"

assert time_word("06:01") == 'six oh one am'

assert time_word("06:10") == 'six ten am'

assert time_word("06:18") == 'six eighteen am'

assert time_word("06:30") == 'six thirty am'

assert time_word("10:34") == 'ten thirty four am'
