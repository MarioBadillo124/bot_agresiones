<?php
include("conexion.php");

if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    
    $stmt = $conn->prepare("DELETE FROM usuarios WHERE id = ?");
    $stmt->bind_param("i", $id);
    if ($stmt->execute()) {
        $status = "deleted";
    } else {
        $status = "delete_error";
    }
    $stmt->close();
    $conn->close();
    
    header("Location: ../admin.php?status=$status");
    exit();
} else {
    header("Location: ../admin.php?status=invalid_id");
    exit();
}
?>
