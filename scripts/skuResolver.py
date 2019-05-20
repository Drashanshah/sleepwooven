# -*- coding: utf-8 -*-
# given parts of the SKU, generate the required long and short description... etc

# import beddingDescChi, beddingDescEng
import productDef as pd
import sizeTableBedding as tb
import productCollection.bedding as bedding
import productCollection.soap as soap


# <p>【尺寸】單人</p>
# <p>1X 被袋（闊x長）：160 × 235 cm</p>
# <p>2X 枕頭套&nbsp;（闊x長）：55 × 80 cm<br></p>
# <p><a href="https://rebrand.ly/sleepwooven-other-sizes" target="_blank" style="vertical-align: baseline;font-size: 14.6667px;"><u>查看其他尺寸</u></a><br></p>
# <p>【設計】</p>
# <p>信封式，綿繩開封。無拉鍊/無鈕 （加倍耐用）</p>
# <p>被袋另內置八條棉繩方便固定被子</p>
# <p>【顏色】象牙</p>
# <p>【物料】100% 埃及特長織綿</p>
# <p>【織法】貢鍛</p>
# <p>400針（每1吋,歐美）</p>
# <p>1600 針 (每10cm,亞洲)</p>



sizeLookup = {
	'INDIV': {
		'eng': 'Single Pack',
		'chi': '獨立單件裝',
		'productDef': pd.INDIV,
	},
	'STD': {
		'eng': 'Standard',
		'chi': '標準',
		'productDef': pd.STANDARD,
	},
	'TWI': {
		'eng': 'Twin/Single',
		'chi': '單人',
		'productDef': pd.TWIN,
	},
	'FUL': {
		'eng': 'Full/Double',
		'chi': '雙人',
		'productDef': pd.FULL,
	},
	'QUE': {
		'eng': 'Queen',
		'chi': '加大雙人 (帝后)',
		'productDef': pd.QUEEN,
	},
	'KIN': {
		'eng': 'King',
		'chi': '特大雙人 (帝王)',
		'productDef': pd.KING,
	},
}


colorLookup = {
	'IVO': {
		'eng':'Ivory',
		'chi':'象牙'	,
	},
	'WHI': {
		'eng':'White',
		'chi':'純白'	,
	},
	'WHT': {
		'eng':'White',
		'chi':'純白'	,
	},
	'TAU': {
		'eng':'Taupe',
		'chi':'灰褐'	,
	},

	# for the soaps
	# 'MNPB': {
	# 	'eng': 'Multipurpose Natural Plant Based Soap',
	# 	'chi': '',
	# },
	# 'COFFEE': {
	# 	'eng': 'Coffee Infused Anti-Odor Multipurpose Plant Based Soap',
	# 	'chi': '',
	# },


}



# merge product SKU lookup
prodDetails = {}
prodDetails.update(bedding.prodDetails)
prodDetails.update(soap.prodDetails)




		
otherMeasurmentsLink = {
	'chi': '''<p><a href="https://rebrand.ly/sleepwooven-other-sizes" target="_blank"><u>查看其他用品尺寸</u></a><br></p>''',
	'eng': '''<p><a href="https://rebrand.ly/sleepwooven-other-sizes" target="_blank"><u>Click here to see more sizes</u></a><br></p>''',
}
# sku = "3PCS-TWI-IVO_S"
# arr = sku.split('-')

# prodCode, size, color = arr

# print prodCode


def getParts(inputSKU):
	arr = inputSKU.split('-')

	prodCode, size, color = arr

	# print arr
	# color needs to select only first 3 chars: 'IVO_S' --> 'IVO'
	color = color[0:3]

	return [prodCode, size, color]

def pTag(content):
	# wraps string in paragraph tag
	return '<p>{}</p>'.format(content)








