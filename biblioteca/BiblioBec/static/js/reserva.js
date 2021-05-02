
$(document).ready(function() {
    $('#id_fecha_reserva').prop('type','date')
    $('#id_fecha_reserva').prop('class','form-control')
    $('#id_fecha_desde').prop('type','date')
    $('#id_fecha_desde').prop('class','form-control')
    $('#id_fecha_hasta').prop('type','date')
    $('#id_fecha_hasta').prop('class','form-control')
    fecha = new Date()
    if((fecha.getMonth() + 1)<10){
        $("#id_fecha_reserva").prop('value',fecha.getFullYear()+'-0'+(fecha.getMonth()+1)+'-'+fecha.getDate())
        $("#id_fecha_desde").prop('value',fecha.getFullYear()+'-0'+(fecha.getMonth()+1)+'-'+fecha.getDate())
        $("#id_fecha_hasta").prop('value',fecha.getFullYear()+'-0'+(fecha.getMonth()+1)+'-'+fecha.getDate())
    }
    else{
        $("#id_fecha_reserva").prop('value',fecha.getFullYear()+'-'+(fecha.getMonth()+1)+'-'+fecha.getDate())
        $("#id_fecha_desde").prop('value',fecha.getFullYear()+'-'+(fecha.getMonth()+1)+'-'+fecha.getDate())
        $("#id_fecha_hasta").prop('value',fecha.getFullYear()+'-'+(fecha.getMonth()+1)+'-'+fecha.getDate())
  
    }
  });
  
  
  function validarForm()
  {
  
    isbn = $('#id_isbn').val()
    titulo=  $('#id_titulo').val()
    autor=  $('#id_autor').val()
    edito =  $('#id_editorial').val()
    fecha=  $('#id_fecha_publicacion').val()
    deicion=  $('#id_edicion').val()
    console.log(isbn)
    if(isbn == "")
    {
        toastr.error("Debe Ingresar el identificador del documento","ERROR",{
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
    return false
  }