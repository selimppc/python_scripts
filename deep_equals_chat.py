"""
deep equals
"""

object_1 = {
  "name": "John",
  "age": 30,
  "address": {
    "city": "New York",
    "state": "NY",
    "zip": "10001"
  }
}

object_2 = {
  "name": "John",
  "age": 30,
  "address": {
    "city": "Boston",
    "state": "MA",
    "zip": "02108"
  }
}


def deep_equals(obj1, obj2):

    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1.keys():
            if not deep_equals(obj1[key], obj2[key]):
                return False
        return True
    elif isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not deep_equals(obj1[i], obj2[i]):
                return False
        return True
    else:
        return obj1 == obj2


result = deep_equals(object_1, object_2)
print(result) # prints False
