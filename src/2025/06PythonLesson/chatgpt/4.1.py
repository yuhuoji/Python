import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# 设置字体为 STHeiti（你系统已安装）
matplotlib.rcParams['font.family'] = 'STHeiti'
matplotlib.rcParams['axes.unicode_minus'] = False

snr = [5, 10, 15]
ber_turbo = [1e-2, 2e-3, 5e-4]
ber_ldpc = [1e-4, 1e-5, 1e-6]

plt.semilogy(snr, ber_turbo, marker='o', label='Turbo 码')
plt.semilogy(snr, ber_ldpc, marker='s', label='LDPC 码')
plt.xlabel('SNR (dB)')
plt.ylabel('误码率 (BER)')
plt.title('误码率 vs SNR')
plt.legend()
plt.grid(True, which='both')
plt.tight_layout()
plt.show()
