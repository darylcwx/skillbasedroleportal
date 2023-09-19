import os

# Establish MySQL connection
user='root'
password='password'
host='localhost'
port = 3306
db='SBRP_Ais_Kachang'
db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"


