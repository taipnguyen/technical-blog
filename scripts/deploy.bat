@echo off

set /p input= pug file to compile: 
pug %input%.pug
git add .
git commit -m %date%
git push