$(document).ready(function(){
    $('.one-post').hover(function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity:'0.1'}, 300);
    }, function(event){
        $(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'},300);
    })
});

$(document).ready(function(){
    $('.image').hover(function(event){
        $(event.currentTarget).animate({width: '338'});},
    function(event){$(event.currentTarget).animate({width: "318px"});
    })
});
