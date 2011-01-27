/* Author: Dheeraj Sayala

*/

$('.hint1').hover(function() {
    $(this).parent().find('.word').toggle();
    $(this).parent().find('.meaning').toggle();
  });

$('.hint2').hover(function() {
    $(this).parent().find('.word').toggle();
    $(this).parent().find('.usage').toggle();
  });
