# -*- coding: utf-8 -*-
# store all bedding size info here 




viewOtherSizesHTML = {
	'chi':'<p><a href="https://rebrand.ly/sleepwooven-other-sizes" target="_blank"><u>查看其他尺寸</u></a><br></p>',
	'eng':'<p><a href="https://rebrand.ly/sleepwooven-other-sizes" target="_blank"><u>View Other Sizes</u></a><br></p>'
}

dimensionNote = {
	'chi': '''其他尺寸 (闊x長x深)''',
	'eng': '''Other sizes available. Dimensions are in width &times; length &times; depth</p>'''
}




INDIV = {
	'eng': 'Individually packed',
	'chi': '單件獨立包裝',
	'soap100': {
		'g': '''100 g'''
	},
	'soap110': {
		'g': '''110 g'''
	},
	
}

STANDARD = {
	'eng': 'Standard',
	'chi': '標準',
	'pillowcase': {
		'cm': '''55&nbsp;&times;&nbsp;80 cm'''
	},
	
}


TWIN = {
	'eng': 'Twin/Single',
	'chi': '單人',
	'fittedSheet': {
		'cm': '''105&nbsp;&times; 210&nbsp;&times; 35 cm'''
	},
	'duvetCover': {
		'cm': '''160&nbsp;&times; 235 cm'''
	},
	'flatSheet': {
		'cm': '''195&nbsp;&times;&nbsp;285 cm'''
	},
	'pillowcase': {
		'cm': '''55&nbsp;&times;&nbsp;80 cm'''
	},

}

FULL = {
	'eng': 'Full/Double',
	'chi': '雙人',
	'fittedSheet': {
		'cm': '''125&nbsp;&times;&nbsp;210&nbsp;&times;&nbsp;35 cm'''
	},
	'duvetCover': {
		'cm': '''180&nbsp;&times;&nbsp;235 cm'''
	},
	'flatSheet': {
		'cm': '''220 &times;&nbsp;285 cm'''
	},
	'pillowcase': {
		'cm': '''55&nbsp;&times;&nbsp;80 cm'''
	},

}

QUEEN = {
	'eng': 'Queen',
	'chi': '加大雙人 (帝后)',
	'fittedSheet': {
		'cm': '''160 &times;&nbsp;210&nbsp;&times;&nbsp;35 cm'''
	},
	'duvetCover': {
		'cm': '''210 &times;&nbsp;235 cm'''
	},
	'flatSheet': {
		'cm': '''240 &times;&nbsp;285 cm'''
	},
	'pillowcase': {
		'cm': '''55&nbsp;&times;&nbsp;80 cm'''
	},

}

KING = {
	'eng': 'King',
	'chi': '特大雙人 (帝王)',
	'fittedSheet': {
		'cm': '''190 &times;&nbsp;210&nbsp;&times;&nbsp;35 cm'''
	},
	'duvetCover': {
		'cm': '''242 &times;&nbsp;235 cm'''
	},
	'flatSheet': {
		'cm': '''280 &times;&nbsp;285 cm'''
	},
	'pillowcase': {
		'cm': '''55&nbsp;&times; 95 cm'''
	},

}

# SOAPBAR = {
# 	'eng': 'single bar',
# 	'chi': '梘',
# 	'soap80': {
# 		'cm': '''80g'''
# 	},
# 	'soap100': {
# 		'cm': '''100g'''
# 	}
	
# }

from productCollection.bedding import *


def getSubProductSize(subProduct, size, dimension='cm'):
	# return measurements of subproduct
	# ie. getSubProductSize(duvetCover, KING) returns king duvet cover sizes
	lookupStr = subProduct.get('lookup')

	# print 'subProduct:', subProduct 
	# print 'size:', size
	# print 'lookupStr:', lookupStr
	# print 'size.get(lookupStr)', size.get(lookupStr)

	availableDimensions = size.get(lookupStr).values()

	# if only 1 dimemsion is specified, then just return that one
	#  i.e. 100g, 10 cm... etc
	if len(availableDimensions) == 1:
		defaultDimension = availableDimensions[0]
		return defaultDimension


	return size.get(lookupStr).get(dimension)

# print getSubProductSize(duvetCover, KING)
