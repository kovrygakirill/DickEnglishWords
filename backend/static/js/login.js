$(document).ready(function () {
    var register_page = document.getElementById("register_label_error");
    var register_value = register_page == null ? "" : register_page.innerHTML;
    if (register_value) {
        $("#register-form-link").trigger("click");
    } else {
        $("#login-form-link").trigger("click");
    }
});

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

function change_url_on_login(e) {
    const nextTitle = '';
    const nextState = {};
    const nextURL = 'http://' + e.host + '/auth/login/';
    window.history.replaceState(nextState, nextTitle, nextURL);
}

function change_url_on_register(e) {
    const nextTitle = '';
    const nextState = {};
    const nextURL = 'http://' + e.host + '/auth/register/';
    window.history.replaceState(nextState, nextTitle, nextURL);
}

function marked_in_red_login_data() {
    document.getElementById("login_username").style.borderColor = "red";
    document.getElementById("login_password").style.borderColor = "red";
}

function verifyLoginData(e) {
    var result = true
    var username = e.username.value;
    var password = e.password.value;

    if (username == '') {
        document.getElementById("login_username").style.borderColor = "red";
        result = false;
    }
    if (password == '') {
        document.getElementById("login_password").style.borderColor = "red";
        result = false;
    }
    if (!result) {
        // var ffd= $("#"+e.id+'label[id="label_error"]');
        document.getElementById("login_label_error").innerHTML = 'Fill in the all fields, please!';
        appearBlockLoginError();
        disappearBlockRegisterSuccess();
    }

    return result
}

function marked_in_red_register_data() {
    document.getElementById("register_username").style.borderColor = 'red';
    document.getElementById("register_email").style.borderColor = 'red';
    document.getElementById("register_password").style.borderColor = 'red';
    document.getElementById("register_confirm_password").style.borderColor = 'red';
}

function check_fill_in_data(username, email, password_1, password_2) {
    var result = true
    if (username == '') {
        document.getElementById("register_username").style.borderColor = 'red';
        result = false;
    }
    if (email == '') {
        document.getElementById("register_email").style.borderColor = 'red';
        result = false;
    }
    if (password_1 == '') {
        document.getElementById("register_password").style.borderColor = 'red';
        result = false;
    }
    if (password_2 == '') {
        document.getElementById("register_confirm_password").style.borderColor = 'red';
        result = false;
    }
    return result
}

function validateEmail(email) {
    return String(email)
        .toLowerCase()
        .match(
            /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
        );
}

function verifyRegisterData(e) {
    var result = true;
    var username = e.username.value;
    var email = e.email.value;
    var password_1 = e.password.value;
    var password_2 = e.confirm_password.value;
    var error = document.getElementById("register_label_error");

    if (!check_fill_in_data(username, email, password_1, password_2)) {
        error.innerHTML = 'Fill in the all fields, please!';
        result = false;
    } else if (password_1 != password_2) {
        document.getElementById("register_password").style.borderColor = 'red';
        document.getElementById("register_confirm_password").style.borderColor = 'red';
        error.innerHTML = 'Confirm password doesnt match';
        result = false;
    }
    validateEmail(email);

    if (!result){
        appearBlockLoginError();
        disappearBlockRegisterSuccess();
    }

    return result
}

function disappearBlockLoginError() {
    var elems = document.getElementsByClassName('error');
    for (var i = 0; i < elems.length; i++) {
        elems[i].style.display = "none";
    }
}

function appearBlockLoginError() {
    var elems = document.getElementsByClassName('error');
    for (var i = 0; i < elems.length; i++) {
        elems[i].style.display = "block";
    }
}

function disappearBlockRegisterSuccess() {
    var elems = document.getElementsByClassName('successful');
    for (var i = 0; i < elems.length; i++) {
        elems[i].style.display = "none";
    }
}


