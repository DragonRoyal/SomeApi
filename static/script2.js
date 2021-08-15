
var Cursor = function(jqArray) {
  var idx = 0;
  this.prev = function() {
    idx = (idx > 0 ? idx : jqArray.length) - 1;
    return jqArray.eq(idx);
  };
  this.current = function() {
    return jqArray.eq(idx);
  };
  this.next = function() {
    idx = (idx + 1);
    if (idx >= jqArray.length) {
      return null;
    }
    return jqArray.eq(idx);
  };
  this.first = function() {
    return jqArray.eq(0);
  };
};

// Utility function
// Credit to: https://jonsuh.com/blog/detect-the-end-of-css-animations-and-transitions-with-javascript/
function whichAnimationEvent(){
  var t,
      el = document.createElement("fakeelement");

  var animations = {
    "animation"      : "animationend",
    "OAnimation"     : "oAnimationEnd",
    "MozAnimation"   : "animationend",
    "WebkitAnimation": "webkitAnimationEnd"
  }

  for (t in animations){
    if (el.style[t] !== undefined){
      return animations[t];
    }
  }
}

const animationEvent = whichAnimationEvent();

$(document).ready(function(){
	const $text = $('.intro-text');
  const audio = $('#audio')[0];
  const textCursor = new Cursor($text);
  
  
  $("#play").click(function(){
    audio.play();
  });
  
  $("#stop").click(function(){
    audio.pause();
    audio.currentTime = 0;
  });
  
  $(".planet").click(function(){
    audio.play();
    $(this).addClass("fade_planet");
    $(this).one(animationEvent,
                  function(event) {
      $(this).removeClass("planet");
      setTimeout(function(){
         animateIntro(textCursor.current());
        
      }, 5000)
    })
  });
  
    function animateIntro(current) {
      if (current === null) {
        
        audio.pause();
        audio.currentTime = 0;
        return;
      }
      current.addClass('animate-intro');
      current.one(animationEvent,
                  function(event) {
       
        animateIntro(textCursor.next());
      });
  }
   
});