from html.parser import HTMLParser
from urllib import parse


class LinkLookup(HTMLParser, homepage, current_page_url):

    def __init__(self):
        return super().__init__()
        self.homepage = homepage
        self.currentpage = current_page_url
        self.links = set()

    #method override
    def handle_starttag(self, tag, attrs):
        if tag=='a':
            for (attribute, value) in attrs: #extract a tuple of att/value from a tag
                if attribute == 'href':
                    formatted_url = parse.urljoin(self.homepage, value)#if full url: do nothing. else combine with the homepage to make it full
                    self.links.add(formatted_url)
    #links getter
    def get_links(self):
        return self.links


finder = LinkLookup()
finder.feed('<html><head><title>Test</title></head><body><h1>Parse Me!</h1></body></html>')