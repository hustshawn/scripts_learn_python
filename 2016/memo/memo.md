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