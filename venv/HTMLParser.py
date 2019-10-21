from html.parser import HTMLParser
import urllib.request
from collections import Counter
#import main
import SiteName


class MyHTMLParser(HTMLParser):

    start_tags_list = []

    def handle_starttag(self, startTag,attr):
        self.start_tags_list.append(startTag)

class Parser(MyHTMLParser):

    def full_name(self, site):
        self.full_site_name = 'http://' + site
        #print (self.full_site_name)
        return self.full_site_name

    def html(self):
        self.html_page =  urllib.request.urlopen (self.full_name(SiteName.site_name))
        #print (self.html_page)
        return self.html_page

parser = Parser()

try:
    parser.feed(str(Parser().html().read()))
except:
    print('Either the site is not reachable or you spelt the name wrong.')
    SiteName.site_name= input('Check your internet connection and enter the site name again: ')
    parser.feed(str(Parser().html().read()))

tag_count = dict(Counter(MyHTMLParser.start_tags_list))

if __name__=='__main__':
    # print('start tags', parser.start_tags_list)
    print('Tag count', tag_count)





"""class MyHTMLParser(HTMLParser):

    start_tags_list = []

    def handle_starttag(self, startTag,attr):
        self.start_tags_list.append(startTag)

parser = MyHTMLParser()
user_input = input('Please enter your site name: ')
full_site_name = 'http://'+user_input
html_page =  urllib.request.urlopen (full_site_name)                         #("https://www.gmail.com/")
parser.feed(str(html_page.read()))

tag_count = dict(Counter(MyHTMLParser.start_tags_list))

if __name__=='__main__':
    print('start tags', parser.start_tags_list)
    print('Tag count', tag_count)"""





