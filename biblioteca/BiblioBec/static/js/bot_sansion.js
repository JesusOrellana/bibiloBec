window.onload = function calculo()
{
    setTimeout('calcularSancion()', hora());
}


function hora()
{
    horaActual  = new Date();
    horaProgramada  = new Date();
    horaProgramada.setHours(horaActual.getHours());
    horaProgramada.setMinutes(horaActual.getMinutes());
    horaProgramada.setSeconds(horaActual.getSeconds()+1);
    return horaProgramada.getTime() - horaActual.getTime(); 
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

function calcularSancion()
{

    const csrftoken = getCookie('csrftoken');

    lista = []
    cont = 0
    $('#id_ejem option').each(function()
    {
        l = [$(this).attr('data-ej'),$(this).attr('data-rut'),$(this).attr('data-isbn')+'}']
        lista.push(l);
    });
    cont = lista.length;
    console.log(lista);
    $.ajax({
        url: 'http://127.0.0.1:8000/calcular-sansion/',
        method: 'POST',
        data:{
            'moroso[]': lista,
            'cont': cont,
            csrfmiddlewaretoken: csrftoken
        },
        async: false,
        success: function(data){
            console.log(data);
        }
    })
}