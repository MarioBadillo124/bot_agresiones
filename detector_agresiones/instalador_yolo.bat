@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

echo ========================================
echo  🚀 Instalador de YOLOv8 para Windows
echo ========================================

:: Verificar Python
where python >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python no está instalado.
    echo 🔽 Descargando e instalando Python 3.11...
    curl -o python-installer.exe https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    del python-installer.exe
    echo ✅ Python instalado correctamente.
) ELSE (
    echo ✅ Python ya está instalado.
)

:: Verificar pip
python -m ensurepip --default-pip
python -m pip install --upgrade pip

:: Instalar Ultralytics
echo 🔧 Instalando Ultralytics (YOLOv8)...
pip install ultralytics

:: Crear estructura del proyecto
echo 🗂️  Creando estructura del proyecto...
mkdir datasets\raw_videos\fight
mkdir datasets\raw_videos\no_fight
mkdir datasets\extracted_frames\fight
mkdir datasets\extracted_frames\no_fight
mkdir datasets\labels\fight
mkdir datasets\labels\no_fight
mkdir scripts
mkdir runs
mkdir yolov8_model

:: Crear archivo YAML por defecto
echo train: datasets/extracted_frames/ > datasets/agresion.yaml
echo val: datasets/extracted_frames/ >> datasets/agresion.yaml
echo. >> datasets/agresion.yaml
echo nc: 2 >> datasets/agresion.yaml
echo names: ['no_fight', 'fight'] >> datasets/agresion.yaml

echo ✅ Todo listo. Ahora puedes comenzar tu entrenamiento con:
echo python -m ultralytics task=detect mode=train model=yolov8n.pt data=datasets/agresion.yaml epochs=100 imgsz=640

pause