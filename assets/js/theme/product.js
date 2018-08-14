/*
 Import all product specific js
 */
import $ from 'jquery';
import PageManager from './page-manager';
import Review from './product/reviews';
import collapsibleFactory from './common/collapsible';
import ProductDetails from './common/product-details';
import videoGallery from './product/video-gallery';
import { selectProductOptionByQueryVariable } from './product/auto-select-variation';
import { classifyForm } from './common/form-utils';

export default class Product extends PageManager {
    constructor(context) {
        super(context);
        this.url = window.location.href;
        this.$reviewLink = $('[data-reveal-id="modal-review-form"]');
    }

    before(next) {
        // Listen for foundation modal close events to sanitize URL after review.
        $(document).on('close.fndtn.reveal', () => {
            if (this.url.indexOf('#write_review') !== -1 && typeof window.history.replaceState === 'function') {
                window.history.replaceState(null, document.title, window.location.pathname);
            }
        });

        next();
    }

    loaded(next) {
        let validator;

        // Init collapsible
        collapsibleFactory();

        this.productDetails = new ProductDetails($('.productView'), this.context, window.BCData.product_attributes);

        videoGallery();

        const $reviewForm = classifyForm('.writeReview-form');
        const review = new Review($reviewForm);

        $('body').on('click', '[data-reveal-id="modal-review-form"]', () => {
            validator = review.registerValidation(this.context);
        });

        $reviewForm.on('submit', () => {
            if (validator) {
                validator.performCheck();
                return validator.areAll('valid');
            }

            return false;
        });

        $(".RM_toggle").click(function(){
            //$(".content").hide();
            var txt = $(".RM_content").is(':visible') ? 'Read More' : 'Read Less';
            $(".RM_toggle").text(txt);
            $('.RM_content').toggle('slow');
        });

        var size_tables = $('.size-tables').html();
        $('#tables-content').html(size_tables);

        $('.inchesClick').click(function(){
            $('#tables-content').find('#sizing-inch').css('display' , 'table');
            $('#tables-content').find('#sizing-cm').css('display',   'none');
        });
        $('.cmClick').click(function(){
            $('#tables-content').find('#sizing-inch').css('display' , 'none');
            $('#tables-content').find('#sizing-cm').css('display',  'table');
        });


        selectProductOptionByQueryVariable()



        var acc = document.getElementsByClassName("faq-title");
        var i;

        for (i = 0; i < acc.length; i++) {
            acc[i].addEventListener("click", function() {
                this.classList.toggle("open");
                var panel = this.nextElementSibling;
                if (panel.style.display === "block") {
                    panel.style.display = "none";
                } else {
                    panel.style.display = "block";
                }
            });
        }

        next();
    }

    after(next) {
        this.productReviewHandler();

        next();
    }

    productReviewHandler() {
        if (this.url.indexOf('#write_review') !== -1) {
            this.$reviewLink.trigger('click');
        }
    }
}


