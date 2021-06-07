def starbar(num):
    print('*'*num)
def hashbar(num):
    print('#'*num)
def simplebar(num):
    print('%'*num)
    

import bars
print(bars.hashbar(10))


>>> import os
>>> os.getuid()
1000
>>> os.getpid()
3599
>>> os.getppid()
2385
>>> os.uname()
posix.uname_result(sysname='Linux', nodename='abirami-Lenovo-B490', release='5.8.0-53-generic', version='#60~20.04.1-Ubuntu SMP Thu May 6 09:52:46 UTC 2021', machine='x86_64')
>>> os.getcwd()
'/home/abirami/Desktop'
>>> os.chdir('/tmp')
>>> os.getcwd()
'/tmp'



