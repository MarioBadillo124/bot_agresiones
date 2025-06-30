<?php
require_once '../vendor/autoload.php'; // Ajusta la ruta si está en otra ubicación

use Dompdf\Dompdf;
use Dompdf\Options;

$options = new Options();
$options->set('defaultFont', 'Arial');
$dompdf = new Dompdf($options);

// Puedes personalizar este contenido con datos dinámicos o HTML de tu frontend
$html = '
    <h1 style="text-align:center;">Reporte de Incidentes</h1>
    <p><strong>Generado:</strong> ' . date("d-m-Y H:i") . '</p>
    <table border="1" cellpadding="8" cellspacing="0" width="100%">
        <thead>
            <tr>
                <th>Tipo</th>
                <th>Cantidad</th>
            </tr>
        </thead>
        <tbody>
            <tr><td>Agresión Física</td><td>12</td></tr>
            <tr><td>Actividad Sospechosa</td><td>6</td></tr>
            <tr><td>Bullying Verbal</td><td>4</td></tr>
            <tr><td>Vandalismo</td><td>2</td></tr>
        </tbody>
    </table>
';

$dompdf->loadHtml($html);
$dompdf->setPaper('A4', 'portrait');
$dompdf->render();
$dompdf->stream("reporte_incidentes_" . date("Ymd_His") . ".pdf", ["Attachment" => false]);
exit();
