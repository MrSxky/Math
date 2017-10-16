def date_fashion(you, date):
    if (you>2 or date>2) and (you<8 or date<8):
        return 1
    elif (you ==10 or date ==10 ) and (you>2 and date>2):
        return 2
    else:
        return 0