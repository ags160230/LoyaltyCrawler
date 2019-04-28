$('#jqtree-from-ajax-get').tree({
   dataUrl: {
       url: 'ajax/filetree/get',
   }
});

$('#jqtree-from-ajax-post').tree({
   dataUrl: {
       url: 'ajax/filetree/post/',
   }
});

var data = [
    {
        name: 'node1',
        children: [
            { name: 'child1' },
            { name: 'child2' }
        ]
    },
    {
        name: 'node2',
        children: [
            { name: 'child3' }
        ]
    }
];
$('#jqtree').tree({
	data: data
});