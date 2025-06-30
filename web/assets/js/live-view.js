async function startCamera() {
    const video = document.getElementById('cameraPatio');
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        alert('Tu navegador no soporta acceso a cámara.');
        return;
    }

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        video.srcObject = stream;
    } catch (err) {
        alert('No se pudo acceder a la cámara: ' + err.message);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    startCamera();
});
