import random

print("============")
temp = 1
guess = int(temp)
cnt = 0
guestcnt = random.randint(1, 100)
while guess != guestcnt:
    temp = input("xxxxxxxxxxx")
    print(guestcnt)
    guess = int(temp)
    cnt += 1
    if guess == guestcnt:
        print("right")
    else:
        if guess > guestcnt:
            print("大了")
        else:
            print("小了")
print(10 < 2)
