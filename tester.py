from codepulse import Tracker 
import numpy as np 
import time 

def check(x,y):

    x = x **3 

    for l in range(2):
        x += 3
        c = time.time()
        print("ccccccccccc", c)
        #c = np.random.randint(c)
        print("c", c)
        np.random.seed(int(c))
        c = np.random.randint(c)
        if c%2==0:
            c = 32
            for k in range(10000):
                y = y + 4  
                y = y + 4 
                y = y + 4
                if k %1000 == 0:
                    return 4 
        print("Damn")
        x = 4 
        if True:
            c = 32
            for k in range(10000):
                y = y + 4  
                y = y + 4 
                y = y + 4 
        x = 9
        for k in range(10000):
            x = 3
            print("done"*x)
    y = x*  y 

    x = 10
    for x in range(10):
        if x %2 !=0:
            z = 2
            for m in range(10000):
                z = z * 10
        else:
            for c in range(100000):
                v= 2
                v = v * 20 + 10 
                v += 12
    x  = x + y 
    y = y + 4  
    y = y + 4 
    for k in range(10000):
        y = y + 4  
        y = y + 4 
        y = y + 4 
    y = y + 4 
    x = 39 * x

    return x + y 


from codepulse import Tracker

def fun1(x,y):
    m = 1
    for i in range(x*100):
        m = m * 3 
        for j in range(x*30):
            m = m + 4 
    return m 

t = Tracker(check, {"np": np})
t(3,5)