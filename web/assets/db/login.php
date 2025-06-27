<?php
// Incluir la conexión
require 'conexion.php';

session_start(); // Iniciar la sesión

if (isset($_POST['login'])) {
    // Obtener los valores enviados por el formulario
    $userr = $_POST['user'];
    $contrasena = $_POST['pass'];

    // Proteger los datos contra inyecciones SQL
    $userr = mysqli_real_escape_string($conexion, $userr);
    $contrasena = mysqli_real_escape_string($conexion, $contrasena);

    // Ejecutamos la consulta para verificar las credenciales
    $sql = "SELECT * FROM usuarios WHERE usuario = '$userr' AND contrasena = '$contrasena'";
    $resultado = mysqli_query($conexion, $sql);

    if (mysqli_num_rows($resultado) > 0) {
        // Credenciales válidas: establecer variables de sesión
        $usuario_data = mysqli_fetch_assoc($resultado);
        $_SESSION['user_id'] = $usuario_data['id']; // ID único del usuario
        $_SESSION['user_name'] = $usuario_data['usuario']; // Nombre del usuario

        // Redirigir al menú principal
        header("Location: ../menu.html");
        exit();
    } else {
        // Credenciales inválidas: redirigir con un mensaje de error
        header("Location: ../index.html?status=invalid_credentials");
        exit();
    }
}

// Cerrar la conexión
mysqli_close($conexion);
?>
