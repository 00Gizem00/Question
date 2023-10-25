const element = document.querySelector('#myPhone');
const maskOptions = {
  mask: '(500) 000 00 00',
  lazy: false
  
};
const mask = IMask(element, maskOptions);


function isCurrentStepValid() {
  const activeElements = document.querySelectorAll('.formContent .active :required');

  for(const element of activeElements) {
    if(!element.checkValidity()) {
      element.reportValidity();

      return false;
    }
  }

  return true;
}

$('.formNext').click(function() {
  if(!isCurrentStepValid()) {return}

  $(this).parent().removeClass('active').next().addClass('active');
  $('.formSteps .active').removeClass('active').next().addClass('active');
});

$('.formPrev').click(function() {
  $(this).parent().removeClass('active').prev().addClass('active');
  $('.formSteps .active').removeClass('active').prev().addClass('active');
});

$('input, select, textarea').change(function() {
  
});

function createFormSteps() {
  $('.formStep').each(function(index, element) {
    $('.formSteps').append(`<li>${element.dataset.step}</li>`)
  });
  
  $('.formSteps li:first, .formStep:first').addClass('active');
}

createFormSteps();
