/* glocal $ */

$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });

  q$('DIV#remove_item').click(function () {
    $('UL.my_list.last').children('li').last().remove();
  });

  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
