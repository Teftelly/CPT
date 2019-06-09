var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++){
 foldBtns[i].addEventListener("click", function(e) {
     if (e.target.value == 'Развернуть'){
         event.target.parentElement.parentElement.getElementsByClassName("folded-inner-post")[0].className = "inner-post";
         e.target.value = 'Свернуть'; 
         }
         else {
             event.target.parentElement.parentElement.getElementsByClassName("inner-post")[0].className = "folded-inner-post";
             e.target.value = 'Развернуть';
             }
         });

}
