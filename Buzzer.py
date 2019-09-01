import time, datetime, json

#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)

# Import bells from bells.json
with open('bells.json', 'r') as f:
    bells = json.loads(f.read())

# Switches the relay on for 'seconds'
def ring(seconds):
    #GPIO.output(18,GPIO.HIGH)
    print("High")
    time.sleep(seconds)
    #GPIO.output(18,GPIO.LOW)
    print("Low")

# Return the number of seconds since 00:00
def get_seconds():
    seconds = (
        (datetime.datetime.now().hour*3600)+
        (datetime.datetime.now().minute*60)+
        (datetime.datetime.now().second)
        )
    return seconds

# Returns weekday as an integer. (Mon == 0 - Sun == 6)
def get_day():
    day = datetime.date.today().weekday()
    return day

ring(0.1)

while True:
    for bell in bells:
        if bell[0] == get_seconds() and bell[2][get_day()] == True:
            ring(bell[1])
    time.sleep(0.5)