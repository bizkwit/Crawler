import threading 
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME =  "Test"#input("What is the name of your project: ")
HOMEPAGE = "http://titan.dcs.bbk.ac.uk/~kikpef01/testpage.html" #input("Please enter the website you want to run your spider on: ")
DOMAIN = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME+'/to_visit.txt'
VISITED_FILE = PROJECT_NAME + '/visited.txt'
NUMBER_OF_THREAD = 8

thread_queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN)


