<?php
session_start();
if (!isset($_SESSION['user_id'])) {
    header("Location: ../../index.html");
    exit();
}

// Evitar que el navegador guarde en caché la página
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Cache-Control: post-check=0, pre-check=0", false);
header("Pragma: no-cache");
?>


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayuda - Sistema de Monitoreo</title>
    <link rel="stylesheet" href="css/estilos_barra_menu.css">
    <link rel="stylesheet" href="css/ayuda.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
</head>
<body>

    <header>
        <div class="superior">
            <div class="search">
                <br><h1>Centro de Ayuda</h1><br>
            </div>
        </div>
        <div class="container__menu">
            <nav>
                <ul>
                <li><a href="menu.php"></a></li>
                <li><a href="live-view.php">Vista en tiempo real</a></li>
                <li><a href="incidents.php">Histórico de incidentes</a></li>
                <li><a href="statistics.php">Estadísticas</a></li>
                <li><a href="admin.php">Administración</a></li>
                <li><a href="" id="selected">Ayuda</a></li>
                <li><a href="db/logout.php">Cerrar sesión</a></li>
                </ul>
            </nav>
        </div>
    </header><br>

    <main class="ayuda-container">
        <section class="manuales">
            <h2><i class="fas fa-book"></i> Manuales</h2>
            <div class="manual-links">
                <a href="docs/manual_de_usuario.pdf" download class="btn-manual">
                    <i class="fas fa-file-download"></i> Descargar Manual de Usuario
                </a>
                <a href="docs/manual_tecnico.pdf" download class="btn-manual">
                    <i class="fas fa-file-download"></i> Descargar Manual Técnico
                </a>
            </div>
        </section>

        <section class="chatbot">
            <h2><i class="fab fa-telegram"></i> Chat de Soporte</h2>
            <p>Si tienes dudas o problemas, puedes contactar al asistente virtual:</p>
            <a href="https://web.telegram.org/a/#7957581596" target="_blank" class="btn-chatbot">
                <i class="fab fa-telegram"></i> Ir al Chatbot en Telegram
            </a>
        </section>

        <div class="contact-form">
            <h2>Contáctanos</h2>
            <form id="contactForm">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required>

                <label for="email">Correo:</label>
                <input type="email" id="email" name="email" required>

                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="mensaje" rows="5" required></textarea>

                <button type="submit">Enviar Mensaje</button>
                <div id="formMessage" class="form-message"></div>
            </form>
        </div>
    </main>


    <!-- Tus scripts si tienes más -->
    <script>
        // Si se navega hacia atrás, forzar recarga de la página
        window.addEventListener("pageshow", function (event) {
            if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
                // Esta página fue mostrada desde la caché (por botón atrás)
                window.location.reload(); // Fuerza recarga para que el PHP redirija si no hay sesión
            }
        });
    </script>

    <script src="js/login_modal.js"></script>
    <script src="js/ayuda.js"></script>

</body>
</html>
