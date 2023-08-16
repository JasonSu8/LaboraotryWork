amp = 1;   % Amplitude
freqBegin = 17000;   % Beginning of frequency for upsweep pattern
freqEnd = 20000;   % Ending of frequency for upsweep pattern
step = 20;    % Step of frequency change for upsweep pattern
fs = 192000;   % Sampling frequency
ts = 0.1;   % Sound duration of each frequency 
tt = 2;   % Sound duration of whole upsweep pattern

fr = linspace(freqBegin, freqEend, step);   % frequency sequence
N = fs * ts / step;   
y = zeros(1, fs * ts);
for i = 0:(step - 1)
    y(1, (N * i + 1):(N * i + N)) = amp * sin(2 * pi * fr(i + 1) * (0:N - 1) / fs);   
end
yy = repmat(y, 1, tt / ts);
sound(yy, fs, 24);   
