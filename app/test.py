import time

tt = time.strftime('%Y-%m-%d_%H%M%S', time.localtime(time.time()))

print(tt)

print(type(tt))