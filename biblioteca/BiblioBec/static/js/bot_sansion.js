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
    horaProgramada.setSeconds(horaActual.getSeconds()+10);
    return horaProgramada.getTime() - horaActual.getTime(); 
}

function calcularSancion()
{
    lista = []
    $('#id_ejem option').each(function()
    {
        l = [$(this).attr('data-ej'),$(this).attr('data-rut'),$(this).attr('data-isbn')]
        lista.push(l);
    });
    console.log(lista);
    $.ajax({
        url: '/producto/data',
        method: 'POST',
        data:{
            moroso: lista
            //id:1,
            //_token:$('input[name="_token"]').val()
        }
    }).done(function(res){
        
        var lista = JSON.parse(res);
        for (var index = 0; index < lista.length; index++) {
            nombres.push(lista[index].nombre);
            stock.push(lista[index].rebaje);

        }
        alert(nombres);
        alert(stock)
        generarGrafico();
        generarGraficoCir();
        generarGraficoLine();
    })

}