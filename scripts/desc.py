# -*- coding: utf-8 -*-
from skuResolver import *
import commonDesc





def getProductSize(**k):
	# returns product size in a string

	# <p>【尺寸】單人</p>
	size = k.get('size')
	lang = k.get('lang')

	header = {
		'eng': 'Size: ',
		'chi': '【尺寸】'
	}

	return '<p>{}{}</p>'.format(
		header.get(lang),
		sizeLookup.get(size).get(lang)
		)

def getPackingFormat(**k):
	# returns 包裝規格	, in a string
	size = k.get('size')
	lang = k.get('lang')

	header = {
		'eng': 'Packing Spec: ',
		'chi': '【包裝規格】'
	}

	return '<p>{}{}</p>'.format(
		header.get(lang),
		sizeLookup.get(size).get(lang)
	)





def getProductDetails(**k):
	# returns product details in a str

	# <p>1X 被袋（闊x長）：160 × 235 cm</p>
	# <p>2X 枕頭套&nbsp;（闊x長）：55 × 80 cm<br></p>
	size = k.get('size')
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')


	r = ''

	# array of procuct details
	prodContainsArr = prodDetail.get('prodContains')
	for subProductDesc, subProductObj  in prodContainsArr:

		# subProductDesc i.e.: 1X 被袋（闊x長）
		# subProductDef i.e. pd.duvetCover
		sizeObj = sizeLookup.get(size).get('productDef')

		sizeStr = pd.getSubProductSize(subProductObj, sizeObj)

		r += '<p>{}{}</p>'.format(subProductDesc, sizeStr)


	return r

def getOtherMeasurements(**k):
	# for bedding products return a link with other measurements

	# 查看其他用品尺寸

	lang = k.get('lang')
	return otherMeasurmentsLink.get(lang)



def getSpecialFeatures(**k):
	# return string that shows the design features 
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')

	header = {
		'eng': '<p><b>Features: </b></p>',
		'chi': '<p>【特點】</p>'
	}
	

	r = header.get(lang)

	# array of product designs
	prodDesignArr = prodDetail.get('design')
	for i in prodDesignArr:
		r += '<p>{}</p>'.format(i)

	return r

def getUsageTips(**k):
	# return string that shows usage tips
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')

	header = {
		'eng': '<p><b>Usage Tips: </b></p>',
		'chi': '<p>【注意事項】</p>',
	}

	r = header.get(lang)

	prodUsageTipsArr = prodDetail.get('usageTips')
	for i in prodUsageTipsArr:
		r += '<p>{}</p>'.format(i)

	return r



def getMainIngredients(**k):
	# return string that shows main ingredients
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')

	header = {
		'eng': '<p><b>Main Ingredients: </b></p>',
		'chi': '<p>【主要成分】</p>',
	}

	r = header.get(lang)

	prodIngredientsArr = prodDetail.get('ingredients')

	
	r += '<p>{}</p>'.format(
		', '.join(prodIngredientsArr)
	)

	return r

def getDesignFeatures(**k):
	# return string that shows the design features 
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')

	header = {
		'eng': '<p><b>Features: </b></p>',
		'chi': '<p>【設計】</p>'
	}
	

	r = header.get(lang)

	# array of product designs
	prodDesignArr = prodDetail.get('design')
	for i in prodDesignArr:
		r += '<p>{}</p>'.format(i)

	return r

def getProdName(**k):
	# return product name as a string
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')

	return prodDetail.get('name')



def getColor(**k):

	lang = k.get('lang')
	color = k.get('color')

	header = {
		'eng': '<b>Color: </b>',
		'chi': '【顏色】',
	}

	r = '<p>{}{}</p>'.format(
		header.get(lang),
		colorLookup.get(color).get(lang)
	)

	return r



def getCommonShtDesc(**k):
	# pad with common description
	prodCollection = k.get('prodCollection')
	lang = k.get('lang')

	return commonDesc.collectionDesc.get(prodCollection).get(lang).get('commonShtDesc')


def getCommonLongDesc(**k):
	prodCollection = k.get('prodCollection')
	lang = k.get('lang')

	return commonDesc.collectionDesc.get(prodCollection).get(lang).get('commonLongDesc')

def getProductTable(**k):
	lang = k.get('lang')
	prodDetail = k.get('prodDetail')
	prodContainsArr = prodDetail.get('prodContains')

	return tb.getTableByLangColArr(lang, columnArr = [i[1] for i in prodContainsArr ])


def getBreak(**k):
	# give it a break, return HTML break in string
	return '<p><br></p>'


def getShtDesc(inputSKU, lang):
	 return getDesc(inputSKU, lang, recipe = collectionShtDescRecipe)

def getLongDesc(inputSKU, lang):
	 return getDesc(inputSKU, lang, recipe = collectionLongDescRecipe)

def getDesc(inputSKU, lang, recipe):
	# given product code i.e: 3PCS
	# return the chinese short desc

	prodCode, size, color = getParts(inputSKU)
	print prodCode, size, color, lang



	# get product details
	prodDetail = prodDetails.get(prodCode).get(lang)

	# print name of tehhe 
	print getProdName(				
			prodDetail = prodDetail, 
			lang = lang
	)

	r = ''

	# product collection is the parent category of the product.
	# i.e. 'bedding', 'soap'... etc
	prodCollection = prodDetails.get(prodCode).get('collection')


	for snippetFunc in recipe.get(prodCollection).get(lang):

		r += snippetFunc(
				prodCollection = prodCollection,
				prodCode = prodCode,
				size = size, 
				color = color, 
				prodDetail = prodDetail, 
				lang = lang
			)

	return r



from collectionDescRecipe import *

# print getShtDesc('3PCS-FUL-IVO_D', 'eng')
# print getShtDesc('3PCS-FUL-IVO_D', 'chi')



# Size: Double
# Style: Envelope with hidden ties (no buttons, no zippers)
# Features: 8 inner cotton strings to help stabilize the duvet
# Width x Length: 180 × 235 cm
# -------
# Color: Ivory
# -------
# Material: 100% Egyptian Long Staple Cotton
# Weave: Sateen, 400 Thread Count (per inch, US & EU), ~1600 Thread Count (per 10 cm, Asia)
# Finishing: Proprietary Mercerization
# Safety/Environmental Certifications: OEKO-Tex 100, ISO 9001-14001


