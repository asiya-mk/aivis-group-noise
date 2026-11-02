import numpy as np
import librosa

SR = 16000


def load_audio(path, sr=SR):
    y, _ = librosa.load(path, sr=sr, mono=True)
    return y


def rms(y):
    return np.sqrt(np.mean(y ** 2) + 1e-12)


def fit_length(y, n):
    if len(y) >= n:
        return y[:n]
    return np.tile(y, int(np.ceil(n / len(y))))[:n]


def gain(y, db):
    return y * 10 ** (db / 20)


def add_noise(y, snr_db, noise=None, seed=0):
    # white noise unless a noise clip is given
    if noise is None:
        noise = np.random.default_rng(seed).standard_normal(len(y)).astype(np.float32)
    noise = fit_length(noise, len(y))
    return y + noise * rms(y) / (rms(noise) * 10 ** (snr_db / 20))


def mix(target, other, ratio_db):
    # ratio_db = level of target over other: +20 target dominates, -20 other dominates
    other = fit_length(other, len(target))
    return target + other * rms(target) / (rms(other) * 10 ** (ratio_db / 20))


def windows(y, sec=5.0, hop=2.5, sr=SR):
    n, h = int(sec * sr), int(hop * sr)
    starts = range(0, max(len(y) - n, 0) + 1, h)
    return [(s / sr, y[s:s + n]) for s in starts]
