@echo off
cls
:menu
cls
                   
echo                 *MENU*
echo  ===================================
echo * 1. Matar Processos Chrome
echo * 1. Matar Processo Chromedriver
echo  ===================================

set /p opcao= Escolha uma opcao: 
echo ------------------------------
if %opcao% equ 1 goto opcao1
if %opcao% equ 2 goto opcao2

:opcao1

@echo on 
TASKKILL /f /im chrome.exe

@echo off
pause
goto menu

:opcao2
TASKKILL /f /im chromedriver.exe

@echo off 
pause
goto menu
