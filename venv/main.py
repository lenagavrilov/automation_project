import pyodbc
import HTMLParser
#import random

connection = pyodbc.connect(
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
        print(key+':  ', site_tags[key], 'expected,' ' found:', value)

"""for k in HTMLParser.tag_count:
    cursor = connection.cursor()
    sql = 'insert into siteparams(site_name, element,validnumber) VALUES (?,?,?)'
    values = ('www.ynet.co.il', k, random.randint(0,20))
    cursor.execute(sql,values)
connection.commit()"""

"""cursor = connection.cursor()
cursor.execute('Truncate table Siteparams')
connection.commit()"""

#cursor.execute('Select * from dbo.SiteParams')"""

#for row in cursor:
 #   print(row)   """







#בנתיים לא רוצה למחוק את כל זה
"""data = [['aaaa','param',8],
       ['bbb','sar',4]]

cursor = connection.cursor()
cursor.execute('Select * from dbo.SiteParams')"""

insert_query = """insert into dbo.siteparams(sitename, validnumber) VALUES(?,?);  """

"""for row in data:
    values= (row[0], row[2])
    cursor.execute(insert_query, values)
connection.commit()"""

#cursor.execute("""insert into dbo.siteparams(sitename, element, validnumber)
#                VALUES('aaa','dot',4)""")
#connection.commit()
#cursor.execute('Select * from dbo.SiteParams')

#for driver in pyodbc.drivers():
#    print(driver)