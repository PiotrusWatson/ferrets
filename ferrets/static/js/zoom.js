$(document).ready(function(){
	$('#zoom').hover(function(){
		console.log("HI");
		var scale = 150/100;
		$(this).css({
			width: this.width*scale,
			height: this.height*scale
		})
}, 
	function(){
	var scale = 150/100;
		$(this).css({
			width: this.width/scale,
			height: this.height/scale
		})
	});
});