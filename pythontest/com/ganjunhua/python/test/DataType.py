import  re
import  threading
a = re.compile(r"[A-Z]")
print(a.findall("I hove Holiday"))


def  a(b):
    print(b)

threading.Thread(target=a("a")).start()
threading.Thread(target=a("b")).start()
threading.Thread(target=a("c"))
threading.Thread(target=a("d")).start()