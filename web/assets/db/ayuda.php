<?php
header('Content-Type: application/json');
include("conexion.php");

// Validación básica
$nombre = trim($_POST['nombre'] ?? '');
$email = trim($_POST['email'] ?? '');
$mensaje = trim($_POST['mensaje'] ?? '');

if ($nombre === '' || $email === '' || $mensaje === '') {
    echo json_encode(['success' => false, 'message' => 'Todos los campos son obligatorios.']);
    exit;
}

// Guardar en base de datos
$stmt = $conn->prepare("INSERT INTO mensajes_ayuda (nombre, email, mensaje, fecha_envio) VALUES (?, ?, ?, NOW())");
$stmt->bind_param("sss", $nombre, $email, $mensaje);

if ($stmt->execute()) {
    echo json_encode(['success' => true, 'message' => 'Mensaje enviado correctamente.']);
} else {
    echo json_encode(['success' => false, 'message' => 'Error al guardar en la base de datos.']);
}

$stmt->close();
$conn->close();
?>
