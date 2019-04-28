// data from callback
$('#jstree-callback').jstree({
	'core' : {
		'data' : function (node, cb) {
			if(node.id === "#") {
				cb([{"text" : "Callback Root", "id" : "1", "children" : true}]);
			}
			else {
				cb(["Child"]);
			}
		}
	}
});

// interaction and events
$('#collapse-tree-button').on("click", function () {
	alert('Hide tree')
	var instance = $('#jstree-events').jstree(true);
	instance.deselect_all();
	$('#jstree-events').jstree('close_all');
});

$('#expand-tree-button').on("click", function () {
	// load ajax data to the dummy url
	// this is what the jstree-events pulls from
	//$('#ajax-filetree-get').load( "ajax/filetree/get");
	$('#ajax-demo-get').load( "ajax/demo/get/");
	//var instance = $('#jstree-events').jstree(true);
	//instance.deselect_all();
	//instance.select_node('1');
});

$('#jstree-events')
	.on("changed.jstree", function (e, data) {
		if(data.selected.length) {
			alert('The selected node is: ' + data.instance.get_node(data.selected[0]).text);
		}
	})
	.jstree({
		'core' : {
			'multiple' : false,
			'data' : [
				{ "text" : "Clickable Root", "children" : [
						{ "text" : "Child node 1", "id" : 1 },
						{ "text" : "Child node 2", "id" : 2 }
				]}
			]
		}
	});