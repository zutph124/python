Note that the date class comes with quite a few methods and “supported operations,” per docs.python.org/3/library/datetime.html#date-objects. 
In particular, the class implements __sub__, per docs.python.org/3/library/operator.html#operator.__sub__, overloading - in such a way that subtracting one date object from another returns a timedelta object, which itself comes with several (read-only) “instance attributes,” per docs.python.org/3/library/datetime.html#timedelta-objects.

Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
  pip install inflect
