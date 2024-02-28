$(document).ready(function () {
  const addItemElement = $('#add_item');
  addItemElement.click(function () {
    const newItem = $('<li>').text('Item');
    $('ul.my_list').append(newItem);
  });
});
