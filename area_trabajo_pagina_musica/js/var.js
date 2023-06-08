
// registro

console.log("hola mundo")

const form =document.getElementById("form") 
const email=document.getElementById("email")
const contrasena=document.getElementById("contrasena")
const confirm_contrasena=document.getElementById("confirm_contrasena")


form.addEventListener("submit",e=> {
    
    let regexEmail=/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/

    if(!regexEmail.test(email.value)){
        alert("email invalido")
        return false
    }

    if (contrasena.value.length =="") {
        alert("contraseña invalida")
        return false
    }

    if (contrasena.value != confirm_contrasena.value){
        alert("Confirmación no coincide")
        return false
    }


    alert("datos enviados exitosamente")  
    
    return true
})


// inicio de sesion



