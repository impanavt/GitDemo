import time
def greet():
    current_time = time.localtime()
    hour = current_time.tm_hour
    if 5<=hour<=12:
      print("Good morning")
    elif 12<=hour<=17:
        print("Good Afternoon")
    elif 17<=hour<=20:
        print("Good Evening")
    else:
        print("Good Night")
greet()