$(document).ready(function() {	
	// 문서의 로딩이 끝나면, 이라는 뜻입니다. 잊지 않으셨죠?
    // 이곳에 코드를 작성하시면 됩니다.
    	$("#shadow").mouseenter(function(){
		$(this).fadeOut(2)
    	});

	$("#button_up").click(function(){
		$("#car").animate({"marginTop":"-=25px"},'2');
	});
	$("#button_down").click(function(){
		$("#car").animate({"marginTop":"-=-25px"},'2');
	});
	$("#button_left").click(function(){
		$("#car").animate({"marginLeft":"-=25px"},'2');
	});

	$("#button_right").click(function(){
		$("#car").animate({"marginLeft":"-=-25px"},'2');
	});


    
    $(document).keydown(function(key) {
        switch(parseInt(key.which,10)) {
			// 왼쪽 방향키
			case 37:
				$("#car").animate({"marginLeft":"-=250px"},'2');
				break;
			// 위쪽 방향키
			case 38:
				$("#car").animate({"marginTop":"-=250px"},'2');
				break;
			// 오른쪽 방향키
			case 39:
				$("#car").animate({"marginLeft":"-=-250px"},'2');
				break;
			// 아래 방향키
			case 40:
				$("#car").animate({"marginTop":"-=-250px"},'2');
				break;
		}
	});
	
});