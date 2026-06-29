@echo off
setlocal

echo =====================================
echo Atualizacao automatica do projeto
echo =====================================

git status --short

if "%ERRORLEVEL%" neq "0" (
    echo Erro ao verificar status do Git.
    pause
    exit /b 1
)

for /f %%i in ('git status --porcelain') do set HAS_CHANGES=1

if not defined HAS_CHANGES (
    echo Nenhuma alteracao encontrada.
    pause
    exit /b 0
)

echo.
set /p CONFIRM=Confirmar commit e push? (S/N): 

if /I not "%CONFIRM%"=="S" (
    echo Operacao cancelada.
    pause
    exit /b 0
)

set /p MSG=Mensagem do commit: 

if "%MSG%"=="" (
    set MSG=Atualizacao automatica do projeto
)

git add .
git commit -m "%MSG%"
git push

echo.
echo Ultimo commit:
git log -1 --oneline

echo.
echo Atualizacao concluida.
pause