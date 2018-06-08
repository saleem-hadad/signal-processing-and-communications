% base audio
[xn, fs]=audioread('audio.wav');
x1 = xn(670000:689000);
dt = 1/fs;
t=0:dt:(length(x1)*dt)-dt;
plot(t, x1)
xlabel('Seconds');
ylabel('Apmlitude');

% note 1
figure;
N1 = xn(677000:681000);
t=1:1:length(N1);
plot(t, N1, 'lineWidth', 1.5);
xlabel('Seconds');
ylabel('Apmlitude');

% note 1: spectrum analysis
figure;
N_1 = length(N1);
x_1 = fftshift(fft(N1));
fshift = (-N_1/2:N_1/2-1) * (fs/N_1);
powershift=abs(x_1).^2/N_1;
plot(fshift, powershift,'linewidth',3)
xlim([-300, 300]);
xlabel('Frequency');
ylabel('Apmlitude');

% note 2
figure;
N2 = xn(682000:689000);
t=1:1:length(N2);
plot(t, N2, 'lineWidth', 1.5);
xlabel('Seconds');
ylabel('Apmlitude');

% note 2: spectrum analysis
figure;
N_2 = length(N2);
x_2 = fftshift(fft(N2));
fshift = (-N_2/2:N_2/2-1) * (fs/N_2);
powershift=abs(x_2).^2/N_2;
plot(fshift, powershift,'linewidth',3)
xlim([-300, 300]);
xlabel('Frequency');
ylabel('Apmlitude');

