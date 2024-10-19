import math

freq = float(input("Enter a value for the frequency, w: "))
duration = float(input("Enter a value for the duration of the sound wave, T: "))
    
eq = round((2 * math.sin(freq * duration))/freq, 3)
    
print("\nThe amplitude spectrum of this Fourier transform is:", eq)