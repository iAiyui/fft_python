#coding:utf-8
import wave
import numpy as np
import scipy.fftpack
from scipy import signal
from pylab import *

if __name__ == "__main__" :
    wf = wave.open("gwave47.wav" , "r" )
    fs = wf.getframerate()  # �T���v�����O���g��
    x  = wf.readframes(wf.getnframes())
    x  = frombuffer(x, dtype= "int16") / 32768.0  # -1 - +1�ɐ��K��
    wf.close()

    start = 0  # �T���v�����O����J�n�ʒu
    N = 14400#2048#1024#65536    # FFT�̃T���v����

    X = np.fft.fft(x[start:start+N])  # FFT
#    X = scipy.fftpack.fft(x[start:start+N])         # scipy��

    freqList = np.fft.fftfreq(N, d=1.0/fs)  # ���g�����̒l���v�Z
#    freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)  # scipy��

    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]  # �U���X�y�N�g��
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]    # �ʑ��X�y�N�g��



    # �g�`��`��
    subplot(211)  # 3�s1��̃O���t��1�Ԗڂ̈ʒu�Ƀv���b�g
    plot(range(start, start+N), x[start:start+N])
    axis([start, start+N, -1.0, 1.0])
    xlabel("time [sample]")
    ylabel("amplitude")

    # �U���X�y�N�g����`��
    subplot(212)
    plot(freqList, amplitudeSpectrum,linestyle='-')
    axis([0, fs/2, 0, 50])
    xscale("log")
    xlim([0,1000])
    xlabel("frequency [Hz]")
    ylabel("amplitude spectrum")

    show()