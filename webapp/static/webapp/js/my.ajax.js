
// ** NOTES TO DEVELOPERS, AJAX 'Post' REQUESTS DEPEND ON THE CSRF TOKEN
// ** DO NOT REMOVE THE $.ajaxSetup AS IT CALLS METHODS TO RETRIEVE THE TOKEN REQUIRED
// ** ALSO DO NOT REMOVE the methods required to retrieve the token

// https://godjango.com/18-basic-ajax/
$(document).ready(function() {
	
	$('#collapse-tree-button').click(function(){
		// print to browswer console as santiy check that this method is called
		console.log('collapse-tree-button clicked');
		
		var root_node = $('#ajax-nested-jqtree').tree('getNodeById', $(".html-file-tree-root-text-box").val());
		$('#ajax-nested-jqtree').tree('closeNode', root_node, false);
	});
	
	// AJAX POST operation
	// this method is called on the expand-tree-button click
	$('#ajax-filetree-post-operation-expand-tree-button').click(function(){
		
		// print to browswer console as santiy check that this method is called
		console.log('ajax-filetree-post-operation-expand-tree-button clicked');
		// print the item retrived from the page
		console.log( 'Value from webpage Root text box is: ' + $(".html-file-tree-root-text-box").val());

		// this method is the link between here and ajax.py python file
		// upon invoking function(data), the ajax request is sent ajax.py
		// if the request is successful, then populate the nested-jqtree with data returned from ajax.py file
		$.ajax({
			type: "POST",
			// note how the url differs from a GET operation, there is a trailing slash
			url: "ajax/filetree/post_tree/",
			dataType: "json",
			// store item from html page into this file
			// function will pass data to the corresponding method in ajax.py during the request
			data: { "my-ajax-file-tree-root": $(".html-file-tree-root-text-box").val() },
			
			// on AJAX request success 
			// populate the nested-jqtree on the webpage with the data returned from python
			// python function is tied to ajax request via the urls.py file
			// in this case the url is ajax/filetree/post/ and the function to call is ajax.filetree_post
			success: function(data) {
				// access tree_data from the data returned by python
				console.log(data.tree_data);
				$('#ajax-nested-jqtree').tree({
					// this is the data manipulated from filetree_post method in ajax.py
					data: data.tree_data,
					dragAndDrop: true
				});
			}
		});
		
	});
	

	
	// ** KEEP THIS CODE since Post methods rely on the CSRF token
	
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