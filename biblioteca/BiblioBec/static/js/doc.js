
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
    $('#id_fecha_publicacion').removeAttr("required");
    $('#id_tipo_medio').removeAttr("required");
    $('#id_edicion').removeAttr("required");
    $('#id_categoria_id_cate').removeAttr("required");
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
    btn_estado1 = true
    btn_estado2 = true
  });
  
  function validarForm()
  {
    isbn = $('#id_isbn').val()
    titulo=  $('#id_titulo').val()
    autor=  $('#id_autor').val()
    edito =  $('#id_editorial').val()
    fecha=  $('#id_fecha_publicacion').val()
    edicion=  $('#id_edicion').val()
    t_doc=  $('#id_tipo_documento_id_tipo_doc').val()
    cate = $('#id_categoria_id_cate').val()
    medio = $('#id_tipo_medio').val()
    imagen = $('#id_imagen').val()
    ubi = $('#id_ubicacion').val()
    estado = $('#id_estado').val()
    stock = $('#id_stock').val()

    var exr = new RegExp("^[0-9,$]");
    if(isbn == "")
    {
        $('#id_isbn').focus()
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
    if(titulo == "")
    {
        $('#id_titulo').focus()
        toastr.error("Debe Ingresar el titulo del documento","ERROR",{
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
    if(autor == "")
    {
        $('#id_autor').focus()
        toastr.error("Debe Ingresar el nombre del autor del documento","ERROR",{
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
    if(edito == "")
    {
        $('#id_editorial').focus()
        toastr.error("Debe Ingresar la editorial del documento","ERROR",{
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
    if(edicion == "")
    {
        $('#id_edicion').focus()
        toastr.error("Debe Ingresar el numero de edición del documento","ERROR",{
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
    if(!exr.test(edicion))
    {
        $('#id_edicion').focus()
        toastr.error("Solo puede ingresar numeros en la edición del documento","ERROR",{
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
    if(fecha =="")
    {   
        if(btn_estado1)
        {   
            $("#btn-dd").click()
            btn_estado1 = false;
        }
        $('#id_fecha_publicacion').focus()
        toastr.error("Debe ingresar una fecha de publicación del documento","ERROR",{
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
    if(t_doc =="")
    {   
        
        $('#id_tipo_documento_id_tipo_doc').focus()
        toastr.error("Debe ingresar el tipo de documento","ERROR",{
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
    if(cate =="")
    {   
        
        $('#id_categoria_id_cate').focus()
        toastr.error("Debe ingresar la categoria del documento","ERROR",{
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
    if(medio =="")
    {   
        
        $('#id_tipo_medio').focus()
        toastr.error("Debe ingresar el tipo de medio","ERROR",{
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
    if(imagen =="")
    {   
        
        $('#id_imagen').focus()
        toastr.error("Debe adjuntar una imagen","ERROR",{
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
    if(ubi =="")
    {   
        if(btn_estado2)
        {   
            $("#btn-ld").click()
            btn_estado2 = false;
        }
        $('#id_ubicacion').focus()
        toastr.error("Debe ingresar la ubicación del documento en estanterias","ERROR",{
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
    if(estado =="")
    {   
        
        $('#id_estado').focus()
        toastr.error("Debe ingresar el estado del documento","ERROR",{
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
    if(stock =="")
    {   
        
        $('#id_stock').focus()
        toastr.error("Debe ingresar la cantidad de existencia del documento","ERROR",{
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
    if(!exr.test(stock))
    {   
        
        $('#id_stock').focus()
        toastr.error("Debe ingresar la cantidad de existencia del documento","ERROR",{
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

  function deleteDoc(isbn)
  {
    $("#eliminar_documento").prop("href",'documento-delete/'+isbn);
    //$("#eliminar_documento").prop("class",'btn-warning');
  }