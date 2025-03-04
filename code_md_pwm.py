import matplotlib.pyplot as plt
import numpy as np

# 📌 Paramètres
frequence_signal = 1         # Fréquence du signal cosinus en Hz
frequence_sawtooth = 20      # Fréquence de la dent de scie en Hz
frequence_echantillonnage = 10  # Fréquence d'échantillonnage pour le sample-and-hold
duree = 1                    # Durée en secondes
amplitude = 3                # Amplitude du signal cosinus

# 📌 Génération du temps
t = np.linspace(0, duree, int(1000 * duree))
t_sample = np.linspace(0, duree, int(frequence_echantillonnage * duree))

# 📌 Génération du signal d'entrée (cosinus)
input_signal = amplitude * np.cos(2 * np.pi * frequence_signal * t)
input_signal_sampled = amplitude * np.cos(2 * np.pi * frequence_signal * t_sample)

# 📌 Génération du signal sample-and-hold
sample_and_hold = np.repeat(input_signal_sampled, len(t) // len(t_sample))

# 📌 Génération du signal en dent de scie
sawtooth = amplitude * (2 * (t * frequence_sawtooth % 1) - 1)

# 📌 Génération du signal PWM par comparaison entre sample-and-hold et dent de scie
pwm_signal = (sample_and_hold > sawtooth).astype(int)

# 📌 Affichage des signaux
fig, ax = plt.subplots(5, 1, figsize=(10, 10))

# Signal d'entrée
ax[0].plot(t, input_signal, label='Signal d\'entrée (3cos(2πft))', color='red')
ax[0].set_title('Signal d\'entrée')
ax[0].grid()

# Signal sample-and-hold
ax[1].step(t, sample_and_hold, where='post', label='Sample-and-Hold', color='brown')
ax[1].set_title('Sample-and-Hold Output')
ax[1].grid()

# Signal en dent de scie
ax[2].plot(t, sawtooth, label='Signal en dent de scie', color='purple')
ax[2].set_title('Signal en dent de scie')
ax[2].grid()

# Superposition des signaux
ax[3].plot(t, sample_and_hold, label='Sample-and-Hold', color='brown')
ax[3].plot(t, sawtooth, label='Dent de scie', color='purple', linestyle='--')
ax[3].set_title('Superposition : Sample-and-Hold vs Dent de scie')
ax[3].grid()
ax[3].legend()

# Signal PWM
ax[4].step(t, pwm_signal, where='post', label='Signal PWM', color='green')
ax[4].set_title('Signal PWM')
ax[4].grid()

plt.tight_layout()
plt.show()
