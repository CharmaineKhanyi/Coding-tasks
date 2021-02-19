from collections import Counter 
def common_chars(str1,str2): 	
	d1 = Counter(str1) 
	d2 = Counter(str2) 
	common_dict = d1 & d2 
	if len(common_dict) == 0: 
		return "No common characters."

	# list of common elements 
	common_chars = list(common_dict.elements()) 
	common_chars = sorted(common_chars) 

	return ', '.join(common_chars) 

str1 = 'house'
str2 = 'computers'
print("Input: "+str1+' , '+str2)
print("Common letters: "+common_chars(str1, str2))

