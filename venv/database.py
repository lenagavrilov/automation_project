import pyodbc
#import main
import SiteName

def connection():

    connection = pyodbc.connect(
        'Driver={ODBC Driver 13 for SQL Server};'
        'Server=DESKTOP-7FQ889E\SQLEXPRESS;'
        'Database=Automation;'
        'Trusted_Connection=yes;'
        #'uid=sa;pwd=""'
    )
    return connection

database_connection = connection()

def get_expected_tags(site):
    cursor = database_connection.cursor()
    sql_statement = "select element, validnumber from siteparams where site_name = ? "
    cursor.execute(sql_statement, site)
    return cursor


def site_in_database():
    expected_tags = dict(get_expected_tags(SiteName.site_name).fetchall())
    if expected_tags == {}:
        print ('The site is not in database.')
        exit(0)
    else:
        return expected_tags

expected_tags = site_in_database()



if __name__ == '__main__':
    #expected_tags = dict(get_expected_tags(main.user_input()).fetchall())
    print('Tags',expected_tags)