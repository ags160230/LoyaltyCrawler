
// ** NOTES TO DEVELOPERS, AJAX 'Post' REQUESTS DEPEND ON THE CSRF TOKEN
// ** DO NOT REMOVE THE $.ajaxSetup AS IT RETRIVES THE TOKEN REQUIRED
	
// https://godjango.com/18-basic-ajax/
$(document).ready(function() {
	
	// AJAX POST filetree
	$('#ajax-filetree-post').click(function(){
		
		// print to browswer console as santiy check that this method is called
		console.log('ajax-filetree-post called');
		// print the item retrived from the page
		console.log( 'Root is: ' + $(".html-file-tree-root-text-box").val());

		$.ajax({
			type: "POST",
			// note how the url differs, there is a trailing slash
			url: "ajax/filetree/post/",
			dataType: "json",
			data: { "ajax-file-tree-root": $(".html-file-tree-root-text-box").val() },
			success: function(data) {
				// access tree_data from the data returned
				console.log(data.tree_data);
				//var source = builddata(data.tree_data);
				//console.log(source);
				$('#ajax-nested-jqtree').tree({
					// this is the data manipulated from filetree_post method in ajax.py
					data: data.tree_data,
					dragAndDrop: true
				});
			}
		});
		
	});
	
	// ** KEEP THIS CODE since Post methods rely on the token
	
    // CSRF code
    function getCookie(name) {
        var cookieValue = null;
        var i = 0;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (i; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    }); 

});