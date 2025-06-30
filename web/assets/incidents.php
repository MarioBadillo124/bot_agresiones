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

include 'db/conexion.php';  // Ajusta la ruta si es necesario

$start = isset($_GET['startDate']) ? $_GET['startDate'] : null;
$end = isset($_GET['endDate']) ? $_GET['endDate'] : null;

// Base de la consulta
$sql = "SELECT id, fecha, hora, ubicacion, tipo, severidad, estado FROM incidentes";

// Si vienen fechas, agregamos filtro
if ($start && $end) {
    $sql .= " WHERE fecha BETWEEN '$start' AND '$end'";
}

// Ordenamos primero por fecha y luego por hora descendente
$sql .= " ORDER BY fecha DESC, hora DESC";

$resultado = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Histórico de Incidentes - Sistema de Monitoreo</title>
    <link rel="stylesheet" href="css/estilos_barra_menu.css">
    <link rel="stylesheet" href="css/historial.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.11.3/css/jquery.dataTables.min.css">
</head>
<body>

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
                    <li><a href="" id="selected">Historico de incidentes</a></li>
                    <li><a href="statistics.php" >Estadisticas</a></li>
                    <li><a href="admin.php" >Administracion</a></li>
                    <li><a href="ayuda.php" >Ayuda</a></li>
                    <li><a href="db/logout.php">Cerrar sesión</a></li>

                </ul>
            </nav>
        </div>
    </header><br>

    <div class="dashboard">
        
        <!-- Main Content -->
        <div class="main-content">
            
                <div class="header-actions">
                    <div class="date-filter">
                        <form method="GET" action="" class="date-filter">
                            <input type="date" name="startDate" id="startDate" value="<?= isset($_GET['startDate']) ? htmlspecialchars($_GET['startDate']) : '' ?>">
                            <span>a</span>
                            <input type="date" name="endDate" id="endDate" value="<?= isset($_GET['endDate']) ? htmlspecialchars($_GET['endDate']) : '' ?>">
                            <button type="submit" class="btn-filter">Filtrar</button>
                        </form>
                    </div>
                    <button class="btn btn-primary" id="exportBtn">
                        <i class="fas fa-file-export"></i> Exportar
                    </button>
                </div>
            
            <div class="content">
                <div class="incidents-table-container">
                    <table id="incidentsTable" class="display">
                        <thead>
                            <tr>
                                <th>Fecha</th>
                                <th>Hora</th>
                                <th>Ubicación</th>
                                <th>Tipo</th>
                                <th>Severidad</th>
                                <th>Estado</th>
                                <th>Acciones</th>
                            </tr>
                        </thead>
                        <tbody>
                            <?php
                            if (!$resultado) {
                                echo '<tr><td colspan="7">Error en la consulta: ' . mysqli_error($conn) . '</td></tr>';
                            } elseif (mysqli_num_rows($resultado) > 0) {
                                while ($fila = mysqli_fetch_assoc($resultado)) {
                                    $sevClass = '';
                                    switch (strtolower($fila["severidad"])) {
                                        case 'alta': $sevClass = 'severity-high'; break;
                                        case 'media': $sevClass = 'severity-medium'; break;
                                        case 'baja': $sevClass = 'severity-low'; break;
                                    }
                                    $estadoClass = strtolower($fila["estado"]) === 'resuelto' ? 'status-resolved' : 'status-pending';

                                    echo "<tr>";
                                    echo "<td>" . htmlspecialchars($fila["fecha"]) . "</td>";
                                    echo "<td>" . htmlspecialchars($fila["hora"]) . "</td>";
                                    echo "<td>" . htmlspecialchars($fila["ubicacion"]) . "</td>";
                                    echo "<td>" . htmlspecialchars($fila["tipo"]) . "</td>";
                                    echo "<td><span class='$sevClass'>" . htmlspecialchars($fila["severidad"]) . "</span></td>";
                                    echo "<td><span class='$estadoClass'>" . htmlspecialchars($fila["estado"]) . "</span></td>";
                                    echo "<td>
                                            <button class='btn-action view' data-id='" . $fila["id"] . "'><i class='fas fa-eye'></i></button>
                                            <button class='btn-action download'><i class='fas fa-download'></i></button>
                                          </td>";
                                    echo "</tr>";
                                }
                            } else {
                                echo '<tr><td colspan="7">No hay incidentes registrados.</td></tr>';
                            }
                            ?>
                        </tbody>
                    </table>
                </div>
                
                <div class="incident-detail-modal" id="detailModal">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h2>Detalles del Incidente</h2>
                            <button class="close-modal">&times;</button>
                        </div>
                        <div class="modal-body">
                            <div class="video-container">
                                <video controls>
                                    <source src="videos/1.mp4" type="video/mp4">
                                    Tu navegador no soporta videos HTML5.
                                </video>
                            </div>
                            <div class="incident-info">
                                <h3>Información del Incidente</h3>
                                <div class="info-grid">
                                    <div class="info-item">
                                        <label>Fecha y Hora:</label>
                                        <p>2025-06-29 10:15:23</p>
                                    </div>
                                    <div class="info-item">
                                        <label>Ubicación:</label>
                                        <p>Patio Principal</p>
                                    </div>
                                    <div class="info-item">
                                        <label>Tipo:</label>
                                        <p>Agresión Física</p>
                                    </div>
                                    <div class="info-item">
                                        <label>Severidad:</label>
                                        <p class="severity-high">Alta</p>
                                    </div>
                                    <div class="info-item">
                                        <label>Estado:</label>
                                        <p class="status-resolved">Resuelto</p>
                                    </div>
                                    <div class="info-item full-width">
                                        <label>Descripción:</label>
                                        <p>El sistema detectó una posible agresión física entre dos estudiantes en el área del patio principal.</p>
                                    </div>
                                    <div class="info-item full-width">
                                        <label>Acciones Tomadas:</label>
                                        <textarea>Se intervino inmediatamente y se reportó a los padres de los estudiantes involucrados.</textarea>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-secondary close-modal">Cerrar</button>
                            <button class="btn btn-primary">Guardar Cambios</button>
                            <button class="btn btn-danger">Eliminar Incidente</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.3/js/jquery.dataTables.min.js"></script>
    <script src="js/main.js"></script>
    <script src="js/descarga.js"></script>

    <script>
        $(document).ready(function() {
            // Inicializar DataTable

            // Abrir modal y cargar datos dinámicos
            $(document).on('click', '.btn-action.view', function() {
                const id = $(this).data('id');
                $.ajax({
                    url: 'db/get_incident_detail.php',
                    method: 'GET',
                    data: { id },
                    dataType: 'json',
                    success: function(data) {
                        if(data.error) {
                            alert(data.error);
                            return;
                        }
                        // Llenar el modal con los datos del incidente
                        const sevClass = {
                            'alta': 'severity-high',
                            'media': 'severity-medium',
                            'baja': 'severity-low'
                        }[data.severidad.toLowerCase()] || '';

                        const estadoClass = (data.estado.toLowerCase() === 'resuelto') ? 'status-resolved' : 'status-pending';

                        $('#detailModal .info-grid').html(`
                            <div class="info-item">
                                <label>Fecha:</label>
                                <p>${data.fecha}</p>
                            </div>
                            <div class="info-item">
                                <label>Hora:</label>
                                <p>${data.hora}</p>
                            </div>
                            <div class="info-item">
                                <label>Ubicación:</label>
                                <p>${data.ubicacion}</p>
                            </div>
                            <div class="info-item">
                                <label>Tipo:</label>
                                <p>${data.tipo}</p>
                            </div>
                            <div class="info-item">
                                <label>Severidad:</label>
                                <p class="${sevClass}">${data.severidad}</p>
                            </div>
                            <div class="info-item">
                                <label>Estado:</label>
                                <p class="${estadoClass}">${data.estado}</p>
                            </div>
                            <div class="info-item full-width">
                                <label>Descripción:</label>
                                <p>${data.descripcion || 'N/A'}</p>
                            </div>
                            <div class="info-item full-width">
                                <label>Acciones Tomadas:</label>
                                <textarea readonly>${data.acciones_tomadas || ''}</textarea>
                            </div>
                        `);

                        $('#detailModal').fadeIn();
                    },
                    error: function() {
                        alert('Error al obtener los detalles del incidente.');
                    }
                });
            });

            // Cerrar modal
            $('.close-modal').click(function() {
                $('#detailModal').fadeOut();
            });
        });


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