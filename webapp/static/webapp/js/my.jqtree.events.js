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
        console.log('moved_node', moved_node);
        console.log('target_node', target_node);
        console.log('position', position);
        console.log('previous_parent', previous_parent);
		
		// let user confirm move
        if (confirm('Really move?')) {
            event.move_info.do_move();
			
			// do ajax request to return to python
			$.ajax({
				type: "POST",
				url: "ajax/filetree/move/",
				// has to be a post call so we can edit data
				data: 	{ 
							"moved_node_name": moved_node.name,
							"target_node_name": target_node.name,
							"position": position,
							"previous_parent_name": previous_parent.name,
						},
				//data: { "moved-node": moved_node },
				success: function(data) {
			}
			});
        }
    }
);