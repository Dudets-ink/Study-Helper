$(function(){
     async function timer(){
        let input = $('#input-timer');
        let starter = $('#starter-timer');
        let stopper = $('#stopper-timer')
        let ticker = $('#ticker-timer');
        let time

        starter.click(function(){
            time = parseInt(input.val())- 1;
            // || time/60 >= 1441
            if (isNaN(time) ){
                alert('wrong input');
                return 0
            }

            starter.hide(1000);
            stopper.show(1000);

            intervalTimer = setInterval(function(){
                seconds = time%60;
                minutes = time/60%60;
                hours = time/3600%60;

                if (time <= 0){
                    clearInterval(intervalTimer);
                    alert('Time has passed...');
                    document.location.reload(); // место ajax
                }
                else{
                    let strTime = `${Math.trunc(hours)}:
                                    ${Math.trunc(minutes)}:
                                    ${Math.trunc(seconds)}`;
                    ticker.html(strTime);     
                }
                --time;
            }, 1000)
            }
        );
        stopper.click(function(){
            clearInterval(intervalTimer);
            alert('Timer stopped');
            starter.show(1000);
            stopper.hide(1000);
            $.ajax({
                type:'GET',
                cache:false, 
                success: function(){
                    $("#ticker-timer").load(location.href + " #ticker-timer>*", "");
            }
        });
        })
    };

    async function toDoList(){
        let input = $('#input-note');
        let deleteButton = $('#delete-note');
        let form = $("#form-list")
        let notes = $('#notes');
        let note = $("<li></li>");

        form.submit(function(event){
            event.preventDefault()

            if (input.val().trim()){
                let val = input.val()
                val = val.replace(/\s/g, '_')
                console.log(val)
                note.html(val);
                note.addClass("note");  
                if ($("#notes li").last().attr('id') != undefined) {
                    id = $("#notes li").last().attr('id').split('-')[1] 
                    note.attr('id', `note-${parseInt(id)+1}`);
                }else {
                    note.attr('id', 'note-1');  
                };
                // notes.append(note);
                $.ajax({
                    type:'POST',
                    data: {"noteVal":note.html(), "noteId":note.attr('id')},
                    success: function(){
                        $("#notes").load(location.href + " #notes>*", "");
                    }
                }).done(function(){
                    input.val('');
                })
            } else {
                alert('Wrong input...')
            }
            });
    }

    timer()
    toDoList()
});