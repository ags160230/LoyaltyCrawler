// AJAX GET
$('#ajax-get-more').click(function(){
	console.log('am i called');
		$.ajax({
		type: "GET",
		url: "ajax/more",
		success: function(data) {
		for(i = 0; i < data.length; i++){
			$('ul').append('<li>'+data[i]+'</li>');
		}
	}
	});
});
