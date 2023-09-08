import json
import sys
import logging
import mysql.connector

logger = logging.getLogger()
logger.setLevel(logging.INFO)

user='root'
password='password'
host='localhost'
port = 3306
db='TEST'

try:
    connection = mysql.connector.connect(user=user, password=password, host=host, database=db)
except:
    logger.error("ERROR: Could not connect to MySql instance.")
    sys.exit()
logger.info("SUCCESS: Connection to MySql instance succeeded")
