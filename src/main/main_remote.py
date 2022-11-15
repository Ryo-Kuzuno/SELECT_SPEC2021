import sys
sys.path.append('../')
from time import sleep
from mission import Resilience

distance = 100 # in meter  
reduce_rate = 0.05
spec = {"radius": 0.3, "height": 2} # in meter
sensor = {"bme" : False, "sht" : False, "counter" : True}

res = Resilience(distance, reduce_rate, spec, sensor)
print("Actuate signal waiting...")

while True: 
    try: 
        actuate_flag = res.twilite_remote.read_actuate()
        
        if actuate_flag==0:
            print("Ascending sequence starts in 10s.")
            for i in range(10):
                print("%d",i+1)
                sleep()
            print("Run!")
            res.run()
            
    except KeyboardInterrupt: 
        print("Aborting the sequence")
        res.twilite_remote.destroy()
        sys.exit()

