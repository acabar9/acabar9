$(document).ready(function() {


	var text = "";

	var first=0;
	var second=0;
	var result=0;


	$mul = function(a,b){
		return a*b
	}




		$("#readybtn").click(function() {
		$("#ready").toggle(0);


		});

		$("#notreadybtn").click(function() {
		$("#notready").toggle(0);


		});

		$("#submit").click(function() {
		text = $("#textarea").val().trim();
			
			if(text=="ready"){	
				$("#ready").toggle(0);
			}


		});

		$("#multiplex").click(function() {
			first = $("#first").val();
			second = $("#second").val(); 
			result = $mul(first,second);

			$("#result").val(result);
			


		});


});