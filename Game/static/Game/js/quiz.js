window.setTimeout(function () {
    //check all radio
    var radios = document.getElementsByTagName('input');
    var no_checked = true;
    for (var i = 0; i < radios.length; i++) {
    if (radios[i].type === 'radio' && radios[i].checked) {
        no_checked = false;
        }
    }
    if(no_checked){
        document.getElementById('radio0').checked = true;
        document.getElementById('radio0').value = currentPlayerId+"$$LATE$$"+roomId;
    }
    document.answer.submit();
}, roomTime * 1000);
