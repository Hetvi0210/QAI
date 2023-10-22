# -*- coding: utf-8 -*-
"""16 Qubit Random Number Generator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rWVQsMOqygCpN6mznk7LpqlilmkTpho3
"""

!pip install qiskit
!pip install qiskit-aer

import numpy as np
from qiskit import QuantumCircuit, transpile, assemble, Aer
from qiskit.visualization import plot_histogram

# Get the number of qubits from the user
num_qubits = int(input("Enter the number of qubits: "))

# Create a quantum circuit with the specified number of qubits
qc = QuantumCircuit(num_qubits, num_qubits)

# Apply Hadamard gates to all qubits to create superposition
for i in range(num_qubits):
    qc.h(i)

# Measure all qubits
qc.measure(range(num_qubits), range(num_qubits))

# Simulate the circuit using the Qiskit Aer simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit, shots=1)

# Run the circuit and obtain the result
result = simulator.run(qobj).result()
counts = result.get_counts()

# Convert the measurement result to an integer
random_number = int(list(counts.keys())[0], 2)

print("Random Number (in decimal):", random_number)
print("Random Number (in binary):", bin(random_number)[2:].zfill(num_qubits))