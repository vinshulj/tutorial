import datetime
import pytz
# Syntax: class.method()
current_time2=datetime.datetime.today()
current_time = datetime.datetime.now()
print(current_time)
print(current_time2)
print(type(current_time))
print(type(current_time2))
# current_time3 = datetime.now()#error
d=datetime.datetime(2005,12,3,23,30)
print(d)
print(type(d))
day=d.time()
print(day)
timestamp=d.fromtimestamp(19*60*60)
print(timestamp)
timestamp2=datetime.datetime.fromtimestamp(24*60*60)
print(timestamp2)

#date to string
string=d.isoformat()
print(string)
print(type(string))
print(current_time2)
current_time4=current_time2.timestamp()
print(current_time4)
time2=datetime.time()
print(time2)

deltatime=datetime.timedelta(days=12)+current_time2
print(deltatime)

time3=current_time2.strftime("%w week")
print(time3)

string2="21Aug2018"
date=datetime.datetime.strptime(string2,"%d%b%Y")
print(date)


# from datetime import datetime,timezone

cur=datetime.datetime.now(datetime.timezone.utc)
n=cur.astimezone()
print(cur,n,sep='\n')
print(n.tzinfo,cur.tzinfo,sep='\t')
