<?php
include 'conexion.php';
header("Content-Type: text/html; charset=UTF-8");

$start = isset($_GET['start']) ? $_GET['start'] : null;
$end = isset($_GET['end']) ? $_GET['end'] : null;

$sql = "SELECT id, fecha, hora, ubicacion, tipo, severidad, estado FROM incidentes";

if ($start && $end) {
    // Filtrar usando la columna 'fecha' que es DATE
    $sql .= " WHERE fecha BETWEEN '$start' AND '$end'";
}

$sql .= " ORDER BY fecha DESC, hora DESC";

$resultado = mysqli_query($conn, $sql);

if (mysqli_num_rows($resultado) > 0) {
    while ($fila = mysqli_fetch_assoc($resultado)) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($fila["fecha"]) . "</td>";
        echo "<td>" . htmlspecialchars($fila["hora"]) . "</td>";
        echo "<td>" . htmlspecialchars($fila["ubicacion"]) . "</td>";
        echo "<td>" . htmlspecialchars($fila["tipo"]) . "</td>";

        $sevClass = '';
        switch (strtolower($fila["severidad"])) {
            case 'alta': $sevClass = 'severity-high'; break;
            case 'media': $sevClass = 'severity-medium'; break;
            case 'baja': $sevClass = 'severity-low'; break;
        }
        echo "<td><span class='$sevClass'>" . htmlspecialchars($fila["severidad"]) . "</span></td>";

        $estadoClass = strtolower($fila["estado"]) === 'resuelto' ? 'status-resolved' : 'status-pending';
        echo "<td><span class='$estadoClass'>" . htmlspecialchars($fila["estado"]) . "</span></td>";

        echo "<td>
                <button class='btn-action view' data-id='{$fila["id"]}'><i class='fas fa-eye'></i></button>
                <button class='btn-action download'><i class='fas fa-download'></i></button>
              </td>";
        echo "</tr>";
    }
} else {
    echo "<tr><td colspan='7'>No hay incidentes registrados.</td></tr>";
}

mysqli_close($conn);
?>
