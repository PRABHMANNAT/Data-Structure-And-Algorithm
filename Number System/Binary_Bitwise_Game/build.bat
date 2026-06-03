@echo off
REM Windows one-click build for BitRealm.
REM Requires g++ (MinGW) in PATH.

g++ -std=c++17 -O2 -Wall -Wextra -Isrc src\*.cpp -o bitrealm.exe
if %ERRORLEVEL%==0 (
    echo.
    echo Build OK. Launch with:  bitrealm.exe
) else (
    echo.
    echo Build FAILED. Check the g++ output above.
)
