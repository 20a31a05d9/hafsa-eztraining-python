import time
def countdown(t):

    while t:
        mins,secs = divmod(t,60)      #divmod gives quotient and remainder
        timer = '{:02d} : {:02d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t=-1
    print('finished')

t= input("enter time in seconds:")
countdown(int(t))