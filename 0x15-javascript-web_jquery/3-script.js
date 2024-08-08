/* global $ */
$(document).ready(function () {
  $('#red_header').click(function () {
    $('this').data('clicked', true);
    if ($('this').data('clicked')) {
      $('header').addClass('red');
    }
  });
});
