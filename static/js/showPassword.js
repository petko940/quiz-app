document.addEventListener("DOMContentLoaded", function () {
    const passwordId = document.getElementById("logpass");
    const togglePassword = document.getElementById("togglePassword");
 
    togglePassword.addEventListener("click", function () {
        if (passwordId.type === "password") {
            passwordId.type = "text";
            togglePassword.innerHTML = '<i class="fas fa-eye-slash" aria-hidden="true"></i>';
        } else {
            passwordId.type = "password";
            togglePassword.innerHTML = '<i class="fas fa-eye" aria-hidden="true"></i>';
        }
    });
});
