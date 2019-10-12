import pyodbc

connection = pyodbc.connect(
    'Driver={ODBC Driver 13 for SQL Server};'
    'Server=DESKTOP-7FQ889E\SQLEXPRESS;'
    'Database=Automation;'
    'Trusted_Connection=yes;'
)






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

"""for row in cursor:
    print(row)"""

#for driver in pyodbc.drivers():
#    print(driver)