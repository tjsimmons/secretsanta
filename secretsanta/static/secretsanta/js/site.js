$(document).ready(function() {
    $("#person").change(function(e) {
        $.get("check_person/" + $(this).val(), function(data) {
            if (data.found) {
                $("#sec").show();
            } else {
                $("#sec").hide();
            }
        });
    });
});
