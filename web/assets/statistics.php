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
    <title>Estadísticas - Sistema de Monitoreo</title>
    <link rel="stylesheet" href="css/estilos_barra_menu.css">
    <link rel="stylesheet" href="css/estadisticas.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="dashboard">
        <!-- Sidebar (igual que en dashboard.html) -->
        <!-- ... -->
        
        <!-- Main Content -->
        <div class="main-content">
            <header>
                <div class="superior">
                    <div class="search">
                        <br><h1>Historial de incidentes</h1><br>
                    </div>
                </div>

                <div class="container__menu">
                    <nav>
                        <ul>
                            <li><a href="menu.php"></a></li>
                            <li><a href="live-view.php" >Vista en tiempo real</a></li>
                            <li><a href="incidents.php" >Historico de incidentes</a></li>
                            <li><a href="" id="selected">Estadisticas</a></li>
                            <li><a href="admin.php" >Administracion</a></li>
                            <li><a href="ayuda.php" >Ayuda</a></li>
                            <li><a href="db/logout.php">Cerrar sesión</a></li>
                        </ul>
                    </nav>
                </div>
            </header><br>
            
                <div class="header-actions">
                    <div class="period-selector">
                        <select id="periodSelect">
                            <option value="day">Hoy</option>
                            <option value="week">Esta Semana</option>
                            <option value="month" selected>Este Mes</option>
                            <option value="year">Este Año</option>
                        </select>
                    </div>
                    <button class="btn btn-primary" id="generateReportBtn">
                        <i class="fas fa-file-pdf"></i> Generar Reporte
                    </button>
                </div>

            <div id="reportContent">
                <div class="content">
                    <div class="stats-grid">
                        <div class="stat-card big">
                            <h2>Resumen General</h2>
                            <div class="stat-row">
                                <div class="stat-item">
                                    <h3>Total Incidentes</h3>
                                    <p class="stat-number">24</p>
                                    <p class="stat-change up"><i class="fas fa-arrow-up"></i> 12% vs mes anterior</p>
                                </div>
                                <div class="stat-item">
                                    <h3>Resueltos</h3>
                                    <p class="stat-number">18</p>
                                    <p class="stat-change up"><i class="fas fa-arrow-up"></i> 8% vs mes anterior</p>
                                </div>
                                <div class="stat-item">
                                    <h3>Pendientes</h3>
                                    <p class="stat-number">6</p>
                                    <p class="stat-change down"><i class="fas fa-arrow-down"></i> 4% vs mes anterior</p>
                                </div>
                            </div>
                        </div>
                        
                        <div class="stat-card">
                            <h2>Incidentes por Tipo</h2>
                            <canvas id="typeChart"></canvas>
                        </div>
                        
                        <div class="stat-card">
                            <h2>Incidentes por Ubicación</h2>
                            <canvas id="locationChart"></canvas>
                        </div>
                        
                        <div class="stat-card">
                            <h2>Incidentes por Hora del Día</h2>
                            <canvas id="hourChart"></canvas>
                        </div>
                        
                        <div class="stat-card big">
                            <h2>Tendencia Mensual</h2>
                            <canvas id="trendChart"></canvas>
                        </div>
                        
                        <div class="stat-card">
                            <h2>Severidad de Incidentes</h2>
                            <canvas id="severityChart"></canvas>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <script src="chart.js"></script>
    <script src="js/graficas.js"></script>
    <script>

        // Si se navega hacia atrás, forzar recarga de la página
        window.addEventListener("pageshow", function (event) {
            if (event.persisted || (window.performance && window.performance.navigation.type === 2)) {
                // Esta página fue mostrada desde la caché (por botón atrás)
                window.location.reload(); // Fuerza recarga para que el PHP redirija si no hay sesión
            }
        });
    </script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>


</body>
</html>