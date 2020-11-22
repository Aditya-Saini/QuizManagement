// templatemo 467 easy profile

// PRELOADER

$(window).load(function(){
	$('.preloader').delay(2700).fadeOut("slow"); // set duration in brackets
	$("#overlayer").delay(2700).fadeOut("slow"); 
});

// HOME BACKGROUND SLIDESHOW
$(function(){
    jQuery(document).ready(function() {
		$('body').backstretch([
	 		 "/static/QuizManagement/quiz-background.jpg",
	 			]);
		});
})