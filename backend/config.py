import os

# Establish MySQL connection
user='root'
password='root'
# password = ''
host='localhost'
<<<<<<< Updated upstream
port = 3306
# ===== MAC USER ====
# port = 8889
=======
port = 8889
>>>>>>> Stashed changes
db='SBRP_Ais_Kachang'
db_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"


