winget install --id Git.Git -e --source winget
ssh-keygen -t rsa

@SET /P name=Input Github account name: 
git config --global user.name %name%

@SET /P email=Input Github account e-mail: 
git config --global user.email %email%

@REM "Show RSA Key"
@echo off
CD %HOMEPATH%\.ssh
echo:
type id_rsa.pub
echo:
:loop
pause
goto loop