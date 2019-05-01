// events for ajax-nested-jqtree which is built in the my.ajax file
$('#ajax-nested-jqtree').on(
    'tree.move',
    function(event) {
        event.preventDefault();
		
		// save attributes from moved_info
        var moved_node = event.move_info.moved_node;
        var target_node = event.move_info.target_node;
        var position = event.move_info.position;
        var previous_parent = event.move_info.previous_parent;
		
		// print to console
		console.log('new build');
		
        console.log('moved_node', moved_node);
        console.log('target_node', target_node);
        console.log('position', position);
        console.log('previous_parent', previous_parent);
		

		var move = 1;
		var i;
		for (i = 0; i < target_node.children.length; i++) { 
			child_at_destination = target_node.children[i];
			// if parent already has existing child with same name
			if (child_at_destination.name == moved_node.name){
				move = -1;
				confirm('Directory already has a file named ' + child_at_destination );
			}
		}

		// do move
        if (move == 1) {
            event.move_info.do_move();
			
			// has to be a post call so we can edit data
			// do ajax request to return to python
			$.ajax({
				type: "POST",
				url: "ajax/filetree/move/",
				// assemble data to send to python
				// DON'T send python the node objects themselves
				// this will mess up the jqtree objects
				data: 	{ 
							"my_jq_tree_moved_node_id": moved_node.id,
							"my_jq_tree_target_node_id": target_node.id,
							"my_jq_tree_position": position,
							"my_jq_tree_previous_parent_id": previous_parent.id,
						},
						
				// on AJAX request success 
				// call python function to move the file
				// python function is tied to ajax request via the urls.py file
				// in this case the url is ajax/filetree/move and the function to call is ajax.filetree_move
				success: function(data) {
					// at this point the data has been returned by python to AJAX
					// no need to do anything with it, since jqtree handles the webpage tree nodes
					console.log("Data returned from python" + data.message);
			}
			});
        }
    }
);