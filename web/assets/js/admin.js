document.addEventListener('DOMContentLoaded', function() {
    // Manejar clics en botones de editar y eliminar
    document.querySelectorAll('.btn-edit').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-id');
            // Aquí puedes abrir un modal o redirigir a una página de edición
            alert('Editar usuario ID: ' + userId);
        });
    });

    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-id');
            if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
                // Enviar solicitud AJAX para eliminar
                fetch(`eliminar_usuario.php?id=${userId}`, {
                    method: 'DELETE'
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload();
                    } else {
                        alert('Error al eliminar usuario');
                    }
                });
            }
        });
    });
});