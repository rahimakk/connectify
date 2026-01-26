echo ==============================
echo Setting up Connectify Project
echo ==============================

echo.
echo Installing Python backend requirements...
cd backend
pip install -r requirements.txt

echo.
echo Installing Newman (API Automation Tool)...
npm install -g newman

echo.
echo Setup Complete!
pause
