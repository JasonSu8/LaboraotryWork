

ampLeft = 0.05;   % Amplitude for left sound channel  
ampRight = 20;   % Amplitude for right sound channel  
freqLeft = 5000;   % Frequency for left sound channel   
freqRight = 12000;   % Frequency for right sound channel
fs = 96000;   % sampling frequency
t = 5;   % Sound duration

x = 0:(fs * t - 1); 
yLeft = ampLeft * sin(2 * pi * freqLeft * x / fs);
yRight = ampRight * sin(2 * pi * freqRight * x / fs);

sound(yLeft, fs, 24); 
pause(t);
sound(yRight, fs, 24); 
pause(t);
sound([yLeft; yRight], fs, 24); 
