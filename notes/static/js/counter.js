$(document).ready(function() {
$('label').append('<span id="counter">0</span>/120');
  var counter = $('#counter');
  var textArea = $('body').find('textarea');

  textArea.on('keyup', function(event) {
    var length = textArea.val().length;

    if ((length > 50) && (length < 90)) {
      $(this).css("color", "purple");
    } else if ((length > 90) && (length <= 120)) {
      $(this).css("color", "red");
    } else if (length < 50) {
      $(this).css("color", "green");
    }
    counter.text(length);
  });
});
