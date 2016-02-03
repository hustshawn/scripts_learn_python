### Loop a object dict
- Loop the object field
```
e = Energy.objects.first()
for key, value in e._fields.items():
    print(key, value)
```
- Loop an object field and value
```
e = Energy.objects.first()
for key in e:
	print(key, e[key])
```

Query set.

- Django ORM support "values('<field_name>'...)" and "values_list('<field_name>'...)", while mongodb only supports the last one.
- Normally, the values() returns a list of dictionary, and it can be iterated. Each item is a dict. eg. item['key']; \ while the queryset itself returns a list of objects, so the object can only be refered as 'obj.attr'

` System.objects.values('id')` 
or
` System.object.filter(id__gte=100).values_list('id', 'name')`

while 
` Energy.objects.filter(system_id__gte=100).values_list('system_id')`


