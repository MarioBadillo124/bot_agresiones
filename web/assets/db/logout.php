<?php
session_start();
session_unset();
session_destroy();

// Evita que se pueda volver con el botón atrás
header("Cache-Control: no-store, no-cache, must-revalidate, max-age=0");
header("Location: ../../../index.html");
exit();
?>
