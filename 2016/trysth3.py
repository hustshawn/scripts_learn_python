from datetime import datetime, timezone, timedelta

now = datetime.now()

dt = datetime(2015,4,19,12,30)
print(dt)

# Convert the datetime to timestamp
dt_stamp = dt.timestamp()

# Convert from the timestam to datetime
datetime.fromtimestamp(dt_stamp)
# Or can be directly conevrt to UTC timestamp
datetime.utcfromtimestamp(dt_stamp)

# Convert the datetime to str
print(now.strftime('%a, %b %d %H:%M'))
# Convert the str to datetime
cday = datetime.strptime('2015-12-29 18:23:49', '%Y-%m-%d %H:%M:%S')
print(cday)

print(now + timedelta(hours=10))


utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(type(utc_dt), utc_dt)

# The date in Beijing and HK is with 8hours deltatime
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)



def to_timestamp(dt_str, tz_str):

	dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	# dt_utc = dt - timedelta(hours=hours)
	zone, deltatime = tz_str.split('+')
	hours, mins = deltatime.split(':')
	if not hours or hours == '00':
		hours = 0

	if not mins or mins == '00':
		mins = 0

	hours = int(hours)
	mins = int(mins)
	print(hours)
	dt_utc = dt - timedelta(hours=hours) - timedelta(minutes=mins)
	print(dt_utc)
	dt_utc = dt_utc.replace(tzinfo=timezone.utc)
	# dt_utc = dt.astimezone(timezone(timedelta(hours=hours)))

	return dt_utc.timestamp()

print(" Func execute")
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC+09:00')
print(t2)
