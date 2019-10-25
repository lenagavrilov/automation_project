import urllib.request
class SiteLoader:
    site_name = ''

    def __init__(self, site_name):
        self.site_name = site_name

    def full_name(self, site):
        self.full_site_name = 'http://' + site
        return self.full_site_name

    def get_plain_html(self):
        try:
            self.html_page = urllib.request.urlopen(self.full_name(self.site_name)).read()
        except Exception as error:
            print (error)
            print("Site is unreachable")
            exit(-1)
        return self.html_page
