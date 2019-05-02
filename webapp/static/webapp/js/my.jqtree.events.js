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
				confirm('Specified destination directory already has a file named ' + child_at_destination.name +'. Move canceled.');
			}
		}
		
		// check is path is a file
		if (target_node.type == 'file'){
			move = -1;
			confirm('Specified destination directory is a file. Move canceled');
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

$('#ajax-nested-jqtree').on(
    'tree.dblclick',
    function(event) {
		
        // event.node is the clicked node
        console.log(event.node);
		
		// prompt user for new name
		var new_name = prompt("Enter new name");
		
		// save attributes from node
        var renamed_node = event.node;
        var parent_node = event.node.parent;
		
		// print to console
        console.log('renamed_node', renamed_node);
        console.log('parent', parent_node);
		

		var rename = 1;
		var i;
		for (i = 0; i < parent_node.children.length; i++) { 
			child_at_destination = parent_node.children[i];
			// if parent already has existing child with same name
			if (child_at_destination.name == new_name){
				rename = -1;
				confirm('Parent directory already has a file named ' + new_name +'. Rename canceled.');
			}
		}
		
		// check is path is a file
		//if (target_node.type == 'file'){
			//move = -1;
			//confirm('Specified destination directory is a file. Move canceled');
		//}
		
		// do move
        if (rename == 1) {

			// has to be a post call so we can edit data
			// do ajax request to return to python
			$.ajax({
				type: "POST",
				url: "ajax/filetree/rename/",
				// assemble data to send to python
				// DON'T send python the node objects themselves
				// this will mess up the jqtree objects
				data: 	{ 
							"my_jq_tree_renamed_node_id": renamed_node.id,
							"my_jq_tree_parent_node_id": parent_node.id,
							"my_jq_tree_new_name": new_name ,
						},
						
				// on AJAX request success 
				// call python function to move the file
				// python function is tied to ajax request via the urls.py file
				// in this case the url is ajax/filetree/move and the function to call is ajax.filetree_move
				success: function(data) {
					// at this point the data has been returned by python to AJAX
					// no need to do anything with it, since jqtree handles the webpage tree nodes
					console.log("Data returned from python" + data.message);
					// add new node
					$('#ajax-nested-jqtree').tree(
						'addNodeAfter',
						{
							name: new_name,
							id: data.new_node_id
						},
						renamed_node
					);
					// delete old node
					$('#ajax-nested-jqtree').tree('removeNode', renamed_node);
				}
			});
        }

    }
	
);