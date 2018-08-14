import async from 'async';
import $ from 'jquery';
import 'owl.carousel';

export default class PageManager {
    constructor(context) {
        this.context = context;
    }

    before(next) {
        next();
    }

    loaded(next) {

        console.log('load owlCarousel')
        $('.owl-carousel').owlCarousel({
            loop: false,
            margin: 10,
            nav: true,
            responsive: {
                0: {
                    items: 1
                }
            }
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
