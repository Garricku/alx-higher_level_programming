$(document).ready(function () {
  const languageInput = $('#language_code');
  const translateButton = $('#btn_translate');
  const helloDiv = $('#hello');
  translateButton.click(function () {
    const languageCode = languageInput.val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (data) {
      const helloTranslation = data.hello;
      helloDiv.text(helloTranslation);
    });
  });
});
