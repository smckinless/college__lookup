import sqlite3 as sql

def insert_college_holder(name,acceptance_rate,location,sat_score,act_score):
	with sql.connect("colleges.db") as con:
		cur = con.cursor()
		cur.execute("INSERT INTO college_holder(name,acceptance_rate,location,sat_score,act_score) VALUES (?,?,?,?,?)", (name,acceptance_rate,location,sat_score,act_score))
		con.commit()
		con.close()

def select_college_holder(params=()):
	with sql.connect("colleges.db") as con:
		cur = con.cursor()
		if params==():
			cur.execute("SELECT * from colleges_holder")
		else:
			string = "SELECT"
			for i in xrange(len(params)-1):
				string += "%s,"
				string += " from college_holder"

				result = cur.execute(string)
				con.close()
				return result.fetchall()

	return cur.fetchall()