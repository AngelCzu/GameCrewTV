
//PASSWORD EN REGISTRO
document.getElementById("ocultarReg").style.display = "none";

function passwordRegistro() {
    const mostrar = document.getElementById("mostrarReg");
    const input = document.getElementById("txtPasswordReg");
    if (input.type == "password") {
        input.type = "text";
        ocultarReg.style.display = "inline";
        mostrarReg.style.display = "none";
    }else{
        input.type = "password";
        ocultarReg.style.display = "none";
        mostrarReg.style.display = "inline";
    }
}

//PASSWORD EN INGRESAR
document.getElementById("ocultarIng").style.display = "none";
function passwordIngresar() {
    const mostrar = document.getElementById("mostrarIng");
    const input = document.getElementById("txtPasswordIng");
    if (input.type == "password") {
        input.type = "text";
        ocultarIng.style.display = "inline";
        mostrarIng.style.display = "none";
    }else{
        input.type = "password";
        ocultarIng.style.display = "none";
        mostrarIng.style.display = "inline";
    }
}


//FUNCIONES DEL DARKMODE
 
const toggle = document.getElementById('toggleDark'); //LISTO
const body = document.querySelector('body'); //LISTO
const contenedorP = document.getElementById('contenedorPrincipalBody'); //LISTO


//REGISTRO
const txtLabelReg = document.getElementById('txtLabelReg'); //LISTO
const labelTxtNomUsu = document.getElementById('labelTxtNomUsu'); //LISTO
const labelTxtCorreo = document.getElementById('labelTxtCorreo'); //LISTO
const labelTxtPassReg = document.getElementById('labelTxtPassReg'); //LISTO
const buttonTxtReg = document.getElementById('buttonTxtReg'); //LISTO
const houseIcon = document.getElementById('houseIcon');//LISTO

//INGRESAR
const contenedorIng = document.getElementById('contenedorIng'); //LISTO 
const txtLabelIng = document.getElementById('txtLabelIng'); //LISTO
const labelTxtUsuIng = document.getElementById('labelTxtUsuIng');//LISTO
const labelTxtPassIng = document.getElementById('labelTxtPassIng');//LISTO
const buttonTxtIng = document.getElementById('buttonTxtIng');//LISTO

toggle.addEventListener('click', function(){
    this.classList.toggle('bi-moon-stars-fill');
    if(this.classList.toggle('bi-brightness-high-fill')){
        body.style.background = 'white';
        body.style.color = 'white';
        body.style.transition = '1s';
        
        contenedorP.style.background = 'white';
        contenedorP.style.color = 'black';
        contenedorP.style.transition = '1s';

        contenedorIng.style.background = '#f3f2f2';

        txtLabelIng.style.color = 'black';
        txtLabelReg.style.color = 'black';
        houseIcon.style.color = 'black';
        houseIcon.style.transition = '4.7s';

        labelTxtNomUsu.style.color = 'black';
        labelTxtCorreo.style.color = 'black';
        labelTxtPassReg.style.color = 'black';
        buttonTxtReg.style.color = 'white';

        labelTxtUsuIng.style.color = 'black';
        labelTxtPassIng.style.color = 'black';
        buttonTxtIng.style.color = 'white';




    }else{
        body.style.background = '#1E1E1E';
        body.style.color = 'white';
        body.style.transition = '1s';
        
        contenedorP.style.background = '#2d2d2d';
        contenedorP.style.color = 'white';
        contenedorP.style.transition = '1s';

        contenedorIng.style.background = '#454545';

        txtLabelIng.style.color = 'white';
        txtLabelReg.style.color = 'white';
        houseIcon.style.color = 'white';
        houseIcon.style.transition = '4.7s';

        labelTxtNomUsu.style.color = 'white';
        labelTxtCorreo.style.color = 'white';
        labelTxtPassReg.style.color  = 'white';
        buttonTxtReg.style.color = 'white';

        labelTxtUsuIng.style.color = 'white';
        labelTxtPassIng.style.color = 'white';
        buttonTxtIng.style.color = 'white';
    }
});


$(function () {
    $("#formReg").validate({
     rules:{
        txtNomUsuReg:{
             required: true,
             maxlength:10
         },
         txtCorreoReg:{
             required: true,
             email:true
         },
         txtPasswordReg:{
            required: true
         },
         txtUsuIng:{
            required: true
         },
         txtPasswordIng:{
            required: true
         }
 
     },
     messages:{
        txtNomUsuReg:{
             required: "El nombre de usuario es un campo obligatorio",
             maxlength: "El maximo de carateres es 10"
         },
         txtCorreoReg:{
             required: "El correo es un campo obligatorio",
             email: "El formato de correo no es valido"
         },
         txtPasswordReg:{
            required: "La contraseña es obligatoria"
         },
         txtUsuIng:{
            required: "El nombre de usuario es un campo obligatorio"
         },
         txtPasswordIng:{
            required: "La contraseña es un campo obligatorio"
         }
     }
    })
 });


 $(function () {
    $("#formLogin").validate({
     rules:{
         txtUsuIng:{
            required: true
         },
         txtPasswordIng:{
            required: true
         }
 
     },
     messages:{

         txtUsuIng:{
            required: "El nombre de usuario es un campo obligatorio"
         },
         txtPasswordIng:{
            required: "La contraseña es un campo obligatorio"
         }
     }
    })
 });