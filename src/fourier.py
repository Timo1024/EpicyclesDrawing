"""
Fourier Transform Utilities

MIT License
"""
import numpy as np
import math
import cmath


class FourierDatum:
    """
    Holds Fourier Transform data: complex result, frequency, phase, and amplitude
    """
    def __init__(self, complex_num, freq):
        self.complex_num = complex_num
        self.freq = freq
        self.phase = math.atan2(complex_num.imag, complex_num.real)
        self.amplitude = np.sqrt(complex_num.real ** 2 + complex_num.imag ** 2)


def fft(z):
    """
    Take FFT of complex vector z and store its values in FourierDatum array
    :param z Complex-valued vector
    :returns Array of FourierDatum objects
    """
    fft_vals = np.fft.fft(z)
    fft_data = []
    N = len(z)
    k = 0

    for fft_val in fft_vals:
        # divide by N to keep drawing size reasonable
        fft_data.append(FourierDatum(fft_val / N, k))
        k += 1

    return fft_data


def dft(z):
    """
    Take DFT of complex vector z and store its values in FourierDatum array
    :param z Complex-valued vector
    :returns Array of FourierDatum objects
    """
    dft_data = []
    N = len(z)

    # k is frequency
    for k in range(0, N):
        zk = complex(0, 0)

        for n in range(0, N):
            phi = (2 * np.pi * k * n) / N
            zk += z[n] * complex(np.cos(phi), -np.sin(phi))

        zk /= N
        dft_data.append(FourierDatum(zk, k))

    return dft_data
