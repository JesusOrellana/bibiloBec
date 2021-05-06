
$(document).ready(function() {

  $('#id_tipo_documento_id_tipo_doc').prop('class','form-control')
  $('#id_categoria_id_cate').prop('class','form-control')
  $('#id_tipo_medio').prop('class','form-control')
  t_doc = $('#t_doc').val()
  $("#id_tipo_documento_id_tipo_doc option[value="+t_doc+"]").attr("selected",true);
  t_cat = $('#t_cat').val()
  $("#id_categoria_id_cate option[value="+t_cat+"]").attr("selected",true);
  t_med = $('#t_med').val()
  $("#id_tipo_medio option[value="+t_med+"]").attr("selected",true);

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