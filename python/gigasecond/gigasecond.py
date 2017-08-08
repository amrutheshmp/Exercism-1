def add_gigasecond(t):
    import datetime
    import time
    return(datetime.datetime.fromtimestamp(time.mktime(t.timetuple()) + 1000000000))
    pass
