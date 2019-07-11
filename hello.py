from os import rename
import math
import sys
import requests


# print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Helo,{}".format(who_to_greet)
    return greeting


r = requests.get("https://google.com")
print(r.status_code)
