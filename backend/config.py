import os

# Establish MySQL connection
user='root'
password='root'
# password = ''
host='localhost'
port = 8889
# port = 3306 
db='SBRP_Ais_Kachang'
db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"


