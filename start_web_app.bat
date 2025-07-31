@echo off
echo Starting Job Application Monitor Web Interface...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Flask application...
echo Web interface will be available at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.
python app.py
pause
