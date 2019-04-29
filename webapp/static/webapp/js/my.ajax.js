
// https://godjango.com/18-basic-ajax/
$(document).ready(function() {

	// AJAX POST filetree
	$('#ajax-filetree-post').click(function(){
		console.log('ajax-filetree-post called');
		console.log( 'Root is: ' + $(".file-tree-root").val());

        $.ajax({
            type: "POST",
			// note how the url differs, there is a trailing slash
            url: "ajax/filetree/post/",
            dataType: "json",
            data: { "ajax-file-tree-root": $(".file-tree-root").val() },
            success: function(data) {
				// access tree_data from the data returned
				console.log(data.tree_data);
				console.log(data1);
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

});