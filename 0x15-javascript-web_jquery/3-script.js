$(document).ready(function () {
  const redHeaderElement = $('#red_header');
  redHeaderElement.click(function () {
    const headerElement = $('header');
    headerElement.addClass('red');
  });
});
