
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
    $(".Aceptar").click(function(){
        fecha = $("#id_fecha_desde").val();
        f=new Date(fecha)
        $("#id_fecha_hasta").prop("min",fecha);
        $("#idlabel").removeAttr("hidden");
        $("#idlabel2").removeAttr("hidden");
        fh=new Date(f)
        fh.setDate(f.getDate()+6)
        dia=fh.getDate()
        mes=fh.getMonth()+1
        ano=fh.getFullYear()
        if (mes  <10) 
        mes = '0' + mes;
        if (dia  <10) 
        dia = '0' + dia;
        fh= [ano, mes, dia].join('-');
        $("#id_fecha_hasta").prop("max",fh);
       
        
    });
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
  function validarForm()
  {
    fecha_d = $('#id_fecha_desde').val()
    fecha_h = $('#id_fecha_hasta').val()
    
    var exr = new RegExp("^[0-9,$]");
    if(fecha_d == "")
    {
        $('#id_fecha_desde').focus()
        toastr.error("Debe Ingresar valida inicial","ERROR",{
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
    if(fecha_h == "")
    {
        $('#id_fecha_hasta').focus()
        toastr.error("Debe Ingresar fecha valida de termino","ERROR",{
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
