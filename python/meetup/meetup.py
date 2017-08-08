def meetup_day(year,month,week,condition):

    import datetime
    import calendar
    weekday = {
        'Monday' : 0 ,'Tuesday' : 1,
        'Wednesday' : 2, 'Thursday' : 3 ,
        'Friday' : 4 ,'Saturday' : 5 ,
        'Sunday' : 6
    }
    week_no = weekday[week]
    for i in range(1,calendar.monthrange(year,month)[1]):
        if datetime.date.weekday(datetime.date(year,month,i)) == week_no :
            date = datetime.date(year,month,i)
            break
    if condition == 'first' or condition == '1st' :
        return date
    elif condition == '2nd' :
        return datetime.date(year,month,i+7)
    elif condition == '3rd' :
        return datetime.date(year,month,i+14)
    elif condition == '4th' :
        return datetime.date(year,month,i+21)
    elif condition == '5th':
        return datetime.date(year,month,i+28)
    elif condition == 'teenth' :
        for i in range(13,calendar.monthrange(year,month)[1]):
            if datetime.date.weekday(datetime.date(year,month,i)) == week_no :
                return datetime.date(year,month,i)
    elif condition =='last' :
           for i in range(calendar.monthrange(year,month)[1],1,-1):
            if datetime.date.weekday(datetime.date(year,month,i)) == week_no :
                return datetime.date(year,month,i)
    return date
