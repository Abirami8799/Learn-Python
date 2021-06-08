
python3 -m venv virt1
source virt1/bin/activate
deactivate
abirami@abirami-Lenovo-B490:~$ source virt1/bin/activate
(virt1) abirami@abirami-Lenovo-B490:~$ python
Python 3.8.5 (default, May 27 2021, 13:30:53) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/lib/python38.zip', '/usr/lib/python3.8', '/usr/lib/python3.8/lib-dynload', '/home/abirami/virt1/lib/python3.8/site-packages']
>>> 
(virt1) abirami@abirami-Lenovo-B490:~$ pip install redis
(virt1) abirami@abirami-Lenovo-B490:~$ pip show requests
Name: requests
Version: 2.25.1
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache 2.0
Location: /home/abirami/virt1/lib/python3.8/site-packages
Requires: urllib3, idna, chardet, certifi
Required-by:
(virt1) abirami@abirami-Lenovo-B490:~$ pip list
Package           Version  
----------------- ---------
certifi           2021.5.30
chardet           4.0.0    
idna              2.10     
mypy              0.812    
mypy-extensions   0.4.3    
pip               20.0.2   
pkg-resources     0.0.0    
redis             3.5.3    
requests          2.25.1   
setuptools        44.0.0   
typed-ast         1.4.3    
typing-extensions 3.10.0.0 
urllib3           1.26.5   


class Student(object):
  def __init__(self,name:str, batch:int, branch:str,roll:int)->None:
    self.name = name
    self.batch = batch
    self.branch = branch
    self.roll=roll
    self.semester= None
    self.paper()
    
 mypy student.py



import unittest from factorial import fact
class TestFactorial(unittest.TestCase):
    def test_fact(self):
        res= fact(5)
        self.assertEqual(res,120)
        if __name__ == '__main__':
        unittest.main()
        
        
        
        
  import sys
  def fact(n):
    if n==0:
      return 1
    retunrn n*fact(n-1)
   def div(n):
    res=10/n
    return res
  def main(n):
    res=fact(n)
    print(res)
  if __name__=='__main__':
    if len(sys.argv)>1:
      main(int(sys.argv[1]))
