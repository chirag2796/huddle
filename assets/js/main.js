let count_patients_to_move_now = new CountUp('num_patients_to_move_now', 23);
let count_keep_as_buffer = new CountUp('num_keep_as_buffer', 56);
let count_patients_to_release = new CountUp('num_patients_to_release', 52);
let count_inbound_transfers = new CountUp('num_inbound_transfers', 56);
let count_outbound_transfers = new CountUp('num_outbound_transfers', 52);

$(document).ready(function(){
    $('.progress-value > span').each(function(){
        $(this).prop('Counter',0).animate({
            Counter: $(this).text()
        },{
            duration: 1500,
            easing: 'swing',
            step: function (now){
                $(this).text(Math.ceil(now));
            }
        });
    });

    $('#main_patient_table').DataTable({
        "scrollY":        "250px",
        "scrollCollapse": true,
        "paging":         false
    });

    count_patients_to_move_now.start();
    count_keep_as_buffer.start();
    count_patients_to_release.start();
    count_inbound_transfers.start();
    count_outbound_transfers.start();
});