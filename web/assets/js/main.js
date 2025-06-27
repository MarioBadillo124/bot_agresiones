// Funcionalidad común a todas las páginas
document.addEventListener('DOMContentLoaded', function() {
    // Manejar el menú hamburguesa en móviles
    const hamburger = document.createElement('div');
    hamburger.className = 'hamburger-menu';
    hamburger.innerHTML = '<i class="fas fa-bars"></i>';
    
    const sidebar = document.querySelector('.sidebar');
    if (sidebar) {
        document.querySelector('.main-header').prepend(hamburger);
        
        hamburger.addEventListener('click', function() {
            sidebar.classList.toggle('active');
        });
    }
    
    // Manejar notificaciones
    const notificationBell = document.querySelector('.notifications');
    if (notificationBell) {
        notificationBell.addEventListener('click', function() {
            // Aquí iría la lógica para mostrar notificaciones
            alert('Mostrar notificaciones');
        });
    }
    
    // Manejar el cierre de sesión
    const logoutBtn = document.querySelector('.logout');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function(e) {
            e.preventDefault();
            if (confirm('¿Estás seguro de que deseas cerrar sesión?')) {
                window.location.href = 'index.html';
            }
        });
    }
    
    // Mostrar/ocultar contraseña
    const passwordToggles = document.querySelectorAll('.toggle-password');
    passwordToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const input = this.previousElementSibling;
            if (input.type === 'password') {
                input.type = 'text';
                this.innerHTML = '<i class="fas fa-eye-slash"></i>';
            } else {
                input.type = 'password';
                this.innerHTML = '<i class="fas fa-eye"></i>';
            }
        });
    });
});

// Funciones de utilidad
function showAlert(message, type = 'success') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;
    
    document.body.prepend(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// Para la vista en tiempo real (live-view.js)
function initLiveView() {
    // Aquí iría la lógica para conectar con las cámaras
    console.log('Inicializando vista en tiempo real');
    
    // Simulación de actualización de estado
    setInterval(() => {
        const statusIndicators = document.querySelectorAll('.camera-status');
        statusIndicators.forEach(indicator => {
            // Simular cambios aleatorios de estado
            if (Math.random() > 0.9) {
                indicator.classList.toggle('warning');
            }
        });
    }, 5000);
}

// Para los gráficos (chart.js)
function initCharts() {
    // Inicialización de gráficos con Chart.js
    console.log('Inicializando gráficos');
    
    // Ejemplo de gráfico
    const ctx = document.getElementById('typeChart');
    if (ctx) {
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Agresión', 'Bullying', 'Vandalismo', 'Sospechoso'],
                datasets: [{
                    label: 'Incidentes por Tipo',
                    data: [12, 8, 3, 5],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.7)',
                        'rgba(54, 162, 235, 0.7)',
                        'rgba(255, 206, 86, 0.7)',
                        'rgba(75, 192, 192, 0.7)'
                    ]
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
}