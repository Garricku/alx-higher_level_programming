$(document).ready(function () {
  const updateHeaderElement = $('#update_header');
  updateHeaderElement.click(function () {
    const headerElement = $('header');
    headerElement.text('New Header!!!');
  });
});
