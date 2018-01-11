var intro = null;
var h_btn = '<a class="btn pull-right"><span class="glyphicon glyphicon-question-sign glyphicon-align-right" aria-hidden="true" span></span></a>';
function set_tips(steps){
  for (var i = 0; i < steps.length; i++) {
      var step = steps[i];
      var btn = $(h_btn)
        .data('i', i)
        .click( function(){
          var i = $(this).data("i") + 1;
          intro.goToStep(i).start() });
      $(step.element).append(btn);
    };
}
(function($) {
  intro = introJs();
    intro.setOptions({steps: steps});
  var l = $(h_btn).click( function(){ intro.start(); })
    l.insertAfter( ".navbar-brand" );
    set_tips(steps);
})(jQuery);
