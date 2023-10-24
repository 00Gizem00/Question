const element = document.querySelector('#myPhone');
const maskOptions = {
  mask: '(500) 000 00 00',
  lazy: false
  
};
const mask = IMask(element, maskOptions);

function isCurrentStepValid() {
  
}

$('.formNext').click(function() {

  $('.formContent .active : required')

  $(this).parent().removeClass('active').next().addClass('active');
  $('.formSteps .active').removeClass('active').next().addClass('active');
});

$('.formPrev').click(function() {
  $(this).parent().removeClass('active').prev().addClass('active');
  $('.formSteps .active').removeClass('active').prev().addClass('active');
})