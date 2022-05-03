@echo off
cls
:menu
cls
                   
echo                 *MENU*
echo  ===================================
echo * 1. Matar Processos Chrome
echo  ===================================

set /p opcao= Escolha uma opcao: 
echo ------------------------------
if %opcao% equ 1 goto opcao1

:opcao1

@echo on 
TASKKILL /f /im chrome.exe

@echo off
pause
goto menu
