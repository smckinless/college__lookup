def search(search_input, colleges):
	i = 0
	try:
		while i <= colleges:
		
			if colleges[i]['name'].lower() == search_input.lower():
				return colleges[i]
			
				#raise Exception('This college does not exist in the database') 
			else:
				i += 1
	except:
		return '<p class="title">This college does not yet exist in the database or there is a typo in the query</p>'


		

