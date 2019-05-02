// Globals
let amount_of_sessions = 0;
let current_session = -1; // None selected is -1

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

function removeCriteria(event) {
    console.log(event.explicitOriginalTarget.getAttribute("value"));
    let word_to_remove = event.explicitOriginalTarget.getAttribute("value");

    var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let keyword_to_add = document.getElementById("keywordInsert").value;
        let dev_root = "http://127.0.0.1:8000/webapp/";
        let local_url = "criteria/remove/" + word_to_remove;
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            console.log(result);
            buildKeyWordTable(result);
        }
        oReq.open("GET", url);
        oReq.send();
}

function setUpRemoveSession() {
    document.getElementById("deleteSessionButton").onclick = function () {
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let keyword_to_add = document.getElementById("keywordInsert").value;
        let dev_root = "http://127.0.0.1:8000/";
        let local_url = "webapp/delete_session/" + current_session;
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            // let table_start = document.getElementById("nav-bar-start");
            buildKeyWordTable(result);
            $("#get-session-button").val(0);
            showNoData();
            setUpSessionSelector(); 
            // Update amount of sessions  
            amount_of_sessions -= 1;
            current_session = -1;
        }
        oReq.open("GET", url);
        oReq.send();

    };
}

function showNoData(){
    $('#table_id').DataTable({
        destroy: true,
        data: []
    });
}


function setUpGetSession() {
    $("#get-session-button").change(function () {
        let selected_session = $(this).val();
        getSession(selected_session);
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
            console.log(result);
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
        columns: [{
                data: 'id'
            },
            {
                data: 'link'
            }
        ],

        paging: true,
        scrollY: 300,
        buttons: [
            'csvHtml5', 'pdfHtml5'
        ],
        dom: 'Bfrtip',
        "lengthChange": true,
        "lengthMenu": [
            [5, 10, 25, 50, -1],
            [5, 10, 25, 50, "All"]
        ],
        "pageLength": 7,
        autofill: true


        //"lengthChange": true,
        //"lengthMenu": [5, 10, 25, 50, 75, 100, "All" ],
        //"pageLength": 5
    });


}

function buildKeyWordTable(result) {

    let formatted = [];
    for (var key in result) {
        let element = {
            'Keyword': '<a>' + result[key] + "</a>",
            'Remove': '<a class="remove-button"  onclick="removeCriteria(event)" value="' + result[key] + '"  >' + "Remove" + "</a>"
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

function getSession(selected_session) {
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/webapp/";
        selected_session = $("#get-session-button").val();
        current_session = selected_session;
        let local_url = "get_session/" + selected_session;
        let url = dev_root + local_url;

        oReq.onload = function (e) {
            let result = oReq.response;
            buildDataTable(result);
        }

        oReq.open("GET", url);
        oReq.send();
}


function setUpStartSession() {

    document.getElementById("session-button").onclick = function () {
        var oReq = new XMLHttpRequest();
        oReq.responseType = "json";
        let dev_root = "http://127.0.0.1:8000/webapp/";
        let keyword_list = "123";
        let local_url = "start_session/"; 
        let url = dev_root + local_url; //"http://127.0.0.1:8000/static/webapp/assets/data/link.json";

        oReq.onload = function (e) {
            let result = oReq.response; //jQuery.parseJSON(oReq.response);
            // buildDataTable(result);
            console.log("Got response from start session" + (amount_of_sessions + 1));
            setUpSessionSelector();
        }
        oReq.abort = function (e) {
            let result = oReq.response; //jQuery.parseJSON(oReq.response);
            // buildDataTable(result);
            console.log("Got response from start session" + (amount_of_sessions + 1));
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
        let unique_sessions = Object.keys(result).length;
        console.log("Number of unique sessions: " + unique_sessions);
        amount_of_sessions = unique_sessions;
        let i = 1;
        let start_node = document.getElementById("get-session-button");

        while (start_node.hasChildNodes()) {
            start_node.removeChild(start_node.lastChild);
        }

        let default_option = document.createElement("option");
        default_option.text = "None Selected";
        default_option.value = 0;
        default_option.selected = true;
        start_node.appendChild(default_option);

        Object.keys(result)
        Object.keys(result).forEach(function(key) {
            // var val = o[key];
            let option = document.createElement("option");
            option.value = key;
            option.text = "Session " + i;
            start_node.appendChild(option);
            i += 1;
          });
    }

    oReq.open("GET", url);
    oReq.send();

}

function main() {

    // Javascript to delete item from table locally
    // CSV and PDF button print whatever is locally shown on user's display
    // This function does not delete permentally
    $(document).ready(function () {
        var table = $('#table_id').DataTable();
        

        $('#table_id tbody').on('click', 'tr', function () {
            if ($(this).hasClass('selected')) {
                $(this).removeClass('selected');
            } else {
                table.$('tr.selected').removeClass('selected');
                $(this).addClass('selected');
            }
        });

        $('#deleteRowButton').click(function () {
            table.row('.selected').remove().draw(false);
        });
    });

    setUpSessionSelector();
    setUpModal();
    setUpStartSession();
    setUpViewCriteria();
    setUpGetSession();
    setUpAddCriteriaButton();
    setUpRemoveSession();
}
main();