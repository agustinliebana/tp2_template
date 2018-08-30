var intervalId;

function request_data(){
    $.ajax({type: 'GET',
            url:'/refresh',
            data: {}
    })
        .done(function(data){
            if ((data.temperature)&&(data.humidity)&&(data.pressure)&&(data.windspeed)){
                $('#temperatureText').text(data.temperature+" C");
                $('#humidityText').text(data.humidity+" %");
                $('#pressureText').text(data.pressure+" Hpa");
                $('#windspText').text(data.windspeed+" Km/h");
                $('#temperaturePr').text(data.tmpavg+" C");
                $('#humidityPr').text(data.humavg+" %");
                $('#pressurePr').text(data.preavg+" Hpa");
                $('#windspPr').text(data.winavg+" Km/h");
            }
        })
}

$(document).ready(function(){
    wait_time = parseInt($('#sel1').val());
   intervalId = setInterval(request_data, wait_time*1000);
   $('form').on('submit', function(event){
       clearInterval(intervalId);
       wait_time = parseInt($('#sel1').val());
       intervalId = setInterval(request_data, wait_time*1000);
       event.preventDefault();
   })
});
