from typing import Any, Dict, List, Set, Tuple

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


def deep_equals(obj1: Any, obj2: Any) -> bool:
    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, Dict):
        if set(obj1.keys()) != set(obj2.keys()):
            return False
        for key in obj1.keys():
            if not deep_equals(obj1[key], obj2[key]):
                return False
        return True
    elif isinstance(obj1, (List, Tuple, Set)):
        if len(obj1) != len(obj2):
            return False
        for elem1, elem2 in zip(obj1, obj2):
            if not deep_equals(elem1, elem2):
                return False
        return True
    else:
        return obj1 == obj2


result = deep_equals(object_1, object_2)
print(result) # prints False