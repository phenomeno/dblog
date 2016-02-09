$(document).ready(function() {
  $('#mail').removeClass("hidden");
  $('.questions').on('click', function(e) {
    e.preventDefault();
    $('.questions').removeClass("questions-active");
    $(this).addClass("questions-active");
    $('.answers').addClass("hidden");

    var a = e.target.className;
    var b = a.indexOf("octicon-");
    var c = a.substring(b, a.length);
    var d = c.indexOf(" ");
    var q = c.substring(8, d);


    $('#'+q).removeClass("hidden");
  });
});
