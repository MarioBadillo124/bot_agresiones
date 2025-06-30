document.addEventListener('DOMContentLoaded', initCharts);
document.addEventListener('DOMContentLoaded', () => {
    initCharts('month'); // Inicial por defecto

    document.getElementById('periodSelect').addEventListener('change', function () {
        const periodo = this.value;
        updateCharts(periodo);
    });
});

function initCharts() {
    // Gráfico de tipos de incidentes
    new Chart(document.getElementById('typeChart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: ['Agresión Física', 'Actividad Sospechosa', 'Bullying Verbal', 'Vandalismo'],
            datasets: [{
                data: [12, 6, 4, 2],
                backgroundColor: ['#e53935', '#ffb74d', '#64b5f6', '#81c784']
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom' } }
        }
    });

    // Gráfico de incidentes por ubicación
    new Chart(document.getElementById('locationChart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Patio', 'Cancha', 'Entrada', 'Baños'],
            datasets: [{
                label: 'Cantidad',
                data: [8, 5, 6, 5],
                backgroundColor: ['#42a5f5', '#ffb74d', '#e53935', '#81c784']
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true } }
        }
    });

    // Gráfico por hora del día
    new Chart(document.getElementById('hourChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: ['08:00', '10:00', '12:00', '14:00', '16:00'],
            datasets: [{
                label: 'Incidentes',
                data: [2, 5, 8, 4, 3],
                borderColor: '#fb8c00',
                fill: false,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom' } },
            scales: { y: { beginAtZero: true } }
        }
    });

    // Gráfico de tendencia mensual
    new Chart(document.getElementById('trendChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            datasets: [{
                label: 'Incidentes',
                data: [10, 12, 8, 15, 9, 11],
                borderColor: '#5e35b1',
                fill: false,
                tension: 0.4
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom' } },
            scales: { y: { beginAtZero: true } }
        }
    });

    // Gráfico de severidad
    new Chart(document.getElementById('severityChart').getContext('2d'), {
        type: 'pie',
        data: {
            labels: ['Alta', 'Media', 'Baja'],
            datasets: [{
                data: [5, 12, 7],
                backgroundColor: ['#e53935', '#ffb74d', '#81c784']
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom' } }
        }
    });

    // Gráfico de incidentes por día de la semana
    new Chart(document.getElementById('weeklyChart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
            datasets: [{
                label: 'Incidentes',
                data: [3, 4, 6, 5, 2, 1, 3],
                backgroundColor: '#42a5f5'
            }]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: { y: { beginAtZero: true, title: { display: true, text: 'Cantidad' } } }
        }
    });

    // Gráfico de líneas por tipo de incidente (evolución semanal)
    new Chart(document.getElementById('weeklyTrendChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
            datasets: [
                {
                    label: 'Agresión Física',
                    data: [4, 5, 6, 3],
                    borderColor: '#e53935',
                    fill: false,
                    tension: 0.3
                },
                {
                    label: 'Bullying Verbal',
                    data: [2, 3, 4, 2],
                    borderColor: '#64b5f6',
                    fill: false,
                    tension: 0.3
                },
                {
                    label: 'Vandalismo',
                    data: [1, 2, 1, 2],
                    borderColor: '#81c784',
                    fill: false,
                    tension: 0.3
                }
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'bottom' } },
            scales: { y: { beginAtZero: true } }
        }
    });
}

let typeChart, locationChart, hourChart, trendChart, severityChart;

