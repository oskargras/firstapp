$(document).ready(function() {


$( function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection(); 
});

$(function(){
    $(".flip").flip({
        trigger: 'click',
        axis: 'x'
    });
});

$('.flip').on('click', function() {
console.log('bangla');
});


});
