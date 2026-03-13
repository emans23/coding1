import random
import time
def getRandomDate(startDate,endDate):
    print("start date is",startDate,"end date is",endDate)
    randomgenerator=random.random()
    dateformat="%m/%d/%Y"
    start_time=time.mktime(time.strptime(startDate,dateformat))
    end_time=time.mktime(time.strptime(endDate,dateformat))
    random_time=start_time+randomgenerator*(end_time-start_time)
    random_date=time.strftime(dateformat,time.localtime(random_time))
    return random_date
print("random_date",getRandomDate("1/1/2006","1/2/2026"))
