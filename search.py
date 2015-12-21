def search(search_input, colleges):
	i = 0
	try:
		while i <= colleges:
			if colleges[i]['name'] == str(search_input):
				return colleges[i]
			
				#raise Exception('This college does not exist in the database') 
			else:
				i += 1
	except:
		raise Exception('This college does not exist in the database')


		

