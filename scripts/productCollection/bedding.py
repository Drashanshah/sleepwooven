# -*- coding: utf-8 -*-

# subproducts, the SKU will contain these items

mattress = {
	'chi': '床褥',
	'eng': 'Mattress',

	# key used to lookup dict values
	'lookup': 'mattress',
}

fittedSheet = {
	'chi': '橡筋床笠',
	'eng': 'Fitted Sheet',
	'lookup': 'fittedSheet',
}

duvetCover = {
	'chi': '被袋',
	'eng': 'Duvet Cover',
	'lookup': 'duvetCover',
}

flatSheet = {
	'chi': '床單',
	'eng': 'Flat Sheet',
	'lookup': 'flatSheet',
}

pillowcase = {
	'chi': '枕頭套',
	'eng': 'Pillowcase',
	'lookup': 'pillowcase',
}


# all product unique descriptions are held here

OXP = {
	'collection': 'bedding',
	'chi': {
		# '雙人【象牙】三件裝：枕頭套+被袋'
		'name': '兩件裝：枕頭套',
		'prodContains': [
			['2X 枕頭套（闊x長）：', pillowcase],
		],
		'design': [
			'- 牛津式枕頭套（優雅 5cm圍邊)',
		],
	},
	'eng': {
		'name': 'Oxford Style Pillowcases 2pcs set',
		'prodContains': [
			['2X Pillowcases（WxL）：', pillowcase],
		],
		'design': [
			'- Oxford style pillowcase with 5cm flange',
		],

	}

}

DC = {
	'collection': 'bedding',
	'chi': {
		# '雙人【象牙】三件裝：枕頭套+被袋'
		'name': '被袋',
		'prodContains': [
			['1X 被袋（闊x長）：', duvetCover],
		],
		'design': [
			'信封式被袋，綿繩開封。無拉鍊/無鈕 （加倍耐用)', 
			'被袋另內置八條棉繩方便固定被子',
		],
	},
	'eng': {

		'name': 'Duvet Cover',
		'prodContains': [
			['1X Duvet Cover（WxL）：', duvetCover],
		],
		'design': [
			'- Durable envelope style with no zippers or buttons',
			'- 8 inner cotton strings to help stabilize the duvet', 
		],


	}

}



# LTB = {
# 	'chi': {
# 		# '雙人【象牙】三件裝：枕頭套+被袋'
# 		'name': '100%真絲優雅毛氈',
# 		'prodContains': [
# 			['1X 毛氈（闊x長）：', loungeBlanket],
# 		],
# 		'design': [
# 			'100%真絲', 
# 		],
# 	},
# 	'eng': {

# 		'name': '100% Silk Lounge Blanket and Scarf',
# 		'prodContains': [
# 			['1X Duvet Cover（WxL）：', loungeBlanket],
# 		],
# 		'design': [
# 			"- Simple elegance speaks to your household's sophistication",
# 		],


# 	}

# }

THREEPCS = {
	'collection': 'bedding',
	'chi': {
		# '雙人【象牙】三件裝：枕頭套+被袋'
		'name': '三件裝：枕頭套+被袋',
		'prodContains': [
			['1X 被袋（闊x長）：', duvetCover],
			['2X 枕頭套（闊x長）：', pillowcase],
		],
		'design': [
			'信封式被袋，綿繩開封。無拉鍊/無鈕 （加倍耐用)', 
			'被袋另內置八條棉繩方便固定被子',
			'牛津式枕頭套（優雅 5cm圍邊)',
		],
	},
	'eng': {
		# Double Ivory 3pcs Duvet Cover & Pillowcases Set
		'name': '3pcs Duvet Cover & Pillowcases Set',
		'prodContains': [
			['1X Duvet Cover（WxL）：', duvetCover],
			['2X Pillowcases（WxL）：', pillowcase],
		],
		'design': [
			'- Durable envelope style with no zippers or buttons',
			'- 8 inner cotton strings to help stabilize the duvet', 
			'- Oxford style pillowcase with 5cm flange',
		],


	}

}


