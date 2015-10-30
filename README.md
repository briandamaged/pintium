# Pintium #

Pinterest + Selenium = Pintium

## Installation ##

Actually, this still needs to be converted into a proper Python package.  For now, you can at least obtain the dependencies for this library by doing:

```shell
pip install -r requirements.txt
```

## Usage ##

Here's a sample script:

```python
from pintium import EasyClient


c = EasyClient("USERNAME", "PASSWORD", "TOKEN")

# Conduct a search
pins = c.search_for("dog", "dancing")
for p in pins:
  print(p["note"])
  print(p["created_at"])
  print("-" * 40)


```

The complete list of dictionary keys can be found here:

https://developers.pinterest.com/docs/api/pins/

## TODO ##

* Make the library more robust
