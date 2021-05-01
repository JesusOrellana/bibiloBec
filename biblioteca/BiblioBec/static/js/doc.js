
$(document).ready(function() {
    $('#id_isbn').prop('class','form-control')
    $("#id_isbn").prop('placeholder','Identidicador del documento')
    $('#id_isbn').removeAttr("required");
    $('#id_tipo_documento_id_tipo_doc').prop('class','form-control')
    $('#id_tipo_documento_id_tipo_doc').removeAttr("required");
    $("#id_tipo_documento_id_tipo_doc option[selected]").html('Selecciona Un tipo de Documento')
    $('#id_titulo').prop('class','form-control')
    $('#id_titulo').removeAttr("required");
    $("#id_titulo").prop('placeholder','Titulo del documento')
    $('#id_autor').prop('class','form-control')
    $('#id_autor').removeAttr("required");
    $("#id_autor").prop('placeholder','Nombre autor del documento')
    $('#id_editorial').prop('class','form-control')
    $('#id_editorial').removeAttr("required");
    $("#id_editorial").prop('placeholder','Editorial del documento')
    $('#id_fecha_publicacion').prop('class','form-control')
    $('#id_fecha_publicacion').prop('type','date')
    fecha = new Date()
    if((fecha.getMonth() + 1)<10){
        $("#id_fecha_publicacion").prop('value',fecha.getFullYear()+'-0'+(fecha.getMonth()+1)+'-'+fecha.getDate())
    }
    else{
        $("#id_fecha_publicacion").prop('value',fecha.getFullYear()+'-'+(fecha.getMonth()+1)+'-'+fecha.getDate())
  
    }
    $('#id_edicion').prop('class','form-control')
    $("#id_edicion").prop('placeholder','Edición del documento')
    $('#id_categoria_id_cate').prop('class','form-control')
    $("#id_categoria_id_cate option[selected]").html('Selecciona Una categoria')
    $('#id_tipo_medio').prop('class','form-control')
    $("#id_tipo_medio option[selected]").html('Selecciona Un tipo medio')
  
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