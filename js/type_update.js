var types = document.querySelector('type');
var subjects = document.querySelector('subject');


subjects.onchange = function() {
  var verse = types.value;
  var request = new XMLHttpRequest();
  var url = document.url;
  request.open('POST', url); // надо как-то передать серверу текущее выбранное значение/значения в списке subjects
  request.responseType = 'json';
  request.onload = function() {
    types. /* надо как-то установить новое содержание списка, причём сервер вернёт набор списков, где 1-ый элемент нужно установить в параметр
    value а 2-ой просто как значение
    */
  };
  request.send();

};
