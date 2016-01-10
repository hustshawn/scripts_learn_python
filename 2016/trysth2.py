# def get_filter_manager(*args, **kwargs):
#     class FilterManager(models.Manager):
#         "Custom manager filters standard query set with given args."
#         def get_query_set(self):
#             return super(FilterManager, self).get_query_set().filter(*args, **kwargs)
#     return FilterManager()

# class Article(models.Model):
    
#     objects = get_filter_manager(deleted=False, author__deleted=False)
#     deleted_articles = get_filter_manager(deleted=True)





# def get_filter_manager(*args, **kwargs):
#     class FilterManager(models.Manager):
#         "Custom manager filters standard query set with given args."
#         def get_query_set(self):
#             return super(FilterManager, self).get_query_set().filter(*args, **kwargs)
#     return FilterManager()

from datetime import datetime, timedelta
def datetimeIterator(from_date, to_date):
	while to_date is None or from_date <= to_date:
		yield from_date
		from_date = from_date + timedelta(days=1)
"""

def get_weekday(from_date, to_date):

	weekday = [ day for day in datetimeIterator(from_date, to_date) if day.isoweekday() in range(1,6)]
	return weekday

def get_weekend(from_date, to_date):

	weekend = [ day for day in datetimeIterator(from_date, to_date) if not day.isoweekday()]
	return weekend
"""
def get_weekday_weekend(from_date, to_date):
	dateiterator = datetimeIterator(from_date, to_date)
	weekday = []
	weekend = []
	for day in dateiterator:
		if day.isoweekday() in range(1,6):
			weekday.append(day)
		else:
			weekend.append(day)
	return {'weekday_list': weekday,
			'weekend_list': weekend
	}


from_date = datetime.strptime('2015-12-31','%Y-%m-%d')
to_date = datetime.strptime('2016-01-03', '%Y-%m-%d')

# print get_weekend(from_date, to_date )
# print get_weekday(from_date, to_date)
print from_date
print to_date
print get_weekday_weekend(from_date, to_date)