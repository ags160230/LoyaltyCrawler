



document.getElementById("session-button").onclick = function(){

    var oReq = new XMLHttpRequest();
    oReq.responseType = "json";
    let dev_root = "http://127.0.0.1:8000/";
    let url = "http://127.0.0.1:8000/static/webapp/assets/data/link.json";
    let local_url = "/webapp/assets/data/link.json";
    // console.log(url);
    oReq.onload = function(e) {
    let result = oReq.response ; //jQuery.parseJSON(oReq.response);
    buildTable(result);

    }
    oReq.open("GET", url);
    oReq.send();
};

function buildTable(result){
    let table_start_node = document.getElementById("table-start");
    let table_node = document.createElement("TABLE");
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
// <table class="table">
//   <thead>
//   <tr>
//     <th scope="col">#</th>
//     <th scope="col">URL</th>
//   </tr>
// </thead>
// <tbody>
//   <tr>
//     <th scope="row">1</th>
//     <td>Mark</td>
//   </tr>
//   <tr>
//     <th scope="row">2</th>
//     <td>Jacob</td>
//   </tr>
//   <tr>
//     <th scope="row">3</th>
//     <td>Larry</td>
//   </tr>
// </tbody>
// </table>
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