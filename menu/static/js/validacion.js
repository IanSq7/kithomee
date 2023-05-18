var input = document.getElementById('name');
input.oninvalid = function(event) {
    event.target.setCustomValidity('Solo Letras')
}


$(document).ready(function (){
    //Validacion de Campos Vacios
    var name, lastname, password, comfirpass, email, cell, street, postalcode;
    
    $(".btnAction").on('click',function(){
        name = $("#name").val();
        lastname = $('#lastname').val();
        password = $("#password").val();
        comfirpass = $("#comfirpass").val();
        email = $("#email").val();
        cell = $("#cell").val();
        street = $("#street").val();
        postalcode = $("#postalcode").val();

        if(name.length == 0 || lastname.length == 0 || password.length == 0 || comfirpass.length == 0 || email.length == 0 || cell.length == 0 || street.length == 0 || postalcode.length == 0){
            alert("Campos Sin Rellenar.");
        }
        else if(password.length < 8){
            alert("La contraseña no puede tener menos de 8 caracteres")
        }
        else if(password.length > 12){
            alert("La contraseña no debe superar los 12 caracteres")
        }
        else if(comfirpass != password){
            alert("Las contraseñas no coinciden.")
        }
        else if(!validar.test($('#password').val)){
            alert("La contraseña debe contener numeros, caracteres, minuscula y mayuscula")
        }

        else if($("#email").val().indexOf('@', 0) == -1 || $("#email").val().indexOf('.', 0) == -1) {
            alert('El correo electrónico introducido es invalido.');
        }else{
            alert("Registro Completo");
            $("#form")[0].reset();
        }
    })
})
function validarPrecio() {
    var precio = document.getElementById("precio").value;
    if (precio < 0) {
    alert("El precio no puede ser negativo.");
    return false;
    }
    return true;
}


function validar() {
    console.log('Registrado');
    FormData.reset();
    return true;
}