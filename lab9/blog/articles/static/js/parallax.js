$(document).ready(function () {
    var yPosition;
    var scrolled = 0;
    var $parallaxElements = $('.right-block-for-icons img');
    $(window).scroll(function () {
        scrolled = $(window).scrollTop();
        for (var i = 0; i < $parallaxElements.length; i++) {
            yPosition = (scrolled * 0.15 * (i + 1));
            $parallaxElements.eq(i).css({ top: yPosition });
        }
    });

    var yPosition1;
    var scrolled1 = 0;
    var $parallaxElements1 = $('.image');
    $(window).scroll(function () {
        scrolled1 = $(window).scrollTop();
            yPosition1 = (scrolled1 * 0.32);
            $parallaxElements1.css({ top: yPosition1 });
    }); 
    });