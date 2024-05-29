/* global $ */

/* request a list */
const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data) {
  $.each(data.results, function (index, element) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  });
});
