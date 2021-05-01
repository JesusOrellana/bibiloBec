
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