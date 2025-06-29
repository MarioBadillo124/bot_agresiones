<?php
// Incluir la conexión
include("conexion.php");

// Verificar que los datos hayan sido enviados por POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Recibir los datos del formulario con valores por defecto si no existen
    $username = $_POST['username'] ?? '';
    $correo = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';
    $role = $_POST['role'] ?? '';
    $confirm_password = $_POST['confirm_password'] ?? '';
    $status = $_POST['status'] ?? '';

    // Validar campos obligatorios
    if (!empty($username) && !empty($correo) && !empty($password) && !empty($role)  && !empty($confirm_password) && !empty($status)) {
        
        // Verificar que la contraseña y la confirmación coincidan
        if ($password !== $confirm_password) {
            $status_msg = "password_mismatch";
        } else {

            // Preparar la consulta para insertar
            $stmt = $conn->prepare("INSERT INTO usuarios (usuario, correo, contrasena, rol,  estado) VALUES (?, ?, ?, ?, ?)");
            if ($stmt) {
                $stmt->bind_param("sssss", $username, $correo, $hashed_password, $role,  $status);
                if ($stmt->execute()) {
                    $status_msg = "success";
                } else {
                    $status_msg = "db_error";
                }
                $stmt->close();
            } else {
                $status_msg = "prepare_error";
            }
        }
    } else {
        $status_msg = "empty_fields";
    }
} else {
    $status_msg = "invalid_method";
}

// Cerrar la conexión
$conn->close();

// Redirigir con el resultado
header("Location: ../admin.php?status=$status_msg");
exit();
?>
