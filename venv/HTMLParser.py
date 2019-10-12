from html.parser import HTMLParser
import urllib.request

global start_tags_list

class MyHTMLParser(HTMLParser):

    start_tags_list = []

    def handle_starttag(self, startTag,attr):
        self.start_tags_list.append(startTag)

parser = MyHTMLParser()
html_page =  urllib.request.urlopen("https://www.gmail.com/")
parser.feed(str(html_page.read()))

if __name__=='__main__':
    print('start tags', parser.start_tags_list)






