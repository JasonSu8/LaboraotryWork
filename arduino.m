% step 1
arduinoPort = serialport('com4');
set(arduinoPort, 'BaudRate', 9600, 'DataBits', 8, 'StopBits', 1);

% step 2
fopen(arduinoPort);

% step 3
fprintf(arduinoPort, '1');
pause(6);

% step 4
fclose(arduinoPort);
delete(arduinoPort);
