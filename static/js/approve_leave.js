$('#leaveform').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    create_post();
});
$(document).on('submit','#leaveform',function(e){
    e.preventDefault();

    $.ajax({
        type:'POST',
        url:url,
        data:{
            leavedate:$('#id_leavedate').val(),
            days:$('#id_days').val(),
            notes:$('#id_notes').val(),
            current_year_days_remaining:$('#id_current_year_days_remaining').val(),
            previous_year_days_remaining:$('#id_previous_year_days_remaining').val(),  
        },
        success:function(){

        }
    });
});
