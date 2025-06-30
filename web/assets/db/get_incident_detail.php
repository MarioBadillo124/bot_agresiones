<?php
include 'conexion.php';

if (!isset($_GET['id'])) {
    echo json_encode(['error' => 'Falta el ID del incidente']);
    exit;
}

$id = intval($_GET['id']);

$sql = "SELECT fecha, hora, ubicacion, tipo, severidad, estado, descripcion, acciones_tomadas FROM incidentes WHERE id = $id";
$result = mysqli_query($conn, $sql);

if (!$result || mysqli_num_rows($result) == 0) {
    echo json_encode(['error' => 'Incidente no encontrado']);
    exit;
}

$incident = mysqli_fetch_assoc($result);

mysqli_close($conn);

echo json_encode($incident);
?>
