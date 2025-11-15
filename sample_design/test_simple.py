import logging
logging.basicConfig(level=logging.DEBUG)

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit('Single-Stage Common-Source Amplifier')
# Define the NMOS transistor model
circuit.model('nmos_model', 'nmos', level=1, kp=100e-6, vto=0.5)
# Power Supply for the power and input signal
circuit.V('dd', 'Vdd', circuit.gnd, 5.0)  # 5V power supply
circuit.V('in', 'Vin', circuit.gnd, 1.5)
# Single-Stage Common-Source Amplifier with Resistive Load
circuit.MOSFET('1', 'Vout', 'Vin', circuit.gnd, circuit.gnd, model='nmos_model', w=50e-6, l=1e-6)
circuit.R('1', 'Vout', 'Vdd', 1@u_kΩ)

print("Circuit netlist:")
print(str(circuit))
print("\nStarting simulation...")

# Analysis Part
simulator = circuit.simulator()
try:
    analysis = simulator.operating_point()
    print("Success!")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
