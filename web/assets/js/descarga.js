$(document).ready(function() {

    // Función para cargar incidentes (con o sin filtros)
    function cargarIncidentes(startDate = '', endDate = '') {
        $.ajax({
            url: '../db/get_incidents.php',
            method: 'GET',
            data: { start: startDate, end: endDate },
            success: function(data) {
                $('#incidentsData').html(data);

                if ($.fn.DataTable.isDataTable('#incidentsTable')) {
                    $('#incidentsTable').DataTable().destroy();
                }

                $('#incidentsTable').DataTable({
                    order: [[0, "desc"]],
                    language: {
                        url: '//cdn.datatables.net/plug-ins/1.11.3/i18n/es_es.json'
                    }
                });
            },
            error: function() {
                $('#incidentsData').html('<tr><td colspan="6">Error al cargar los datos.</td></tr>');
            }
        });
    }

    // Carga inicial
    cargarIncidentes();

    // Abrir modal cuando se da clic en ver incidente
    $(document).on('click', '.btn-action.view', function () {
        const id = $(this).data('id');
        if (!id) {
            alert('ID del incidente no encontrado.');
            return;
        }

        $.ajax({
            url: 'db/get_incident_detail.php',
            method: 'GET',
            data: { id },
            dataType: 'json',
            success: function(data) {
                if(data.error) {
                    alert(data.error);
                    return;
                }
                // Aquí llenas el modal con data, por ejemplo (ajusta según tu modal):
                // $('#detailModal .info-grid').html(...);
                $('#detailModal').fadeIn();
            },
            error: function() {
                alert('Error al obtener los detalles del incidente.');
            }
        });
    });

    // Cerrar modal
    $('.close-modal').click(function () {
        $('#detailModal').fadeOut();
    });

    // Filtro por fechas
    $('.btn-filter').click(function (e) {
        e.preventDefault(); // prevenir submit real
        let start = $('#startDate').val();
        let end = $('#endDate').val();

        cargarIncidentes(start, end);
    });

    // Exportar tabla completa a PDF
    async function exportTableToPDF() {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF('p', 'pt', 'a4');
        const element = document.getElementById('incidentsTable');

        const canvas = await html2canvas(element, { scale: 2 });
        const imgData = canvas.toDataURL('image/png');

        const imgProps = doc.getImageProperties(imgData);
        const pdfWidth = doc.internal.pageSize.getWidth();
        const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;

        doc.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        doc.save('incidentes.pdf');
    }

    $('#exportBtn').click(() => {
        exportTableToPDF();
    });

    // Exportar incidente individual a PDF
    $(document).on('click', '.btn-action.download', function() {
        const id = $(this).closest('tr').find('.btn-action.view').data('id');

        if(!id) {
            alert('ID del incidente no encontrado.');
            return;
        }

        $.ajax({
            url: 'db/get_incident_detail.php',
            method: 'GET',
            data: { id },
            dataType: 'json',
            success: function(data) {
                if(data.error) {
                    alert(data.error);
                    return;
                }

                exportIncidentToPDF(data);
            },
            error: function() {
                alert('Error al obtener los detalles del incidente para exportar.');
            }
        });
    });

    function exportIncidentToPDF(data) {
        const { jsPDF } = window.jspdf;
        const doc = new jsPDF();

        doc.setFontSize(18);
        doc.text("Detalle del Incidente", 20, 20);

        doc.setFontSize(12);
        const lineHeight = 15;
        let y = 40;

        doc.text(`Fecha y Hora: ${data.fecha_hora}`, 20, y); y += lineHeight;
        doc.text(`Ubicación: ${data.ubicacion}`, 20, y); y += lineHeight;
        doc.text(`Tipo: ${data.tipo}`, 20, y); y += lineHeight;
        doc.text(`Severidad: ${data.severidad}`, 20, y); y += lineHeight;
        doc.text(`Estado: ${data.estado}`, 20, y); y += lineHeight;

        const description = data.descripcion || 'N/A';
        const acciones = data.acciones_tomadas || '';

        y += 10;
        doc.setFontSize(14);
        doc.text("Descripción:", 20, y); y += lineHeight;

        doc.setFontSize(12);
        const descriptionLines = doc.splitTextToSize(description, 170);
        doc.text(descriptionLines, 20, y);
        y += descriptionLines.length * lineHeight;

        y += 10;
        doc.setFontSize(14);
        doc.text("Acciones Tomadas:", 20, y); y += lineHeight;

        doc.setFontSize(12);
        const accionesLines = doc.splitTextToSize(acciones, 170);
        doc.text(accionesLines, 20, y);
        y += accionesLines.length * lineHeight;

        doc.save(`incidente_${data.id || 'detalle'}.pdf`);
    }

});
