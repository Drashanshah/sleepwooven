import $ from 'jquery';
import _ from 'lodash';
import { selectBedSize } from '../product/auto-select-variation'


// fitted, flat, pillowcase
// Twin    39" × 75" × 15" 71" × 98"   21" × 27"
// Full    54" × 75" × 15" 86" × 98"   21" × 27"
// Queen   60" × 80" × 15" 92" × 104"  21" × 27"
// King    78" × 80" × 15" 110" × 104" 21" × 37"

// given a custom Length, width, depth, determine what base size should the fitted sheet be cut from (twin, full, queen, king)
function getBaseSize(custLength, custWidth, custDepth) {

	if (!custLength || !custWidth || !custDepth || custLength == 0 || custWidth == 0 || custDepth == 0 ) {
		// if poor sizes got in, return undefined
		return undefined
	}

    const bases = {
        'twin': 'twin',
        'full': 'full',
        'queen': 'queen',
        'king': 'king',
    }

    if (custLength >= 75) {
        // only queen or king can support this

        if (custWidth <= 60) {
            return bases.queen;
        } else {
            return bases.king
        }

    }

    // if length is less that 75, it can still be any base size depending on width
    if (custWidth <= 39) {
        return bases.twin
    }

    if (custWidth <= 54) {
        return bases.full
    }

    if (custWidth <= 60) {
        return bases.queen
    }

    if (custWidth <= 78) {
        return bases.king
    }

    return bases.king

}

function initCustomSizeListener($customSizeOptionsElement) {
	// do not do any thing if product does not support custom sizes
	if ($customSizeOptionsElement.length == 0) return


	// console.log("$('.form-field label')", $('.form-field label:contains("Custom Size")').parent().hide())

	// uncomment below to show all ordered options
	$('.form-field label:contains("Custom Size")').parent().hide()
	$('.form-field label:contains("Bed Size")').parent().hide()


    // find the custom stuff for forms
    $customSizeOptionsElement.on('input', event => {
        const custLength = Number($customSizeOptionsElement.find('[name=cust-length]').val())
        const custWidth = Number($customSizeOptionsElement.find('[name=cust-width]').val())
        const custDepth = Number($customSizeOptionsElement.find('[name=cust-depth]').val())

        
        const baseSize = getBaseSize(custLength, custWidth, custDepth)
        console.log('custLength', custLength, custWidth, custDepth, baseSize)

        // poor baseSize, skip selection, clear textarea
        if (!baseSize) {
        	$('.form-field textarea').val("")
        	return
        }

        selectBedSize(baseSize)

	    $('.form-field textarea').val(`${custLength}" x ${custWidth}" x ${custDepth}" \nlength x width x depth`);
    });


}


export {
	getBaseSize, initCustomSizeListener
}