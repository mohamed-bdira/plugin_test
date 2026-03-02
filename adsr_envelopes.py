import numpy as np
import sounddevice as sd

def main():
    #Generate 4 sine saves

    sine1 = sine_tone(77.8, 2, 0.1)
    sine2 = sine_tone(116.5, 2, 0.1)
    sine3 = sine_tone(196, 2, 0.1)
    sine4 = sine_tone(261.6, 2, 0.1)

    #Combine the sine waves
    mysound = sum([sine1, sine2, sine3, sine4])
    mysound = apply_envelope(mysound, [0.5, 0.2, 0.6, 0.5])
     
    sd.play(mysound)
    sd.wait()

def sine_tone(
        frequency: float = 400,
        duration: float = 1.0,
        amplitude: float =  0.5,
        sample_rate: int = 44100
        ) -> np.ndarray:
    """Generate a sine tone"""

    #Calculate the number of samples required
    n_samples = int(sample_rate * duration)

    #Create an array of time points
    time_points = np.linspace(0, duration, n_samples, False)

    #Create the sine wave
    sine = np.sin(2 * np.pi * frequency * time_points)
    sine*= amplitude
    return sine

def apply_envelope(sound: np.ndarray, adsr: list, sample_rate: int = 44100) -> np.ndarray:
    sound = sound.copy()

    # Calculate samples
    attack_samples = int(adsr[0] * sample_rate)
    decay_samples = int(adsr[1] * sample_rate)
    release_samples = int(adsr[3] * sample_rate)
    sustain_samples = len(sound) - (attack_samples + decay_samples + release_samples)

    # 1. Attack: 0 to 1.0
    sound[:attack_samples] *= np.linspace(0, 1, attack_samples)

    # 2. Decay: 1.0 down to sustain level (adsr[2])
    sound[attack_samples:attack_samples + decay_samples] *= np.linspace(1.0, adsr[2], decay_samples)

    # 3. Sustain: Constant level
    sound[attack_samples + decay_samples : attack_samples + decay_samples + sustain_samples] *= adsr[2]

    # 4. Release: Sustain level down to 0
    sound[-release_samples:] *= np.linspace(adsr[2], 0, release_samples)

    return sound
    
if __name__ == "__main__":
    main()