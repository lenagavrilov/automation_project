from db.DB_ODBC_Connection import DB_ODBC_Connection
from db.DB_Postgres_Connection import DB_Postgres_Connection


def site_in_database(site_name):
    records=[]
    try:
        database_connection = DB_Postgres_Connection()
        cursor = database_connection.get_connection().cursor()
        sql_statement = "select element, validnumber from siteparams where site_name = (%s)"
        cursor.execute(sql_statement, [site_name])
        records = cursor.fetchall()
    except Exception as error:
        print ('ERROR')
        print (error)
    finally:
       # database_connection.close()
        cursor.close()
    return records


def get_expected_tags(site_name):
    expected_tags = dict(site_in_database(site_name))
    if expected_tags == {}:
        print ('The site is not in database.')
        exit(0)
    else:
        return expected_tags
