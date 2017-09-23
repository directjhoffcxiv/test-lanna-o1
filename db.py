import pyodbc

server = 'digitaleco.database.windows.net'
database ='Digital_ECO'
username = 'anuwatk'
password = 'L@nnacom@1'
#driver= '{ODBC Driver 13 for SQL Server}'
driver = '{SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT [ID],[username],[contact] FROM [dbo].[Alluser]")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
