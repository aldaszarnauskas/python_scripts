# returns the list of vehicles due over 50 euros
def list_toll_dodgers(tfile):

    fines = {}

    with open(tfile, 'r') as dodgers:

        dodgers = dodgers.readlines()

        for line in dodgers:
            p, d, t = line.split(' ')  # splits into plate, date, time
            h, m, _ = t.split(':')  # splits into hour, minute, second
            d, _, _ = d.split('/')  # splits into day, month, year
            h, m, d = int(h), int(m), int(d)
            # returns true if the data is not the first day of the month
            if int(d) != 1:

                # returns true of hours are between 7-19
                if h in range(7,19) or (h == 19 and m == 00):
                    if p in fines.keys():
                        fines[p] = fines[p] + 2.5 
                    else:
                        fines[p] = 2.5

                # for hours NOT in 7-19 range
                else:
                    if p in fines.keys():
                        fines[p] = fines[p] + 1.0
                    else:
                        fines[p] = 1.0

    # selects vehicles that are due 50 or more
    over_fifty = []
    for key in fines.keys():
        if fines[key] >= 50:
            over_fifty.append([key, fines[key]])

    # sorts lists based on the amount due in decreasing order
    sorted_over_fifty = sorted(over_fifty, key=lambda t: t[1], reverse = True) 
    return sorted_over_fifty