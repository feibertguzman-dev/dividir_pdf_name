@echo off
title Divisor de PDF por Nombres - Tipo iLovePDF
cd /d "%~dp0"
echo Iniciando Divisor de PDF Web...
echo Abre tu navegador en la direccion que aparecera a continuacion:
start "" "http://localhost:8501"
C:\Users\Feibert\AppData\Local\Programs\Python\Python311\Scripts\streamlit.exe run app.py
pause
