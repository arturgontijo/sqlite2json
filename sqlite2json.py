import sqlite3
import json

def dict_factory(cursor,row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

filename = raw_input("Filename(path): ")
table = raw_input("Table: ")

# SQLite
conn = sqlite3.connect(filename)
conn.row_factory = dict_factory
cur = conn.cursor()

# JSON
sql = "SELECT * FROM %s" % (table)
cur.execute(sql)
jsondata = json.dumps(cur.fetchall(), indent=2)
fd = open('%s.json' % table, 'w')
fd.write(jsondata)
fd.close()