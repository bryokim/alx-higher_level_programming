/* global $ */

$.ajax({
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: function (result) {
    for (const movie of result.results) { $('UL#list_movies').append('<li>' + movie.title + '</li>'); }
  }
});
