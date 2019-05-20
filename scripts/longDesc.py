# -*- coding: utf-8 -*-
# append stuff from sht desc and include common long desc
from shortDesc import *
# import beddingDescChi as bdc
# import beddingDescEng as bde
import commonDesc as cd


def getBreak(**k):
	# give it a break, return HTML break in string
	return '<p><br></p>'

def getLongDesc(inputSKU, lang):
	# get long description

	prodCode, size, color = getParts(inputSKU)

	# print prodCode, size, color

	# get product details
	prodDetail = prodDetails.get(prodCode).get(lang)
	prodContainsArr = prodDetail.get('prodContains')

	r = ''


	# product collection is the parent category of the product.
	# i.e. 'bedding', 'soap'... etc
	prodCollection = prodDetails.get(prodCode).get('collection')



	for snippetFunc in collectionDescRecipe.get(prodCollection).get(lang):
		r += snippetFunc(
				prodCode = prodCode,
				size = size, 
				color = color, 
				prodDetail = prodDetail, 
				lang = lang
			)

	return r

	# start with Short Desc
	shtDesc = getShtDesc(inputSKU, lang)
	r += shtDesc

	# give it a break
	r += '<p><br></p>'
	# append with long desc

	if lang == 'chi':
		r += cd.bedding.get('chi').get('longDesc')
		return r

	# eng desc needs size table
	r += tb.getTableByLangColArr(lang, columnArr = [i[1] for i in prodContainsArr ])
	r += cd.bedding.get('eng').get('longDesc')


	return r

from collectionDescRecipe import *

