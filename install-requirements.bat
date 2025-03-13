@echo off
echo Installing base dependencies...
pip install -r requirements-base.txt

echo Installing Windows-specific dependencies...
pip install -r requirements-windows.txt

set /p install_gpu="Do you want to install GPU (CUDA) dependencies? (y/n): "
if /I "%install_gpu%"=="y" (
    echo Installing GPU dependencies...
    pip install -r requirements-gpu.txt
)

echo Installation complete!
pause
