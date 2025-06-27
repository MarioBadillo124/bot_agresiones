<?php

$servidor = "localhost"; 
$usuario = "root"; 
$contraseña = "1234"; 
$base_de_datos = "agreciones"; 
$puerto = 3307; 

$conexion = mysqli_connect($servidor, $usuario, $contraseña, $base_de_datos, $puerto);

if (!$conexion) {
    die("Conexión fallida: " . mysqli_connect_error()); 
}
?>
