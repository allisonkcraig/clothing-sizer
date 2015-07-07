brands = {
	'Old Navy Tops': {
			'zero': {'chest': 34, 'waist': 23,'letter':'XS','num_size':0}, 
			'one': {'chest': 35, 'waist': 24,'letter':'XS','num_size':1},
			'two': {'chest': 36, 'waist': 25,'letter':'XS','num_size':2},
			'four': {'chest': 37, 'waist': 26,'letter':'S','num_size':4},
			'six': {'chest': 38, 'waist': 27,'letter':'S','num_size':6},
			'eight': {'chest': 39, 'waist': 28,'letter':'M','num_size':8},
			'ten': {'chest': 40, 'waist': 29,'letter':'M','num_size':10},
			'twelve': {'chest': 41.5, 'waist': 30.5,'letter':'L','num_size':12},
			'fourteen': {'chest': 43.5, 'waist': 32.5,'letter':'L','num_size':14},
			'sixteen': {'chest': 45.5, 'waist': 34.5,'letter':'XL','num_size':16},
			'eighteen': {'chest': 48, 'waist': 37,'letter':'XL','num_size':18},
			'twenty': {'chest': 50.5, 'waist': 39.5,'letter':'XXL','num_size':20}
			},

	'Mossimo Tops': {
			'zerozero': {'chest': 31.5, 'waist': 25.25,'letter':'XXS','num_size':00},
			'zero': {'chest': 32.5, 'waist': 26,'letter':'XS','num_size':0}, 
			'two': {'chest': 33.5, 'waist': 26.75,'letter':'XS','num_size':2},
			'four': {'chest': 34.5, 'waist':27.5,'letter':'S','num_size':4},
			'six': {'chest': 35.5, 'waist': 28.5,'letter':'S','num_size':6},
			'eight': {'chest': 36.5, 'waist': 29.5,'letter':'M','num_size':8},
			'ten': {'chest': 37.5, 'waist': 30.5,'letter':'M','num_size':10},
			'twelve': {'chest': 39, 'waist': 32,'letter':'L','num_size':12},
			'fourteen': {'chest': 40.5, 'waist': 33.75,'letter':'L','num_size':14},
			'sixteen': {'chest': 42.5, 'waist': 36,'letter':'XL','num_size':16},
			'eighteen': {'chest': 44.5, 'waist': 38.5,'letter':'XL','num_size':18},
			},
}

def determine_brand():
	"""Determines which brand the user would like to check their size in"""
	user_brand_choice = int(raw_input("Enter 1 for Old Navy, 2 for Target - Mossimo: "))
	if user_brand_choice == 1:
		selected_brand = brands['Old Navy Tops']
		return selected_brand
	elif user_brand_choice == 2:
		selected_brand = brands['Mossimo Tops']
		return selected_brand
	else:
		print "Please select either 1 or 2: "
		determine_brand()


def determine_bust_size(brand_size_chart):
	"""Determines which size the user's bust fits better"""
	bust = float(raw_input("Enter Bust Measurement in inches: "))
	for size in brand_size_chart:
		if brand_size_chart[size]['chest'] <= bust and brand_size_chart[size]['chest'] > bust - .25:
			print "Size ", brand_size_chart[size]['letter'], "coresponds to", brand_size_chart[size]['chest'], " in."
			size_per_bust = brand_size_chart[size]['num_size']
			return size_per_bust


def determine_waist_size(brand_size_chart):
	"""Determines which size the user's waist fits better"""
	waist = float(raw_input("Enter Waist Measurement in inches: "))
	for size in brand_size_chart:
		if brand_size_chart[size]['waist'] <= waist and brand_size_chart[size]['waist'] > waist - .25:
			print "Size ", brand_size_chart[size]['letter'], "coresponds to", brand_size_chart[size]['waist'], " in."
			size_per_waist = brand_size_chart[size]['num_size']
			return size_per_waist


user_brand_choice = determine_brand()
size_per_bust = determine_bust_size(user_brand_choice)
size_per_waist = determine_waist_size(user_brand_choice)


def determine_bigger_size():
	if size_per_waist > size_per_bust:
		print "Size", size_per_waist, "would be the better size"
	elif size_per_bust > size_per_waist:
		print "Size", size_per_bust, "would be the better size"
	else:
		print "Go with size ", size_per_waist


determine_bigger_size()
