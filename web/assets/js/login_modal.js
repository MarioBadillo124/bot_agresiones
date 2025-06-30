document.addEventListener("DOMContentLoaded", function () {
    const modal = document.getElementById("loginErrorModal");
    const span = document.querySelector(".modal .close");

    // Detecta si viene con ?error=1 en la URL
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('error') === '1') {
        modal.style.display = "block";
    }

    // Cierra el modal
    span.onclick = function () {
        modal.style.display = "none";
    }

    // Cierra el modal si se hace clic fuera del contenido
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
