var data1 = [
    {
        name: 'node1', id: 1,
        children: [
            { name: 'child1', id: 2 },
            { name: 'child2', id: 3 }
        ]
    },
    {
        name: 'node2', id: 4,
        children: [
            { name: 'child3', id: 5 }
        ]
    }
];

var data2 = [
{
    "name": "a",
	"type": "directory",
    "id": "1",
    "parentid": "-1"
},{
    "name": "b",
	"type": "directory",
    "id": "1",
    "parentid": "1"
},{
    "name": "c",
	"type": "directory",
    "id": "1",
    "parentid": "1"
}]
var builddata = function (data) {
    var source = [];
    var items = [];
    // build hierarchical source.
    for (i = 0; i < data.length; i++) {
        var item = data[i];
        var name = item["name"];
        var parentid = item["parentid"];
        var id = item["id"];

        if (items[parentid]) {
            var item = { parentid: parentid, name: name, item: item };
            if (!items[parentid].items) {
                items[parentid].items = [];
            }
            items[parentid].items[items[parentid].items.length] = item;
            items[id] = item;
        }
        else {
            items[id] = { parentid: parentid, name: name, item: item };
            source[id] = items[id];
        }
    }
    return source;
}

// console.log(source);
// https://godjango.com/18-basic-ajax/
$(document).ready(function() {
	
	// AJAX GET demo
	$('#ajax-demo-get').click(function(){
		console.log('ajax-demo-get called');
		$.ajax({
			type: "GET",
			url: "ajax/demo/get",
			success: function(data) {
			for(i = 0; i < data.length; i++){
				$('ul').append('<li>'+data[i]+'</li>');
			}
		}
		});
	});

	// AJAX POST demo
	$('#ajax-demo-post').click(function(){
		console.log('ajax-demo-post called');
		console.log( 'Todo box is: ' + $(".todo-item").val());

        $.ajax({
            type: "POST",
			// note how the url differs, there is a trailing slash
            url: "ajax/demo/post/",
            dataType: "json",
            data: { "ajax-item": $(".todo-item").val() },
            success: function(data) {
				$('ul').append('<li>'+data.message+'</li>');
                alert(data.message);
            }
        });
		
	});
	
	// AJAX GET filetree
	$('#ajax-filetree-get').click(function(){
		console.log('ajax-filetree-get called');
		$.ajax({
			type: "GET",
			url: "ajax/filetree/get",
			success: function(data) {
				// build the tree from my.jstree.js file using the data from success function
				//var instance = $('#jstree-events').jstree(true);
				//instance.deselect_all();
				//instance.select_node('1');
				// build another tree from my.jqtree.js file using data
				$('#tree1').tree({data: data});
		}
		});
	});
	
	// AJAX GET filetree
	$('#ajax-filetree-move').click(function(){
		console.log('ajax-filetree-move called');
		$.ajax({
			type: "GET",
			url: "ajax/filetree/move",
			success: function(data) {
				// build the tree from my.jstree.js file using the data from success function
				//var instance = $('#jstree-events').jstree(true);
				//instance.deselect_all();
				//instance.select_node('1');
				// build another tree from my.jqtree.js file using data
				$('#tree1').tree({data: data});
		}
		});
	});

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