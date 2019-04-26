

function setUpModal(){
    // Get the modal
var modal = document.getElementById('myModal');

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

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

setUpModal();

document.getElementById("session-button").onclick = function(){

    var oReq = new XMLHttpRequest();
    oReq.responseType = "json";
    let dev_root = "http://127.0.0.1:8000/";
    let url = "http://127.0.0.1:8000/static/webapp/assets/data/link.json";
    let local_url = "/webapp/assets/data/link.json";
    // console.log(url);
    oReq.onload = function(e) {
    let result = oReq.response ; //jQuery.parseJSON(oReq.response);
    buildDataTable(result);

    }
    oReq.open("GET", url);
    oReq.send();
};

function buildDataTable(result){
    
    let formatted = [];
    for(var key in result) {
        formatted.push({
            'id' : key,
            'link' : '<a target="_blank" href=' + result[key].link + '>' + result[key].link + "</a>"
        }); 
     }
     console.log(formatted);
    
    $(document).ready( function () {
        $('#table_id').DataTable({
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
    } );
}


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



var toggler = document.getElementsByClassName("caret");
    var i;

    for (i = 0; i < toggler.length; i++) {
      toggler[i].addEventListener("click", function() {
        this.parentElement.querySelector(".nested").classList.toggle("active");
        this.classList.toggle("caret-down");
      });
    }

    function isSessionActive() {
        document.getElementById("session-button").onclick = function(){
            console.log("WORKInG");
                  };
      $(document).ready(function(){
          
        $('.session-button' ).click(function(){
          $('.session-button').html('Stop Web Crawler Session');
          $('.session-button').css('background-color', 'red');
          $('.session-button:hover').css('background-color', '#f63c3c');
        });
      });
    }