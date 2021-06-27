
$(document).ready(function() {

  $('#id_tipo_documento_id_tipo_doc').prop('class','form-control')
  $('#id_categoria_id_cate').prop('class','form-control')
  $('#id_tipo_medio').prop('class','form-control')
  $('#id_editorial').prop('class','form-control')
  t_doc = $('#t_doc').val()
  $("#id_tipo_documento_id_tipo_doc option[value="+t_doc+"]").attr("selected",true);
  t_cat = $('#t_cat').val()
  $("#id_categoria_id_cate option[value="+t_cat+"]").attr("selected",true);
  t_med = $('#t_med').val()
  $("#id_tipo_medio option[value="+t_med+"]").attr("selected",true);
  t_edit = $('#t_edit').val()
  $("#id_editorial option[value="+t_edit+"]").attr("selected",true);
  $('#id_fecha_publicacion').removeAttr("required");
  $('#id_tipo_medio').removeAttr("required");
  $('#id_edicion').removeAttr("required");
  $('#id_categoria_id_cate').removeAttr("required");
  $('#id_tipo_documento_id_tipo_doc').removeAttr("required");
  $('#id_editorial').removeAttr("required");
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
  if(imagen =="")
  {
      $('#id_opcion').prop('value','b')
  }
}

$(".eliminarEjem").click(function(){
    eliminarEjemplar($(this).attr("data-ejem"));
});

function eliminarEjemplar(id_ejem){
    

    const csrftoken = getCookie('csrftoken');

    $.ajax({
        url: '/ejemplar/delete/',
        method: 'POST',
        data:{
            'ejem': id_ejem,
            csrfmiddlewaretoken: csrftoken
        },
        async: false,
        success: function(data){
            count = 0
            console.log(data)
            if(data == 1)
            {
                
                toastr.success("Ejemplar "+id_ejem+" eliminado con exito","EXITO",{
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

                $("#ejem-"+id_ejem).css("display","none")
            
               
            }
            else
            {
                toastr.error("Ha ocurrido un problema, no se pudo eliminar el ejemplar","ERROR",{
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
            }
        }
    })

    setTimeout('cambiarHecho()', hora());

} 


function cambiarHecho()
{
    $("#hecho").prop("value","0")
}
function cambiarHecho2()
{
    console.log("recargando...")
    location.reload()
}
function hora()
{
horaActual  = new Date();
horaProgramada  = new Date();
horaProgramada.setHours(horaActual.getHours());
horaProgramada.setMinutes(horaActual.getMinutes());
horaProgramada.setSeconds(horaActual.getSeconds()+2);
return horaProgramada.getTime() - horaActual.getTime(); 
}

function hora2()
{
horaActual  = new Date();
horaProgramada  = new Date();
horaProgramada.setHours(horaActual.getHours());
horaProgramada.setMinutes(horaActual.getMinutes());
horaProgramada.setSeconds(horaActual.getSeconds()+2);
return horaProgramada.getTime() - horaActual.getTime(); 
}

//actualizar stock
$("#actualizarStock").click(function(){
    isbn = $(this).attr("data-isbn")
    stock = $('#stock').val()
    ubi = $(this).attr("data-ubi")
    actualizarStock(isbn,stock,ubi)
})

function actualizarStock(isbn,stock,ubi) {
    

    const csrftoken = getCookie('csrftoken');
    if(validarStock())
    {
        $.ajax({
            url: '/ejemplar/update/',
            method: 'POST',
            data:{
                'isbn': isbn,
                'stock': stock,
                'ubi':ubi,
                csrfmiddlewaretoken: csrftoken
            },
            async: false,
            success: function(data){
                if(data == 1)
                {
                    
                    toastr.success("Operación realizada con exito","EXITO",{
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
                    
                    setTimeout('cambiarHecho2()',hora2());
                   
                }
                else
                {
                    toastr.error("Ha ocurrido un problema, no se pudo actualizar el stock","ERROR",{
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
                }
            }
        })
    }
} 

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function validarStock()
{
  stock = $('#stock').val()
  console.log(stock)
  var exr = new RegExp("^[0-9,$]");
  if(stock == "")
  {
      $('#stock').focus()
      toastr.error("Debe Ingresar una cantidad para registrar el nuevo stock","ERROR",{
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
        $('#id_edicion').focus()
        toastr.error("Solo puede ingresar numeros en el stock del documento","ERROR",{
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
    if(stock > 0)
  {
      return true;
  }
}