// data from callback
$('#clbk').jstree({
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
	var instance = $('#evts').jstree(true);
	instance.deselect_all();
	$('#evts').jstree('close_all');
});

$('#expand-tree-button').on("click", function () {
	var instance = $('#evts').jstree(true);
	instance.deselect_all();
	instance.select_node('1');
});

$('#evts')
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