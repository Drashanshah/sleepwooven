import $ from 'jquery';
import _ from 'lodash';


function getQueryVariable(parameter) {
    var searchString = window.location.search.substring(1);
    var params = searchString.split('&');
    for (var i = 0; i < params.length; i++) {
        var pair = params[i].split('=');
        if (decodeURIComponent(pair[0]) == parameter) {
            return decodeURIComponent(pair[1]);
        }
    }
}

function selectBedSize(keyword) {
	// select bed size variant on product page based on string: ie. king, Queen, TwIn, ... etc

	var keywordLowerCase = keyword.toLowerCase()

	// restrict selection to bed size only
	var allBedSizesStr = $(".productView-options .form-field[data-product-attribute='set-rectangle'] .form-option-variant ")

	var size = _.find(allBedSizesStr, (v) => {
		return $(v).text().toLowerCase() == keywordLowerCase
	})

	if (size) {
		// console.debug('found size', size)

		// click on button to select variant 
		$(size).parent().click()

	}

}

function selectColor(keyword) {
	// select color variant on product page based on string: ie. white, Ivory, taupe, ... etc

	var keywordLowerCase = keyword.toLowerCase()

	// restrict selection to bed size only
	var allBedColorsStr = $(".productView-options .form-field[data-product-attribute='swatch'] .form-option-swatch ")

	var color = _.find(allBedColorsStr, (v) => {
		return $(v).text().trim().toLowerCase() == keywordLowerCase
	})

	if (color) {
		// console.debug('found color', color)

		// click on button to select variant 
		$(color).click()

	}

}



function selectProductOptionByQueryVariable() {
	// ie. http://localhost:3000/bedsheet-set/?size=king&color=taupE 
	// will auto select king size taupe for the product
    var sizeKeyword = getQueryVariable('size');

    if (sizeKeyword) {
    	selectBedSize(sizeKeyword);
    }

    var colorKeyword = getQueryVariable('color');

    if (colorKeyword) {
    	selectColor(colorKeyword);
    }

    


}

export { selectProductOptionByQueryVariable, selectBedSize }