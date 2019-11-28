import threading
import time

def test(a):
    time.sleep(0.001)
    print(a)
ts = []
for i in range(0, 15):
    th = threading.Thread(target=test,args=[i])
    th.start()
    ts.append(th)
for i in ts:
    i.join()
print("hhh")
