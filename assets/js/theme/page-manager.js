import async from 'async';
import $ from 'jquery';
import 'owl.carousel';
import 'jquery-lazy';

export default class PageManager {
    constructor(context) {
        this.context = context;
    }

    before(next) {
        next();
    }

    loaded(next) {

        console.info('jquery ready load owlCarousel')
        $('.owl-carousel').owlCarousel({
            lazyLoad:true,
            loop: false,
            margin: 10,
            nav: true,
            responsive: {
                0: {
                    items: 1
                }
            }
        });

        // lazyload imgs your configuration goes here

        $(function() {
            $('.lazy').Lazy({
                // your configuration goes here
                scrollDirection: 'vertical',
                effect: 'fadeIn',
                visibleOnly: true,
                effectTime: 1000,
                onError: function(element) {
                    console.log('error loading ' + element.data('src'));
                }
            });
        });



        $('.search-box').on('click', function(){
            $('#quickSearch').toggle('slow');
        })

        next();
    }

    after(next) {
        next();
    }

    type() {
        return this.constructor.name;
    }

    load() {
        async.series([
            this.before.bind(this), // Executed first after constructor()
            this.loaded.bind(this), // Main module logic
            this.after.bind(this), // Clean up method that can be overridden for cleanup.
        ], (err) => {
            if (err) {
                throw new Error(err);
            }
        });
    }
}
