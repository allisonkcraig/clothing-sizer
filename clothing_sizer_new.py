waist = float(raw_input("Enter Waist Measurement in inches"))
hip = float(raw_input("Enter Hip Measurement in inches"))
bust = float(raw_input("Enter Waist Measurement in inches"))
main = 0

old_navy_tops_num = {'zero': {'chest': 23, 'waist': 34,'letter':'XS'}, 
					 'one': {'chest': 24, 'waist': 35,'letter':'XS'},
					 'two': {'chest': 25, 'waist': 36,'letter':'XS'},
					 'four': {'chest': 26, 'waist': 37,'letter':'S'},
					 'six': {'chest': 27, 'waist': 38,'letter':'S'},
					 'eight': {'chest': 28, 'waist': 39,'letter':'M'},
					 'ten': {'chest': 29, 'waist': 40,'letter':'M'},
					 'twelve': {'chest': 30.5, 'waist': 41.5,'letter':'L'},
					 'fourteen': {'chest': 32.5, 'waist': 43.5,'letter':'L'},
					 'sixteen': {'chest': 34.5, 'waist': 45.5,'letter':'XL'},
					 'eighteen': {'chest': 37, 'waist': 48,'letter':'XL'},
					 'twenty': {'chest': 39.5, 'waist': 50.5,'letter':'XXL'},

def determine_greater_measurement():
	if bust > waist:
		pass
	else:
		pass

print old_navy_tops_num['zero']['chest']