function initCharts(periodo = 'month') {
    let datos = {
        month: {
            tipos: [12, 6, 4, 2],
            ubicaciones: [8, 5, 6, 5],
            horas: [2, 5, 8, 4, 3],
            tendencia: [10, 12, 8, 15, 9, 11],
            severidad: [5, 12, 7]
        }
    }[periodo];

    const typeCtx = document.getElementById('typeChart').getContext('2d');
    typeChart = new Chart(typeCtx, {
        type: 'doughnut',
        data: {
            labels: ['Agresión Física', 'Actividad Sospechosa', 'Bullying Verbal', 'Vandalismo'],
            datasets: [{ data: datos.tipos, backgroundColor: ['#e53935', '#ffb74d', '#64b5f6', '#81c784'] }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
    });

    const locationCtx = document.getElementById('locationChart').getContext('2d');
    locationChart = new Chart(locationCtx, {
        type: 'bar',
        data: {
            labels: ['Patio', 'Cancha', 'Entrada', 'Baños'],
            datasets: [{ label: 'Cantidad', data: datos.ubicaciones, backgroundColor: '#42a5f5' }]
        },
        options: { responsive: true, plugins: { legend: { display: false } }, scales: { y: { beginAtZero: true } } }
    });

    const hourCtx = document.getElementById('hourChart').getContext('2d');
    hourChart = new Chart(hourCtx, {
        type: 'line',
        data: {
            labels: ['08:00', '10:00', '12:00', '14:00', '16:00'],
            datasets: [{ label: 'Incidentes', data: datos.horas, borderColor: '#fb8c00', fill: false, tension: 0.3 }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } }, scales: { y: { beginAtZero: true } } }
    });

    const trendCtx = document.getElementById('trendChart').getContext('2d');
    trendChart = new Chart(trendCtx, {
        type: 'line',
        data: {
            labels: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
            datasets: [{ label: 'Incidentes', data: datos.tendencia, borderColor: '#5e35b1', fill: false, tension: 0.4 }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } }, scales: { y: { beginAtZero: true } } }
    });

    const severityCtx = document.getElementById('severityChart').getContext('2d');
    severityChart = new Chart(severityCtx, {
        type: 'pie',
        data: {
            labels: ['Alta', 'Media', 'Baja'],
            datasets: [{ data: datos.severidad, backgroundColor: ['#e53935', '#ffb74d', '#81c784'] }]
        },
        options: { responsive: true, plugins: { legend: { position: 'bottom' } } }
    });
}

function updateCharts(periodo) {
    // Aquí actualizamos los datos en base al periodo
    let nuevosDatos;

    switch (periodo) {
        case 'day':
            nuevosDatos = {
                tipos: [2, 1, 0, 1],
                ubicaciones: [1, 0, 1, 2],
                horas: [0, 1, 1, 1, 0],
                tendencia: [1, 2, 1, 1, 2, 1],
                severidad: [1, 1, 1]
            };
            break;
        case 'week':
            nuevosDatos = {
                tipos: [4, 2, 2, 1],
                ubicaciones: [2, 2, 2, 1],
                horas: [1, 2, 2, 2, 1],
                tendencia: [3, 4, 2, 3, 4, 3],
                severidad: [2, 3, 1]
            };
            break;
        case 'month':
            nuevosDatos = {
                tipos: [12, 6, 4, 2],
                ubicaciones: [8, 5, 6, 5],
                horas: [2, 5, 8, 4, 3],
                tendencia: [10, 12, 8, 15, 9, 11],
                severidad: [5, 12, 7]
            };
            break;
        case 'year':
            nuevosDatos = {
                tipos: [30, 20, 15, 10],
                ubicaciones: [20, 18, 22, 25],
                horas: [12, 18, 20, 15, 13],
                tendencia: [30, 25, 28, 40, 36, 38],
                severidad: [10, 20, 15]
            };
            break;
        default:
            return; // no hacer nada
    }

    // Ahora actualizamos las gráficas con los nuevos datos
    typeChart.data.datasets[0].data = nuevosDatos.tipos;
    locationChart.data.datasets[0].data = nuevosDatos.ubicaciones;
    hourChart.data.datasets[0].data = nuevosDatos.horas;
    trendChart.data.datasets[0].data = nuevosDatos.tendencia;
    severityChart.data.datasets[0].data = nuevosDatos.severidad;

    // Refrescamos los gráficos
    typeChart.update();
    locationChart.update();
    hourChart.update();
    trendChart.update();
    severityChart.update();
}

//generar PDF

document.getElementById('generateReportBtn').addEventListener('click', () => {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF('p', 'mm', 'a4');
    const content = document.getElementById('reportContent');

    html2canvas(content).then(canvas => {
        const imgData = canvas.toDataURL('image/png');
        const imgProps = doc.getImageProperties(imgData);
        const pdfWidth = doc.internal.pageSize.getWidth();
        const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;

        doc.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
        doc.save('Reporte_General.pdf');
    });
});
