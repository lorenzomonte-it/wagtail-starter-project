// https://swiperjs.com/
import Swiper, {Navigation, Pagination} from 'swiper';

// Configure Swiper to use modules
Swiper.use([Navigation, Pagination]);

// Single slide
const swiperSingle = new Swiper('.swiper-container--single', {
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
});