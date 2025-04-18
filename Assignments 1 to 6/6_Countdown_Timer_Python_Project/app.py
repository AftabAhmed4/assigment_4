import time

# User se input lena (seconds)
seconds = int(input("Enter the countdown time in seconds: "))

# While loop for countdown
while seconds > 0:
    print(seconds)
    time.sleep(1)  # 1 second ka delay
    seconds -= 1

print("Time's up! ⏰")
