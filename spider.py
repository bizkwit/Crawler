from urllib.request import urlopen
from lookup import LinkLookup
from general import *


class Spider:

    # Class variables (shared among all instances)
    project_name = ''
    homepage = ''
    domain_name = ''
    open_list_file = ''
    closed_list_file = ''
    open_list_set = set()
    closed_list_set = set()

    def __init__(self, project_name, homepage, domain_name):
        Spider.project_name = project_name
        Spider.homepage = homepage
        Spider.domain_name = domain_name
        Spider.open_list_file = Spider.project_name + 'to visit.txt'
        Spider.closed_list_file = Spider.project_name + 'visited.txt'
        self.boot()
        self.crawl('Initial spider', Spider.homepage) #happen once to initial the crawl

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_file(Spider.project_name, Spider.homepage)
        Spider.open_list_set = convert_to_set(Spider.open_list_file)
        Spider.closed_list_set = convert_to_set(Spider.closed_list_file)

    
        