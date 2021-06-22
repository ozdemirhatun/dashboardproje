$(document).ready(function() {
    // bind the form submit event to our function
    $("#loginForm").bind('submit', function(e) {
        // prevent page refresh
        e.preventDefault();
        // post the data
        var ajax=$.ajax({
            type: "POST",
            data: $("#loginForm").serialize(),
            url: "http://localhost:5000/"
        }).done(function(login){
            console.log('done!')
        });
        ajax.fail(function(login){
            console.log('error!');
        });
    });
});