config={
    "range":[],
    "point":[],
    "NOTIFY_WHEN_FULL":"True",
    "DEL_LOG":"True"
}

function pointSubmit(){
    config["point"].push({
        "VAL":$("#point-number").val(),
        "MSG":$("#point-msg").val(),
        "PLUG":getPlug()
    })
    var newRow=document.getElementById("point-table").appendChild(document.createElement("tr"))
    newRow.appendChild(document.createElement("td")).innerText=$("#point-number").val()
    newRow.appendChild(document.createElement("td")).innerText=$("#point-msg").val()
    newRow.appendChild(document.createElement("td")).innerText=getPlug()

    document.getElementById("point-form").reset()
    $("#point-number").removeAttr("aria-invalid")

    return false;
}

function rangeSubmit(){
    config["range"].push({
        "MAX_VAL":$("#max-val-per").val(),
        "MIN_VAL":$("#max-val-per").val(),
        "MSG":$("#range-msg").val(),
        "PLUG":getPlugRange()
    })
    var newRow=document.getElementById("range-table").appendChild(document.createElement("tr"))
    newRow.appendChild(document.createElement("td")).innerText=$("#max-val-per").val()
    newRow.appendChild(document.createElement("td")).innerText=$("#min-val-per").val()
    newRow.appendChild(document.createElement("td")).innerText=$("#range-msg").val()
    newRow.appendChild(document.createElement("td")).innerText=getPlugRange()

    document.getElementById("range-form").reset()
    $("#max-val-per").removeAttr("aria-invalid")
    $("#min-val-per").removeAttr("aria-invalid")

    return false;
}

function getPlug(){
    if($("#True").is(':checked')){
        return "True";
    }else if($("#False").is(':checked')){
        return "False";
    }
}

function getPlugRange(){
    if($("#TrueRange").is(':checked')){
        return "True";
    }else if($("#FalseRange").is(':checked')){
        return "False";
    }
}

function validatePercentage(el){
    if(0<$(el).val() && $(el).val()<=100){
        $(el).attr("aria-invalid","false")
    }else{
        $(el).attr("aria-invalid","true")
    }
}

function debugMode(){
    if($("#debug-mode").is(":checked")){
        config.DEL_LOG=false
    }else{
        config.DEL_LOG=true
    }
}

function downloadJson(){
    var data = "text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(config));
    $('<a href="data:' + data + '" download="config.json" role="button" id="download-json">Download config.json</a>').appendTo('#download-div');
}

$(document).ready(function() {
    $(document).on('submit', '#point-form', function() {
    if($("#point-number").attr("aria-invalid")=="false"){
        if($("#True").is(':checked') || $("#False").is(':checked')){
            pointSubmit()
        }}
      return false;
     });
});

$(document).ready(function() {
    $(document).on('submit', '#range-form', function() {
        if($("#max-val-per").attr("aria-invalid")=="false" && $("#min-val-per").attr("aria-invalid")=="false"){
            rangeSubmit()
        };
        return false;
})});