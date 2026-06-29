@echo off
echo =====================================
echo Atualizando projeto no GitHub
echo =====================================

git status

set /p MSG=Digite a mensagem do commit: 

git add .
git commit -m "%MSG%"
git push

echo =====================================
echo Atualizacao concluida.
echo =====================================
pause