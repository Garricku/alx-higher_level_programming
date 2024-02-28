$(document).ready(function () {
  const toggleHeaderElement = $('#toggle_header');
  toggleHeaderElement.click(function () {
    const headerElement = $('header');
    headerElement.toggleClass('red green');
  });
});
