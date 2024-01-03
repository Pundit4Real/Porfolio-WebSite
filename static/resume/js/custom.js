// templatemo 467 easy profile

// PRELOADER

$(window).load(function(){
    $('.preloader').delay(1000).fadeOut("slow"); // set duration in brackets    
});

$(function(){
    jQuery(document).ready(function() {
		$('body').backstretch([
	 		 "{% static 'resume/images/tm-bg-slide-1.jpg' %}", 
	 		 "{% static 'resume/images/tm-bg-slide-2.jpg' %}",
			 "{% static 'resume/images/tm-bg-slide-3.jpg' %}",
		], {duration: 3200, fade: 1300});
	});
})
