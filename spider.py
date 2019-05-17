from urllib.request import urlopen
from lookup import LinkLookup
from general import *


class Spider:

    # Class variables (shared among all instances)
    project = ''
    homepage = ''
    domain_name = ''
    open_list_file = ''
    closed_list_file = ''
    open_list_set = set()
    closed_list_set = set()

    def __init__(self, project, homepage, domain_name):
        Spider.project = project
        Spider.homepage = homepage
        Spider.domain_name = domain_name
        Spider.open_list_file = Spider.project + 'to visit.txt'
        Spider.closed_list_file = Spider.project + 'visited.txt'
        self.boot()
        self.crawl('Initial spider', Spider.homepage) #happen once to initial the crawl

    @staticmethod
    def boot():
        '''
        Initiates the project and creates all the necessary files and folders for the spiders
        '''
        create_project_dir(Spider.project)
        create_data_file(Spider.project, Spider.homepage)
        Spider.open_list_set = convert_to_set(Spider.open_list_file)
        Spider.closed_list_set = convert_to_set(Spider.closed_list_file)

    @staticmethod
    def crawl(name, page_url):
        '''
        Main fn of the spider. collects al the links from a page and stored in the designated places.
        Moves the page to the visited list when done.
        '''
        if page_url not in Spider.open_list_set:
            print(name + " working on: "+ page_url)
            print('In queue :'+ str(len(Spider.open_list_set)) + ' | Visited: '+ str(len(Spider.close_list_set)))
            Spider.add_links_to_list(Spider.get_links(page_url))
            Spider.open_list_set.remove(page_url)
            Spider.closed_list_set.add(page_url)
            Spider.update_files()

    @staticmethod
    def get_links(page_url):
        '''
        connects to a website, convert to a proper html string and pass it to Linklookup
         - returns: set of all the links of that webpage
        '''
        html_string = ''
        try:
            response = urlopen(page_url) #make connection
            if response.getheader('content-type')== 'text/html':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8') #convert bytes to string
            finder = LinkLookup(Spider.homepage, page_url)
            finder.feed(html_string)
        except:
            print("Error: cannot crawl page")
            return set()
        return finder.get_links()

    @staticmethod
    def add_links_to_list(links):
        for link in links:
            if link in Spider.open_list_set or link in Spider.closed_list_set:
                continue
            if Spider.domain_name not in link:
                continue
            Spider.open_list_set.add(link)

    @staticmethod
    def update_files():
        convert_to_file(Spider.open_list_set, Spider.open_list_file)
        convert_to_file(Spider.closed_list_set, Spider.closed_list_file)
        