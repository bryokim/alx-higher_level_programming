/* global $ */

$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (result) {
    $('DIV#hello').text(result.hello);
  });
});
