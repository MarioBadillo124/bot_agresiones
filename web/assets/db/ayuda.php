<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $nombre = htmlspecialchars(trim($_POST['nombre']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $mensaje = htmlspecialchars(trim($_POST['mensaje']));

    if ($nombre && $email && $mensaje) {
        $destinatario = "admin@tusitio.com"; // CAMBIA este correo
        $asunto = "Nuevo mensaje desde el formulario de contacto";
        $contenido = "Nombre: $nombre\n";
        $contenido .= "Email: $email\n\n";
        $contenido .= "Mensaje:\n$mensaje\n";

        $cabeceras = "From: $email\r\n";
        $cabeceras .= "Reply-To: $email\r\n";

        if (mail($destinatario, $asunto, $contenido, $cabeceras)) {
            echo "<script>alert('Mensaje enviado correctamente.'); window.history.back();</script>";
        } else {
            echo "<script>alert('Error al enviar el mensaje. Intenta más tarde.'); window.history.back();</script>";
        }
    } else {
        echo "<script>alert('Todos los campos son obligatorios.'); window.history.back();</script>";
    }
} else {
    header("Location: ayuda.html");
    exit;
}
?>
