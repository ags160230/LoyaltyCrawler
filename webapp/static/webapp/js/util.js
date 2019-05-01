// Globals
let amount_of_sessions = 4;

function setUpModal() {
    // Get the modal
    var modal = document.getElementById('myModal');

    // Get the button that opens the modal
    var btn = document.getElementById("criteria-button");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on the button, open the modal

    // When the user clicks on <span> (x), close the modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
}

function setUpAddCriteriaButton() {
    document.getElementById("add-criteria-button").onclick = function () {

        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let keyword_to_add = document.getElementById("keywordInsert").value;
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "webapp/criteria/add/" + keyword_to_add;
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            // let table_start = document.getElementById("nav-bar-start");
            buildKeyWordTable(result);
        }

        oReq.open("GET", url);
        oReq.send();
    };
}

function removeCriteria(e) {
    console.log(e);
    // this.text
}

function setUpRemoveSession(){

}

function setUpGetSession() {
    $("#get-session-button").change(function () {
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/webapp/";
        let selected_session = $(this).val();
        let local_url = "get_session/" + selected_session;
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            buildDataTable(result);
        }

        oReq.open("GET", url);
        oReq.send();
    });
}

function setUpViewCriteria() {
    document.getElementById("criteria-button").onclick = function () {
        var modal = document.getElementById('myModal');
        modal.style.display = "block";

        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "webapp/criteria";
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            buildKeyWordTable(result);

        }

        oReq.open("GET", url);
        oReq.send();
    };

}

function buildDataTable(result) {

    let formatted = [];
    for (var key in result) {
        let element = {
            'id': key,
            'link': '<a target="_blank" href=' + result[key] + '>' + result[key] + "</a>"
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
        "lengthChange": true,
        "lengthMenu": [ [5, 10, 25, 50, -1], [5, 10, 25, 50, "All"] ],
        "pageLength": 7,
        autofill: true


        //"lengthChange": true,
        //"lengthMenu": [5, 10, 25, 50, 75, 100, "All" ],
        //"pageLength": 5
    });

    // Javascript to delete item from table locally
    // CSV and PDF button print whatever is locally shown on user's display
    // This function does not delete permentally
    $(document).ready(function() {
        var table = $('#table_id').DataTable();
     
        $('#table_id tbody').on( 'click', 'tr', function () {
            if ( $(this).hasClass('selected') ) {
                $(this).removeClass('selected');
            }
            else {
                table.$('tr.selected').removeClass('selected');
                $(this).addClass('selected');
            }
        } );
     
        $('#deleteRowButton').click( function () {
            table.row('.selected').remove().draw( false );
        } );
    } );
}

function buildKeyWordTable(result) {

    let formatted = [];
    for (var key in result) {
        let element = {
            'Keyword': '<a>' + result[key] + "</a>",
            'Remove': '<a class="remove-button"  onclick="removeCriteria()"  >' + "Remove" + "</a>"
        }
        formatted.push(element);
    }

    $('#keyword_table').DataTable({
        destroy: true,
        data: formatted,
        columns: [{
                data: 'Keyword'
            },
            {
                data: 'Remove'
            }
        ],
        buttons: [],
        paging: true,
        scrollY: 250,
        dom: 'Bfrtip',
    });

}


function setUpStartSession() {

    document.getElementById("session-button").onclick = function () {
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/webapp/";
        let local_url = "start_session/" + (amount_of_sessions + 1);
        let url = dev_root + local_url; //"http://127.0.0.1:8000/static/webapp/assets/data/link.json";

        oReq.onload = function (e) {
            let result = oReq.response; //jQuery.parseJSON(oReq.response);
            // buildDataTable(result);
            console.log(result);
            setUpSessionSelector();
        }
        oReq.open("GET", url);
        oReq.send();
    };

    function addLinkToTable(tbody_node, url, key) {
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

function setUpSessionSelector() {
    var oReq = new XMLHttpRequest();
    oReq.responseType = "json";
    let dev_root = "http://127.0.0.1:8000/webapp/";
    let local_url = "check_last_session_index";
    let url = dev_root + local_url;

    oReq.onload = function (e) {
        let result = oReq.response;
        console.log(result[0]);
        amount_of_sessions = result[0];
        let i = 1;
        let start_node = document.getElementById("get-session-button");

        while (start_node.hasChildNodes()) {
            start_node.removeChild(start_node.lastChild);
        }

        let default_option = document.createElement("option");
        default_option.text = "None Selected";
        default_option.selected = true;
        start_node.appendChild(default_option);

        while (i < amount_of_sessions + 1) {
            let option = document.createElement("option");
            option.value = i;
            option.text = "Session " + i;
            start_node.appendChild(option);
            // id="get-session-button";
            i += 1;
        }
    }

    oReq.open("GET", url);
    oReq.send();

}

function main() {

    setUpSessionSelector();
    setUpModal();
    setUpStartSession();
    setUpViewCriteria();
    setUpGetSession();
    setUpAddCriteriaButton();
    setUpRemoveSession();
}
main();