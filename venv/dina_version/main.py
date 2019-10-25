import sys
from web.SiteLoader import SiteLoader
from web.HtmlParserImpl import HTMLParserImpl
import db.dataBaseWorker
import sys

def get_site_name():
    site_name = input("Enter your site name: ")
    return site_name

def expected_vs_found(site_name):
    siteTags=get_site_tags(site_name)
    expected_tags=db.dataBaseWorker.get_expected_tags(site_name)
    for key in expected_tags.keys():
        if key in siteTags.keys():
            print(key + ':  ', expected_tags[key], 'expected,' ' found:', siteTags[key])
        else:
            print(key + ':  ', expected_tags[key], 'expected,' ' found:', 0)

def get_site_tags(site_name):
    site_loader=SiteLoader(site_name)
    htmlParser=HTMLParserImpl()
    return htmlParser.get_tag_counter(site_loader.get_plain_html())

def set_path():
    sys.path.insert(0, '/dina_version/web/')
    sys.path.insert(0, '/dina_version/db/')


if __name__ == '__main__':
    set_path()
    site_name=get_site_name()
    expected_vs_found(site_name)







"""connection = pyodbc.connect(
    'Driver={ODBC Driver 13 for SQL Server};'
    'Server=DESKTOP-7FQ889E\SQLEXPRESS;'
    'Database=Automation;'
    'Trusted_Connection=yes;'
    #'uid=sa;pwd=""'
)

def get_expected_tags(site):
    cursor = connection.cursor()
    sql_statement = "select element, validnumber from siteparams where site_name = ? "
    cursor.execute(sql_statement, site)
    #site_tags = cursor.fetchall()
    #return site_tags
    return cursor

site_tags = dict(get_expected_tags(HTMLParser.user_input).fetchall())

# print ('Expected Tags are: ', site_tags)

# print('Site Tags are: ', HTMLParser.tag_count)


for key,value in HTMLParser.tag_count.items():
    if key in site_tags.keys():
        print(key+':  ', site_tags[key], 'expected,' ' found:', value)"""

