import sys
print('python-version =')
print(sys.version)


import django
print('\nDjango version =')
print(django.get_version())


import rest_framework
print('\nDjango REST Framework version =')
print(rest_framework.VERSION)


'''
python-version =
3.7.3 (default, Jul  6 2019, 19:58:31) 
[GCC 5.4.0 20160609]

Django version =
2.2.3

Django REST Framework version =
3.10.1
'''