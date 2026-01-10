import os
import time

os.system('cls')

while True:
    for _ in range(1, 11):
        print('*' * _)
    
        time.sleep(0.1)
    
    os.system('cls')
    
    for _ in range(11, -1, -1):
        print('*' * _)
        
        time.sleep(0.1)
    
    os.system('cls')
    
    for _ in range(10, -1, -1):
        print(' ' * _ + '*' * (11-_))
        
        time.sleep(0.1)
    
    os.system('cls')