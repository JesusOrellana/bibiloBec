function checkRut(rut) {
  // Despejar Puntos
  var valor = rut.value.replace(".", "");
  // Despejar Guión
  valor = valor.replace("-", "");

  // Aislar Cuerpo y Dígito Verificador
  cuerpo = valor.slice(0, -1);
  dv = valor.slice(-1).toUpperCase();

  // Formatear RUN
  rut.value = cuerpo + dv;

  // Si no cumple con el mínimo ej. (n.nnn.nnn)
  if (cuerpo.length < 8) {
    rut.setCustomValidity("RUT incompleto");
    return false;
  }

  // Calcular Dígito Verificador
  suma = 0;
  multiplo = 2;

  // Para cada dígito del Cuerpo
  for (i = 1; i <= cuerpo.length; i++) {
    // Obtener su Producto con el Múltiplo Correspondiente
    index = multiplo * valor.charAt(cuerpo.length - i);

    // Sumar al Contador General
    suma = suma + index;

    // Consolidar Múltiplo dentro del rango [2,7]
    if (multiplo < 7) {
      multiplo = multiplo + 1;
    } else {
      multiplo = 2;
    }
  }

  // Calcular Dígito Verificador en base al Módulo 11
  dvEsperado = 11 - (suma % 11);

  // Casos Especiales (0 y K)
  dv = dv == "K" ? 10 : dv;
  dv = dv == 0 ? 11 : dv;

  // Validar que el Cuerpo coincide con su Dígito Verificador
  if (dvEsperado != dv) {
    rut.setCustomValidity("RUT inválido");
    return false;
  }

  // Si todo sale bien, eliminar errores (decretar que es válido)
  rut.setCustomValidity("");
}
$(document).ready(() => {
  $("#password2").on("input", (e) => {
    password1 = document.getElementById("password1");
    password2 = document.getElementById("password2");
    if (password1.value != password2.value) {
      password2.setCustomValidity("Las contraseñas no coinciden");
      return false;
    } else {
      password2.setCustomValidity("");
    }
  });
});

function validarFormUsuario() {
  rut_usr = $('#rut_usr').val()
  nombre =  $('#nombre').val()
  apellido_p =  $('#apellido_p').val()
  apellido_m =  $('#apellido_m').val()
  direccion =  $('#direccion').val()
  telefono =  $('#telefono').val()
  correo =  $('#correo').val()
  password = $('#password').val()

if (rut_usr == "")
{
  $('#rut_usr').focus()
  toastr.error("Debe ingresar el RUT del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
}

if (nombre == "")
{
  $('#nombre').focus()
  toastr.error("Debe ingresar el nombre del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (apellido_p == "")
{
  $('#apellido_p').focus()
  toastr.error("Debe ingresar el apellido paterno del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (apellido_m == "")
{
  $('#apellido_m').focus()
  toastr.error("Debe ingresar el apellido materno del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (apellido_m == "")
{
  $('#apellido_m').focus()
  toastr.error("Debe ingresar el apellido materno del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (direccion == "")
{
  $('#direccion').focus()
  toastr.error("Debe ingresar la dirección del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (telefono == "")
{
  $('#telefono').focus()
  toastr.error("Debe ingresar el teléfono del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (correo == "")
{
  $('#correo').focus()
  toastr.error("Debe ingresar el correo del usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

if (password == "")
{
  $('#password').focus()
  toastr.error("Debe ingresar una password para el usuario","ERROR",{
      "closeButton": true,
      "debug": false,
      "newestOnTop": false,
      "progressBar": true,
      "positionClass": "toast-bottom-right",
      "preventDuplicates": false,
      "onclick": null,
      "showDuration": "300",
      "hideDuration": "1000",
      "timeOut": "5000",
      "extendedTimeOut": "1000",
      "showEasing": "swing",
      "hideEasing": "linear",
      "showMethod": "fadeIn",
      "hideMethod": "fadeOut"
  });
  return false;
} 

}
