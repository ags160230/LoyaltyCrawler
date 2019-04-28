// https://godjango.com/18-basic-ajax/

$(document).ready(function() {
	// AJAX GET
	$('#ajax-get-more').click(function(){
		console.log('get called');
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

	// AJAX POST
	$('#ajax-add-todo').click(function(){
		console.log('add called');
		console.log( 'Todo box is: ' + $(".todo-item").val());

        $.ajax({
            type: "POST",
			// note how the url differs, there is a trailing slash
            url: "ajax/add/",
            dataType: "json",
            data: { "item": $(".todo-item").val() },
            success: function(data) {
				$('ul').append('<li>'+data.message+'</li>');
                alert(data.message);
            }
        });
		
	});




	$.ajaxSetup({ 
		 beforeSend: function(xhr, settings) {
			 function getCookie(name) {
				 var cookieValue = null;
				 if (document.cookie && document.cookie != '') {
					 var cookies = document.cookie.split(';');
					 for (var i = 0; i < cookies.length; i++) {
						 var cookie = jQuery.trim(cookies[i]);
						 // Does this cookie string begin with the name we want?
						 if (cookie.substring(0, name.length + 1) == (name + '=')) {
							 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
							 break;
						 }
					 }
				 }
				 return cookieValue;
			 }
			 if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
				 // Only send the token to relative URLs i.e. locally.
				 xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
			 }
		 } 
	}); 
});