$(document).ready(function(){
	var curWidth=$('#zoom').css('width'); //gets default width of image
	var curHeight=$('#zoom').css('height'); //gets default height of image
	var biganim=false; //safety for making bigger
	var smallanim=false; //safety for making smaller
	
	$('#zoom').hover(function(event){
		//while mouse is over image, make it bigger
		if (biganim) return false; //don't load again if already animating
		var scale = 150/100;
		biganim=true; //we are animating right now!
		$('#zoom').animate({width: this.width*scale,
			height: this.height*scale}, //make image bigger, but real slow
			"slow",
			"swing", 
			function(){ biganim=false;}); //once animation is over, tell boolean we've stopped :)
	
}, 
	function(event){
		//while mouse is off image, make it its default size
		if (smallanim) return false; //don't do this again if already animating
	smallanim=true;
	$('#zoom').animate({width: curWidth, //animates size down to original width/height, but real slow
			height: curHeight},
			"slow",
			"swing",
			function(){ smallanim=false; }); //once animation is over, tell boolean we've stopped 
	});
});