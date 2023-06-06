import numpy as np
from scipy.signal import chirp, spectrogram
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 1000  # 采样频率
DURATION = 3  # 采样时间

def generate_sine_wave(sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    X = np.zeros(3000)
    x1 = X
    x1[200:1200] = chirp(x,f0=0, f1=201, t1=1)
    x1[1500:2500] = chirp(x, f0=0, f1=201, t1=1)

    x2 = X
    x2[200:1200] = chirp(x, f0=50, f1=251, t1=1)
    x2[1800:2800] = chirp(x, f0=50, f1=251, t1=1)
    y = x1 + x2
    return x, y

def plot_spectrogram(w, fs):
    ff, tt, Sxx = spectrogram(w, fs=fs, nperseg=100, nfft=250)
    # plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.xlabel('t (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.grid()


x, y = generate_sine_wave(SAMPLE_RATE, DURATION)

fig,axes = plt.subplots(2,2)
ax1 = axes[0, 0]
ax1.plot(x, y)
#傅里叶变换
N = SAMPLE_RATE * DURATION
yf = rfft(y)
xf = rfftfreq(N, 1 / SAMPLE_RATE)
ax2 = axes[0, 1]
ax2.plot(xf, np.abs(yf))
#短时傅里叶变换
plot_spectrogram(y, SAMPLE_RATE)
plt.show()


