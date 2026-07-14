@echo off
cd /d %~dp0\..
python -m automation.run_pipeline
pause