/* global $ */
$(document).ready(function () {
  $('INPUT#btn_translate').on('click', function () {
    const lang = $('INPUT#language_code').val();
    if (lang) {
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, function (result) {
        $('DIV#hello').text(result.hello);
      });
    }
  });
});
