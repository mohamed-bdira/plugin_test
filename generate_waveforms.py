import numpy as np
import sounddevice as sd

def main():
    #Generate 3 sine saves

    saw1 = saw_tone(77.8, 2, 0.1)
    saw2 = saw_tone(116.5, 2, 0.1)
    saw3 = saw_tone(196, 2, 0.1)
    saw4 = saw_tone(261.6, 2, 0.1)

    #Combine the sine waves
    mysound = sum([saw1, saw2, saw3, saw4])
     
    sd.play(mysound)
    sd.wait()

def saw_tone(
        frequency: float = 400,
        duration: float = 1.0,
        amplitude: float =  0.5,
        sample_rate: int = 44100
        ) -> np.ndarray:
    """Generate a sawtooth tone"""

    # Calculate the number of samples required
    n_samples = int(sample_rate * duration)

    # Create an array of time points
    time_points = np.linspace(0, duration, n_samples, False)

    # Create the sawtooth wave:
    # (time_points * frequency) % 1.0 creates a ramp from 0 to 1
    # Multiply by 2 and subtract 1 to scale it from -1 to 1
    sawtooth = 2.0 * ((time_points * frequency) % 1.0) - 1.0
    
    sawtooth *= amplitude
    return sawtooth

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

def white_noise(
        duration: float= 1.0,
        amplitude: float= 0.5,
        sample_rate: int= 44100
        ) -> np.ndarray:
        
    
    """ Generate white noise. """

    # Calculate the number of samples needed
    n_samples = int(duration * sample_rate)

    #Generate white noise with values between -1 & 1
    noise  = np.random.uniform(-1, 1, n_samples)

    #Scale by amplitude
    noise*= amplitude
    return noise

if __name__ == "__main__":
    main()