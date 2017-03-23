$(document).ready(function(){
	$('#zoom').hover(function(){
		console.log("HI");
		var scale = 150/100;
		$(this).animate({width : width * scale}, 20);
		$(this).animate({height: height * scale}, 20);
}, 
	function(){
	var scale = 150/100;
		$(this).animate({"width" : width / scale}, 20);
		$(this).animate({"height": height / scale}, 20);
	});
});