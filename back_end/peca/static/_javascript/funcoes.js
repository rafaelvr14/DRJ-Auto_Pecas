function validacao(){
    var password = document.getElementById("password")
    , confirm_password = document.getElementById("confirm_password");
    if(password.value != confirm_password.value) {
        confirm_password.setCustomValidity("Senhas diferentes!");
    } else {
        confirm_password.setCustomValidity("");
        }
    password.onchange = validatePassword;
    confirm_password.onkeyup = validatePassword;
}
function clienteFixo(valor){
    var val=valor.clienteFixo;
    if(val=="ClienteFixo"){
        window.location.href="file:///C:/Users/rafael/Desktop/DRJ-Auto_Pecas/_paginas/registro_clienteFixo.html";
    }
    else{
        window.location.href="../_paginas/index.html";
    }
}