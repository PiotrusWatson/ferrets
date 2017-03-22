$(document).ready(function(){
	var curWidth=$('#zoom').css('width');
	var curHeight=$('#zoom').css('height');
	var biganim=false;
	var smallanim=false;
	
	$('#zoom').hover(function(event){
		if (biganim) return false;
		console.log("HI");
		var scale = 150/100;
		biganim=true;
		$('#zoom').animate({width: this.width*scale,
			height: this.height*scale},
			"slow",
			"swing", 
			function(){ biganim=false;});
			
}, 
	function(event){
		if (smallanim) return false;
	var scale = 150/100;
	smallanim=true;
	console.log(curWidth);
	console.log(curHeight);
	$('#zoom').animate({width: curWidth,
			height: curHeight},
			"slow",
			"swing",
			function(){ smallanim=false; });
			
	});
});