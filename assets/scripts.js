$(document).ready(function(){
    
    $popover = $(".message-popover");
    if($popover.length) {
        window.setTimeout(function() {
            $popover.fadeOut(1000);
        }, 2000);
    }

    $('#start-screen').click(function(){
        $('.push-notification').addClass("fade-in");
    });
    
});

setInterval(function(){
    get_post()         
},5000);

function get_post(){
    var Url = 'https://ancient-inlet-30790.herokuapp.com/seller'
    $.ajax({
        url: Url,
        type: 'POST',
        dataType: 'json',
        data: {},
    })
    .done(function(data) {
        //here assign the returned data to the html element
    })
    .fail(function() {
        console.log("error");
    });
}