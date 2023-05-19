#Lucas Ross 5 Dec 2022

from pynput.keyboard import Key, Listener, Controller
from time import sleep

con = Controller()

msg = "FREE YOUNG THUNG FREE GUNNA"
start = "a"
num = 50
sleepy = 0.5
def on_press(key):
    try:
        if key.char == start:
            sleep(sleepy)

            con.tap(Key.delete)

            for i in range(0, num):

                sleep(sleepy)

                for j in msg:
                    con.tap(j)

                sleep(sleepy)

                con.tap(Key.enter)

                sleep(sleepy)
            
            quit()
            
    except AttributeError:
        pass

# collect events
with Listener(on_press=on_press) as listener:
    listener.join()