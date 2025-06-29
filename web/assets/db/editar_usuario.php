<?php
include("conexion.php");

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $id = intval($_POST['id']);
    $username = $_POST['username'] ?? '';
    $correo = $_POST['correo'] ?? '';
    $role = $_POST['role'] ?? '';
    $status = $_POST['status'] ?? '';

    if (!empty($username) && !empty($correo) && !empty($role) && !empty($status)) {
        $stmt = $conn->prepare("UPDATE usuarios SET usuario=?, correo=?, rol=?, estado=? WHERE id=?");
        $stmt->bind_param("ssssi", $username, $correo, $role, $status, $id);
        if ($stmt->execute()) {
            $status_msg = "updated";
        } else {
            $status_msg = "update_error";
        }
        $stmt->close();
    } else {
        $status_msg = "empty_fields";
    }
} else {
    $status_msg = "invalid_method";
}

$conn->close();
header("Location: ../admin.php?status=$status_msg");
exit();
?>
