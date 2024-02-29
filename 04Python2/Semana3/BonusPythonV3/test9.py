import threading
import time

def evenNumbers(n, results):
    time.sleep(1)
    if n % 2 == 0:
        results[n] = True
    else:
        results[n] = False

results = {}
threadPool = [threading.Thread(target=evenNumbers, args=(n, results)) for n in range(0, 27)]
[t.start() for t in threadPool]
[t.join() for t in threadPool]
