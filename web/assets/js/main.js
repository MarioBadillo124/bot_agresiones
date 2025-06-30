//carga de datos de la db

function cargarIncidentes() {
    $.ajax({
        url: '../db/get_incidents.php',
        method: 'GET',
        success: function(data) {
            // Insertar datos en el tbody
            $('#incidentsData').html(data);

            // Reiniciar DataTable después de insertar los nuevos datos
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

$(document).ready(function() {
    cargarIncidentes();

    // Modal: ver incidente
    $(document).on('click', '.btn-action.view', function () {
        $('#detailModal').fadeIn();
    });

    $('.close-modal').click(function () {
        $('#detailModal').fadeOut();
    });
});

// Función para convertir dd/mm/yyyy → yyyy-mm-dd si hace falta
function formatearFecha(fecha) {
    const partes = fecha.split('/');
    if (partes.length === 3) {
        return `${partes[2]}-${partes[1]}-${partes[0]}`;
    }
    return fecha;
}

$(document).on('click', '.btn-filter', function () {
    let start = $('#startDate').val();
    let end = $('#endDate').val();

    // Asegurar formato correcto yyyy-mm-dd
    start = start ? start.split('/').reverse().join('-') : '';
    end = end ? end.split('/').reverse().join('-') : '';

    cargarIncidentes(start, end);
});


// Función que carga los incidentes (sin filtro o con)
function cargarIncidentes(startDate = '', endDate = '') {
    $.ajax({
        url: '../db/get_incidents.php',
        method: 'GET',
        data: {
            start: startDate,
            end: endDate
        },
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


$(document).ready(function() {
    // Carga todos los incidentes al inicio
    cargarIncidentes();

    // Modal: ver incidente
    $(document).on('click', '.btn-action.view', function () {
        $('#detailModal').fadeIn();
    });

    $('.close-modal').click(function () {
        $('#detailModal').fadeOut();
    });

    // Filtro por fechas
    $('.btn-filter').click(function () {
        let startDate = $('#startDate').val();
        let endDate = $('#endDate').val();

        // Convertir fechas si vienen en formato dd/mm/yyyy (por seguridad)
        startDate = formatearFecha(startDate);
        endDate = formatearFecha(endDate);

        cargarIncidentes(startDate, endDate);
    });
});


