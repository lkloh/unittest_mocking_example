

def fake_sql_stmt(d):
	for key in d.keys():
		print '%s = %r' % (key, d[key])

d = {'name': 'Alice', 'age': 21, 'college': 'Cal'}
fake_sql_stmt(d)


