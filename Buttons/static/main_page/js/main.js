async function timer(){
    let input = document.getElementById('input_timer');
    let starter = document.getElementById('starter_timer');
    let stopper = document.getElementById('stopper_timer')
    let ticker = document.getElementById('ticker_timer');
    let time

    starter.addEventListener('click', function(){
        time = parseInt(input.value)- 1
        // || time/60 >= 1441
        if (isNaN(time) ){
            alert('wrong input or time more than 24h');
            return 0
        }

        starter.style['visibility'] = 'collapse';
        stopper.style['visibility'] = 'visible';

        timer = setInterval(function(){
            seconds = time%60;
            minutes = time/60%60;
            hours = time/3600%60;

            if (time <= 0){
                clearInterval(timer);
                alert('Time has passed...');
                document.location.reload();
            }
            else{
                let strTime = `${Math.trunc(hours)}:
                                ${Math.trunc(minutes)}:
                                ${Math.trunc(seconds)}`;
                ticker.innerHTML = strTime;
            }
            --time;
        }, 1440)
        }
    );
    stopper.addEventListener('click', function(){
        clearInterval(timer);
        alert('Timer stopped');
        starter.style['visibility'] = 'visible';
        stopper.style['visibility'] = 'collapse';
        document.location.reload();
    })
}

timer()