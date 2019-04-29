
// Globals
let amount_of_sessions = 3;

function setUpModal(){
    // Get the modal
    var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("criteria-button");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
} 
}

function setUpAddCriteriaButton(){
    document.getElementById("add-criteria-button").onclick = function(){

        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "webapp/criteria/add";
        let url = dev_root + local_url; 

        oReq.onload = function(e) {
        let result = oReq.response ; 
            let table_start = document.getElementById("nav-bar-start");
            for(var key in result) {
                let link = document.createElement("div");
                link.innerHTML = result[key];
                table_start.appendChild(link);
             }
        }

        oReq.open("GET", url);
        oReq.send();
    };

}

function setUpGetSession(){
    $("#get-session-button").change(function(){
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/webapp/";
        let selected_session = $(this).val();
        let local_url = "get_session/" + selected_session;
        let url = dev_root + local_url;

        oReq.onload = function(e) {
        let result = oReq.response ; 
        buildDataTable(result);
        }

        oReq.open("GET", url);
        oReq.send();
    });
}


function setUpViewCriteria(){
    document.getElementById("criteria-button").onclick = function(){
        var modal = document.getElementById('myModal');
        modal.style.display = "block";

        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "webapp/criteria";
        let url = dev_root + local_url; 

        oReq.onload = function(e) {
        let result = oReq.response ; 
            let table_start = document.getElementById("nav-bar-start");
            for(var key in result) {
                let link = document.createElement("div");
                link.innerHTML = result[key];
                table_start.appendChild(link);
             }
        }

        oReq.open("GET", url);
        oReq.send();
    };

}
function buildDataTable(result){
        
    let formatted = [];
    for(var key in result) {
        let element = {
            'id' : key,
            'link' : '<a target="_blank" href=' + result[key] + '>' + result[key] + "</a>"
        }
        formatted.push(element); 
     }
    
        $('#table_id').DataTable({
            destroy: true,
            data: formatted,
            columns: [
                { data: 'id' },
                { data: 'link' }
            ],
            
            paging: true,
            scrollY: 300,
            buttons: [
                'csvHtml5', 'pdfHtml5'
            ],
            dom: 'Bfrtip',
        });
}


function setUpStartSession(){

    document.getElementById("session-button").onclick = function(){
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "start/" + (amount_of_sessions+1);
        let url = dev_root + local_url; //"http://127.0.0.1:8000/static/webapp/assets/data/link.json";

        oReq.onload = function(e) {
        let result = oReq.response ; //jQuery.parseJSON(oReq.response);
        buildDataTable(result);
    
        }
        oReq.open("GET", url);
        oReq.send();
    };
    
    
    
    // Used with no plugins
    function buildTable(result){
        let table_start_node = document.getElementById("table-start");
        let table_node = document.createElement("TABLE");
        table_node.id= "data-table";
        table_node.className = "table";
        let thead_node = document.createElement("THEAD");
    
        table_start_node.appendChild(table_node);
        table_node.appendChild(thead_node);
    
        let tr_node = document.createElement("TR");
        thead_node.appendChild(tr_node);
    
        let th_node = document.createElement("TH");
        th_node.scope - "col";
        th_node.innerText = "#";
        tr_node.appendChild(th_node);
    
        th_node = document.createElement("TH");
        th_node.scope - "col";
        th_node.innerText = "URL";
        tr_node.appendChild(th_node);
        
        th_node = document.createElement("TH");
        th_node.scope - "col";
        th_node.innerText = "Delete";
        tr_node.appendChild(th_node);
    
        let tbody_node = document.createElement("TBODY");
        table_node.appendChild(tbody_node);
    
    
        for(var key in result) {
            addLinkToTable(table_start_node, result[key].link, key);
         }
    }
    
    function addLinkToTable(tbody_node, url, key){
        let tr_node = document.createElement("TR");
        let th_node = document.createElement("TH");
        th_node.scope = "row";
        th_node.innerHTML = key;
        tr_node.appendChild(th_node);
        let td_node = document.createElement("TD");
        let link_node = document.createElement("a");
        link_node.href = url;
        link_node.target = "_blank"; 
        link_node.innerText = url;
        td_node.appendChild(link_node);
        tr_node.appendChild(td_node);
    
        tbody_node.appendChild(tr_node);
    }
}

    function main(){
        setUpModal();
        setUpStartSession();
        setUpViewCriteria();
        setUpGetSession();
    }
    main();
    