$(document).ready(function () {
  const myList = $('ul.my_list');
  $('#add_item').click(function () {
    const newItem = $('<li>').text('Item');
    myList.append(newItem);
  });
  $('#remove_item').click(function () {
    myList.children().last().remove();
  });
  $('#clear_list').click(function () {
    myList.empty();
  });
});
