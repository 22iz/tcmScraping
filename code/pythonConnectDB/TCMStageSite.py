from sqlalchemy import *
from datetime import datetime
import csv



# db = create_engine('postgresql://pjlmqkcqsbpvdc:bLEsehw4DgT2KZIDX2LwcWGRqq@ec2-54-235-245-180.compute-1.amazonaws.com:5432/d93nich4osg1m6') # live site
# db = create_engine('postgresql://postgres@localhost:5432/TCM_Master')
# db = create_engine('postgresql://uanjdzyaobyqwh:WTX-O46zXiLhudxrcNMYzpLq3O@ec2-23-21-161-153.compute-1.amazonaws.com:5432/d5ambc3o8mmh4e') # stage site

db = create_engine('postgresql://postgres:tcm2014@localhost:5432/scrapeData')
metadata = MetaData(db)

# users = Table('map_resources_table', metadata, autoload=True)
users = Table('commodities', metadata, autoload=True)

# read csv and insert into database
with open('f:\\addComm.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print row
		s = users.insert().values(symbol = row[0], default_mean_grade_units = row[1], default_price_units = row[2], created_at = datetime.now(), updated_at = datetime.now(), precious_metal = row[3], concentrate_units = row[4])

# s = users.select(not_(users.c.latitude == 0))
# s = users.select()
		s.execute()
# rs = users.select().execute()
# rows = rs.fetchall()
# print rows
