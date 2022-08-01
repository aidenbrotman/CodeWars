def format_duration(seconds):
    time_list = []
    if not seconds:
        print('now')
    if seconds >= 31536000 and seconds != '':
        yrs = seconds // 31536000
        seconds = seconds % 31536000
        if yrs == 1:
            yrs = str(yrs) + " year"
            time_list.append(yrs)
        elif yrs > 1:
            yrs = str(yrs) + " years"
            time_list.append(yrs)
    if seconds >= 86400 and seconds < 31536000 and seconds != '':
        days = seconds // 86400
        seconds = seconds % 86400
        if days == 1:
            days = str(days) + " day"
            time_list.append(days)
        elif days > 1:
            days = str(days) + " days"
            time_list.append(days)
    if seconds >= 3600 and seconds < 86400:
        hrs = (seconds // 3600)
        seconds = seconds % 3600
        if hrs == 1:
            hrs = str(hrs) + " hour"
            time_list.append(hrs)
        elif hrs > 1:
            hrs = str(hrs) + " hours"
            time_list.append(hrs)    
    if seconds >= 60 and seconds < 3600:
        mins = (seconds // 60)
        seconds = seconds % 60
        if mins == 1:
            mins = str(mins) + " minute"
            time_list.append(mins)
        elif mins > 1:
            mins = str(mins) + " minutes"
            time_list.append(mins)
    if seconds < 60 and seconds > 0:
        secs = (seconds // 1)
        if secs == 1:
            secs = str(secs) + " second"
            time_list.append(secs)
        elif secs > 1:
            secs = str(secs) + " seconds"
            time_list.append(secs)
    if len(time_list) > 2:
        for i, v in enumerate(time_list[:-2]):
            time_list[i] = v + ','
    if len(time_list) == 2:
        time_list.insert(-1, 'and')
    elif len(time_list) > 2:
        time_list.insert(-1, 'and')
    if not seconds == '':
        print(" ".join(time_list))

format_duration(3742978729479792748932978347928342364927346)
