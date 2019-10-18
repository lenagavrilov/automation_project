from html.parser import HTMLParser
import urllib.request
from collections import Counter



class MyHTMLParser(HTMLParser):

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






