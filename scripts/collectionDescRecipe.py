from desc import *
# from longDesc import *



# collection from skuResolver controls what appears in the descriptions
collectionShtDescRecipe = {
	'bedding': {
		'eng': [
			getProductSize, 
			getProductDetails, 
			getOtherMeasurements, 
			getDesignFeatures,
			getColor,
			getCommonShtDesc,
		],
		'chi': [
			getProductSize, 
			getProductDetails, 
			getOtherMeasurements, 
			getDesignFeatures,
			getColor,
			getCommonShtDesc,
			getProductTable,
		],
	},
	'soap': {
		'eng': [
			getPackingFormat,
			getProductDetails, 
			getMainIngredients,
			getSpecialFeatures,
			getCommonShtDesc,
			getUsageTips,

		],
		'chi': [
			getPackingFormat,
			getProductDetails, 
			getMainIngredients,
			getSpecialFeatures,
			getCommonShtDesc,
			getUsageTips,

		],
	},
}

collectionLongDescRecipe = {
	'bedding': {
		'eng': [
			getProductSize, 
			getProductDetails, 
			getOtherMeasurements, 
			getDesignFeatures,
			getColor,
			getCommonShtDesc,
			getBreak, 
			getProductTable,
			getCommonLongDesc,
		],
		'chi': [
			getProductSize, 
			getProductDetails, 
			getOtherMeasurements, 
			getDesignFeatures,
			getColor,
			getCommonShtDesc,
			getBreak, 
			getProductTable,
			getCommonLongDesc,
		],
	},
	'soap': {
		'eng': [
			getPackingFormat,
			getProductDetails, 
			getMainIngredients,
			getSpecialFeatures,
			getCommonShtDesc,
			getUsageTips,
			getBreak, 
			getCommonLongDesc,

		],
		'chi': [
			getPackingFormat,
			getProductDetails, 
			getMainIngredients,
			getSpecialFeatures,
			getCommonShtDesc,
			getUsageTips,
			getBreak, 
			getCommonLongDesc,
		],
	},
}







