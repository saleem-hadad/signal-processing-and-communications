import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav

NTTF = 1000
names = [
	'saleem',
	'tariq',
	'khaled',
	'muhammed',
	'google'
]

def calc_fft(audio):
	fs, data = wav.read(audio)
	fft_out = fft(data)
	k = np.arange(len(data))
	T = len(data)/fs
	frqLabel = k/T
	fft_out = fft_out[:len(fft_out)//2-1]
	frqLabel= frqLabel[:len(frqLabel)//2-1]
	plt.plot(frqLabel, np.abs(fft_out))
	return np.abs(fft_out)

def calc_dist(s1, s2):
	return np.linalg.norm(s1 - s2)

def calc_avg_fft(s):
	return np.sum(s/len(s))

def avg_fft(name):
	avg_ffts = []
	plt.figure(name)
	for i in range(5):

		avg_ffts.append(
			calc_avg_fft(
				calc_fft('./dataset/' + name + str(i+1) + '.wav')
			)
		)

	return np.average(avg_ffts)

def normalized(a, axis=-1, order=2):
    l2 = np.atleast_1d(np.linalg.norm(a, order, axis))
    l2[l2==0] = 1
    return a / np.expand_dims(l2, axis)

def process_unknowns(known):
	n = len(known)
	result = []
	for i in range(n):
		dists = []
		avg_fft = calc_avg_fft(calc_fft('./dataset/unknown' + str(i+1) + '.wav'))
		for j in range(n):
			dists.append(calc_dist(known[j], avg_fft))
		result.append((1-normalized(dists))*100)
	return result

result = process_unknowns([
	avg_fft(names[0]),
	avg_fft(names[1]),
	avg_fft(names[2]),
	avg_fft(names[3]),
	avg_fft(names[4]),
])

for i in range(len(result)):
	print("unknown " + str(i+1) + ", matched "),
	for j in range(len(result[i][0])):
		print(str(int(result[i][0][j])) + "% with " + names[j] + " "),
	print

plt.show()
