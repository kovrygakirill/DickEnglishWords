function marked_in_red_login_data(e) {
    document.getElementById("username").style.borderColor = 'red';
    document.getElementById("password").style.borderColor = 'red';
}

$(function () {

    $('#login-form-link').click(function (e) {
        $("#login-form").delay(100).fadeIn(100);
        $("#register-form").fadeOut(100);
        $('#register-form-link').removeClass('active');
        $(this).addClass('active');
        e.preventDefault();
    });
    $('#register-form-link').click(function (e) {
        $("#register-form").delay(100).fadeIn(100);
        $("#login-form").fadeOut(100);
        $('#login-form-link').removeClass('active');
        $(this).addClass('active');
        e.preventDefault();
    });

});

function verifyLoginData() {
    var result = true
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username == '') {
        document.getElementById("username").style.borderColor = 'red';
        document.getElementById("label_login_error").style.borderColor = 'red';

        result = false;
    }
    if (password == '') {
        document.getElementById("password").style.borderColor = 'red';
        result = false;
    }
    if (!result) {
        var error = document.getElementById("label_login_error");
        error.innerHTML = 'Fill in the all fields, please!';
    }

    return result
}

