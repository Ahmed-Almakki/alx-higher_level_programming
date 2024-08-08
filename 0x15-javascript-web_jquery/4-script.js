/* global $ */
$(document).ready(function () {
  $('toggle_header').click(function () {
    if ($('header').css('color') === 'rgb(255, 0, 0)') {
      $('header').css('color', 'green');
    } else {
      $('header').css('color', 'red');
    }
  });
});
