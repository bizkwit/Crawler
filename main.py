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


def crawl():
    '''
    checks for links in to_visit file and crawls them
    '''
    queued_links = convert_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)), " links in the queue")
        create_jobs()

def create_jobs():
    '''
    each queued link is a job
    '''
    for link in convert_to_set(QUEUE_FILE):
        thread_queue.put(link)
    thread_queue.join()
    crawl()


def create_workers():
    '''
    create worker threads (will die when main exits)
    '''
    for _ in range(NUMBER_OF_THREAD):
        thread = threading.Thread(target = work)
        thread.daemon = True
        thread.start()


def work():
    '''
    Do the next job in the queue
    '''
    while True:
        url = thread_queue.get()
        Spider.crawl(threading.current_thread().name, url)
        thread_queue.task_done()






'''TEST'''
create_workers()
crawl()