FOURPCS = {
	'collection': 'bedding',
	'chi': {
		# 單人【純白】四件裝：床單套裝
		'name': '四件裝：床笠、床單、2枕頭套',
		'prodContains': [
			# - 1x 橡筋床笠 (105 × 210 × 35 cm)
			# - 1x 床單 (195 × 285 cm)
			# - 2x 枕頭套 (55 × 80 cm)
			['1x 橡筋床笠（闊x長x深）：', fittedSheet],
			['1x 床單（闊x長）：', flatSheet],
			['2X 枕頭套（闊x長）：', pillowcase],
		],
		'design': [
			'- 如酒店一樣，床單用於隔開身體和被子，倍感優雅舒適。', 
			'- 牛津式枕頭套（優雅 5cm圍邊)。',
		],
	},
	'eng': {
		# Double Ivory 3pcs Duvet Cover & Pillowcases Set
		# Twin White 4pcs Bed Sheet Set
		'name': '4pcs Bed Sheet Set: Fitted Sheet, Flat Sheet, 2 Pillowcases',
		# - 1x Fitted Sheet (105 × 210 × 35 cm)
		# - 1x Flat Sheet (195 × 285 cm)
		# - 2x Pillowcases (55 × 80 cm)
		'prodContains': [
			['1X Fitted Sheet（WxLxH）：', fittedSheet],
			['1X Flat Sheet（WxL）：', flatSheet],
			['2X Pillowcases（WxL）：', pillowcase],
		],
		'design': [
			'- Oxford style pillowcase with 5cm flange',
		],


	}

}




FIVEPCS = {
	'collection': 'bedding',
	'chi': {
		# 單人【純白】五件裝：床單套裝+被袋
		'name': '五件裝：床笠、床單、2枕頭套、被袋',
		'prodContains': [
			# - 1x 橡筋床笠 (105 × 210 × 35 cm)
			# - 1x 床單 (195 × 285 cm)
			# - 2x 枕頭套 (55 × 80 cm)
			['1X 被袋（闊x長）：', duvetCover],
			['1x 橡筋床笠（闊x長x深）：', fittedSheet],
			['1x 床單（闊x長）：', flatSheet],
			['2X 枕頭套（闊x長）：', pillowcase],
			
		],
		'design': [
			'- 信封式被袋，綿繩開封。無拉鍊/無鈕 （加倍耐用)', 
			'- 被袋另內置八條棉繩方便固定被子',
			'- 如酒店一樣，床單用於隔開身體和被子，倍感優雅舒適。', 
			'- 牛津式枕頭套（優雅 5cm圍邊)。',
		],
	},
	'eng': {
		'name': '5pcs Bed Sheet Set: Fitted Sheet, Flat Sheet, 2 Pillowcases, Duvet Cover',
		'prodContains': [
			['1X Duvet Cover（WxL）：', duvetCover],
			['1X Fitted Sheet（WxLxH）：', fittedSheet],
			['1X Flat Sheet（WxL）：', flatSheet],
			['2X Pillowcases（WxL）：', pillowcase],
		],
		'design': [
			'- Oxford style pillowcase with 5cm flange',
			'- Durable envelope style with no zippers or buttons',
			'- 8 inner cotton strings to help stabilize the duvet', 
		],


	}

}

FITS = {
	'collection': 'bedding',
	'chi': {
		# 單人【純白】四件裝：床單套裝
		'name': '橡筋床笠：400針、埃及綿、名酒店專用',
		'prodContains': [
			['1x 橡筋床笠（闊x長x深）：', fittedSheet],
		],
		'design': [
			'- 比一般床笠更有深度，適合較深的床褥或加上床墊的用家',
			'- 使用加強橡筋，加培耐用',
		],
	},
	'eng': {
		# Double Ivory 3pcs Duvet Cover & Pillowcases Set
		# Twin White 4pcs Bed Sheet Set
		'name': '400TC Deep Fit Fitted Sheet',
		# - 1x Fitted Sheet (105 × 210 × 35 cm)
		# - 1x Flat Sheet (195 × 285 cm)
		# - 2x Pillowcases (55 × 80 cm)
		'prodContains': [
			['1X Fitted Sheet（WxLxH）：', fittedSheet],
		],
		'design': [
			'- Deep pocket fits thicker mattresses and beds with a mattress topper',
			'- Fortified elastic bands for extra durability',
		],


	}

}


prodDetails = {
	'3PCS': THREEPCS,
	'4PCS': FOURPCS,
	'OXP': OXP,
	'5PCS':FIVEPCS,
	'DC': DC,
	'FITS': FITS,
}