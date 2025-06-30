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
    <title>Vista en Tiempo Real - Sistema de Monitoreo</title>
    <link rel="stylesheet" href="css/estilos_barra_menu.css">
    <link rel="stylesheet" href="css/live-view.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
</head>
<body>

    <header>
        <div class="superior">
            <div class="search">
                <br><h1>Vista en tiempo reals</h1><br>
            </div>
        </div>

        <div class="container__menu">
            <nav>
                <ul>
                    <li><a href="menu.php"></a></li>
                    <li><a href="" id="selected">Vista en tiempo real</a></li>
                    <li><a href="incidents.php" >Historico de incidentes</a></li>
                    <li><a href="statistics.php" >Estadisticas</a></li>
                    <li><a href="admin.php" >Administracion</a></li>
                    <li><a href="ayuda.php" >Ayuda</a></li>
                    <li><a href="db/logout.php">Cerrar sesión</a></li>
                </ul>
            </nav>
        </div>
    </header><br>

    <div class="dashboard">
        <!-- Sidebar (igual que en dashboard.html) -->
        <!-- ... -->
        
        <!-- Main Content -->
        <div class="main-content">
            
            
            <div class="content">
                <div class="camera-grid">
                    <div class="camera-view">
                        <div class="camera-header">
                            <h3>Patio Principal</h3>
                            <span class="camera-status active"><i class="fas fa-circle"></i> Activa</span>
                        </div>
                        <div class="video-container">
                            <video id="cameraPatio" class="live-feed" autoplay playsinline muted></video>
                            <div class="video-overlay">
                                <button class="btn-overlay"><i class="fas fa-expand"></i></button>
                                <button class="btn-overlay"><i class="fas fa-volume-up"></i></button>
                            </div>
                        </div>

                        <div class="camera-controls">
                            <button class="btn-control"><i class="fas fa-pause"></i></button>
                            <button class="btn-control"><i class="fas fa-camera"></i></button>
                            <button class="btn-control"><i class="fas fa-record-vinyl"></i></button>
                        </div>
                    </div>
                    
                    
                    <!-- Más cámaras según sea necesario -->
                </div>
                
                <div class="alert-panel">
                    <div class="panel-header">
                        <h2>Alertas Automáticas</h2>
                        <div class="alert-toggle">
                            <span>Notificaciones: </span>
                            <label class="switch">
                                <input type="checkbox" checked>
                                <span class="slider round"></span>
                            </label>
                        </div>
                    </div>
                    <div class="panel-body">
                        <div class="alert-item">
                            <div class="alert-time">10:15 AM</div>
                            <div class="alert-content">
                                <strong>Posible agresión detectada</strong> en Patio Principal
                                <p>Confianza del sistema: 92%</p>
                            </div>
                            <button class="btn-alert">Ver</button>
                        </div>
                        
                        <div class="alert-item">
                            <div class="alert-time">09:30 AM</div>
                            <div class="alert-content">
                                <strong>Actividad sospechosa</strong> en Entrada Principal
                                <p>Confianza del sistema: 85%</p>
                            </div>
                            <button class="btn-alert">Ver</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="js/live-view.js"></script>
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
</body>
</html>