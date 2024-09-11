function formValidation (form) {
    if (form.username.value == "") {
        alert("Error: Username cannot be empty");
        form.username.focus();
        return false;
    }

    if (form.password.value != "") {
        if (form.password.value.length < 8) {
            alert("Error: Password must have at least 8 characters");
            form.password.focus();
            return false;
        }

        if (form.password.value == form.username.value) {
            alert("Error: Password cannot be equal username");
            form.password.focus();
            return false;
        }

        temp = /[0-9]/;
        if (!temp.test(form.password.value)) {
            alert("Error: Password must have at least one number");
            form.password.focus();
            return false;
        }

        temp = /[a-z]/;
        if (!temp.test(form.password.value)) {
            alert("Error: Password must have at least one character (a-z)");
            form.password.focus();
            return false;
        }

        temp = /[A-Z]/;
        if (!temp.test(form.password.value)) {
            alert("Error: Password must have at least one character (A-Z)");
            form.password.focus();
            return false;
        }

    } else {
        alert("Error: Please check you have entered your password");
        form.password.focus();
        return false;
    }

    alert("Sign up successful");
    return true;
}