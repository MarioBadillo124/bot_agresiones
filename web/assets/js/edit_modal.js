// Abrir el modal
document.querySelectorAll('.btn-edit').forEach(button => {
    button.addEventListener('click', function () {
        const modal = document.getElementById('editModal');

        document.getElementById('edit_id').value = this.dataset.id;
        document.getElementById('edit_username').value = this.dataset.usuario;
        document.getElementById('edit_correo').value = this.dataset.correo;
        document.getElementById('edit_role').value = this.dataset.rol;
        document.getElementById('edit_estado').value = this.dataset.estado;

        modal.style.display = 'flex'; // OJO: flex para centrarlo
    });
});

// Cerrar el modal con la X
document.querySelector('.modal .close').addEventListener('click', () => {
    document.getElementById('editModal').style.display = 'none';
});

// Cerrar haciendo clic fuera del modal
window.addEventListener('click', event => {
    const modal = document.getElementById('editModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});
