# Reimport libraries and reset the sketching process after reset
import numpy as np
import matplotlib.pyplot as plt

# Define volume range (arbitrary units)
V = np.linspace(1, 10, 100)

# Define constants for the polytropic processes
C = 10  # Arbitrary constant

# Compute pressures for different values of n
P_n0 = np.full_like(V, C)            # n = 0 (constant pressure)
P_n1 = C / V                         # n = 1 (isothermal process)
P_n1_4 = C / (V ** 1.4)              # n = 1.4 (adiabatic process)
P_n_inf = np.full_like(V, np.nan)    # n = infinity (constant volume)
P_n_inf[0] = 10  # Arbitrary pressure for visualization

# Plot the P-V diagram
plt.figure(figsize=(8, 6))
plt.plot(V, P_n0, label="n = 0 (Isobaric)", color="blue")
plt.plot(V, P_n1, label="n = 1 (Isothermal)", color="green")
plt.plot(V, P_n1_4, label="n = 1.4 (Adiabatic)", color="orange")
plt.axvline(x=V[0], color="red", linestyle="--", label="n = ∞ (Isochoric)")

# Labels and legend
plt.title("Polytropic Processes on P-V Diagram")
plt.xlabel("Volume (V)")
plt.ylabel("Pressure (P)")
plt.grid(True)
plt.legend()
plt.show()