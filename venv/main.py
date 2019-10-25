import HTMLParser
import database

"""def site_name():              # why this doesn't work with main.py but does work with SiteName.py????
    user_input = input("Enter your site name: ")
    print(user_input)
    return user_input

site_name = site_name()"""
# <DINA> because you can not do circal import : means if main knows HTMLParser , HTMLParser can NOT know main
# best practice - no on knows main , and main knows every on ehe needs.
# if you want to use the site name from main , you should pass it as parameter



def expected_vs_found():
    for key, value in HTMLParser.tag_count.items():
        if key in database.expected_tags.keys():
            print(key + ':  ', database.expected_tags[key], 'expected,' ' found:', value)
        #print(database.expected_tags)
        #print(HTMLParser.tag_count)

if __name__ == '__main__':
    expected_vs_found()







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

