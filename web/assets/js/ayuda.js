document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contactForm');
    const msg = document.getElementById('formMessage');

    form.addEventListener('submit', function (e) {
        e.preventDefault(); // Evita que se recargue la página
        const formData = new FormData(form);

        fetch('db/ayuda.php', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            msg.style.color = data.success ? 'green' : 'red';
            msg.textContent = data.message;

            if (data.success) {
                form.reset(); // Limpia el formulario
            }
        })
        .catch(() => {
            msg.style.color = 'red';
            msg.textContent = 'Error al enviar el mensaje.';
        });
    });
});
