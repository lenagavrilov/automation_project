from html.parser import HTMLParser
from collections import Counter
class HTMLParserImpl(HTMLParser):
    start_tags_list = []
    def handle_starttag(self, startTag, attr):
        global start_tags_list
        self.start_tags_list.append(startTag)

    def get_start_tag_list(self):
        return start_tag_list

    def get_tag_counter(self,plain_html):
        self.feed(str(plain_html))
        tag_count = dict(Counter(self.start_tags_list))
        return tag_count