waist = float(raw_input("Enter Waist Measurement in inches"))
bust = float(raw_input("Enter Bust Measurement in inches"))


old_navy_tops_num = {
		'zero': {'chest': 23, 'waist': 34,'letter':'XS','num_size':0}, 
		'one': {'chest': 24, 'waist': 35,'letter':'XS','num_size':1},
		'two': {'chest': 25, 'waist': 36,'letter':'XS','num_size':2},
		'four': {'chest': 26, 'waist': 37,'letter':'S','num_size':4},
		'six': {'chest': 27, 'waist': 38,'letter':'S','num_size':6},
		'eight': {'chest': 28, 'waist': 39,'letter':'M','num_size':8},
		'ten': {'chest': 29, 'waist': 40,'letter':'M','num_size':10},
		'twelve': {'chest': 30.5, 'waist': 41.5,'letter':'L','num_size':12},
		'fourteen': {'chest': 32.5, 'waist': 43.5,'letter':'L','num_size':14},
		'sixteen': {'chest': 34.5, 'waist': 45.5,'letter':'XL','num_size':16},
		'eighteen': {'chest': 37, 'waist': 48,'letter':'XL','num_size':18},
		'twenty': {'chest': 39.5, 'waist': 50.5,'letter':'XXL','num_size':20}
		}

def determine_bust_size():
	for size in old_navy_tops_num:
		if old_navy_tops_num[size]['chest'] <= bust and old_navy_tops_num[size]['chest'] > bust - 1:
			print old_navy_tops_num[size]['letter'], "coresponds to", old_navy_tops_num[size]['chest']
			size_per_bust = old_navy_tops_num[size]['num_size']
			print size_per_bust
			return size_per_bust



def determine_waist_size():
	for size in old_navy_tops_num:
		if old_navy_tops_num[size]['waist'] <= waist and old_navy_tops_num[size]['waist'] > waist - 1:
			print old_navy_tops_num[size]['letter'], "coresponds to", old_navy_tops_num[size]['waist'] 
			size_per_waist = old_navy_tops_num[size]['num_size']
			print size_per_waist
			return size_per_waist


size_per_bust = determine_bust_size()
size_per_waist = determine_waist_size()


def determine_bigger_size():
	if size_per_waist > size_per_bust:
		print size_per_waist, "would be the better size"
	elif size_per_bust > size_per_waist:
		print size_per_bust, "would be the better size"
	else:
		print "Go with either size"
		print size_per_waist
		print size_per_bust


determine_bigger_size()
