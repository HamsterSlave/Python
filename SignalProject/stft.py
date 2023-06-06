import numpy as np
from scipy.signal import chirp, spectrogram
from matplotlib import pyplot as plt
from scipy.fft import rfft, rfftfreq

SAMPLE_RATE = 1000  # 采样频率
DURATION = 2  # 采样时间

def generate_sine_wave(freq, sample_rate, duration):
    # T = 0.001
    # a = np.arange(0, sample_rate * duration,1)
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    frequencies = x * freq
    s = np.sin((2 * np.pi) * frequencies)
    x1 = chirp(x,f0=300, f1=0, t1=2, method='quadratic')
    N = [0]*2000
    n1 = N
    n1[800:1000] = x1[800:1000]
    n2 = N
    n2[1200:1800] = x1[1200:1800]
    y = s + n1 + n2
    return x, y

def plot_spectrogram(w, fs):
    ff, tt, Sxx = spectrogram(w, fs=fs, nperseg=100, nfft=250)
    # plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.pcolormesh(tt, ff[:145], Sxx[:145], cmap='gray_r', shading='gouraud')
    plt.xlabel('t (sec)')
    plt.ylabel('Frequency (Hz)')
    plt.grid()


x, y = generate_sine_wave(50, SAMPLE_RATE, DURATION)

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


