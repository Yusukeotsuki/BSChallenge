$('[has-ripple="true"]').click(function () {
  $(this).toggleClass('clicked');
  $('.menu').toggleClass('open');
});

$('.menu a').each(function (index) {
  var thismenuItem        = $(this);
  
  thismenuItem.click(function (event) {
    event.preventDefault();
    
    $('.menuitem-wrapper').eq(index).addClass('spin');
    
    var timer = setTimeout(function () {
      $('body').removeAttr('class').addClass('bg-'+index);
      $('.menuitem-wrapper').eq(index).removeClass('spin');
      $('.menu').removeClass('open');
      $('.menu-btn').removeClass('clicked');
    }, 800);
  });
});