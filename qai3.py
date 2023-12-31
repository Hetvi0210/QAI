# -*- coding: utf-8 -*-
"""QAI3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-uEOGwuztNOZxDoi6v_96woefx62e3qe
"""

pip install qiskit

pip install qiskit-aer

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile, assemble, Aer, execute

# Create a Quantum Circuit with three quantum registers and three classical registers
qr = QuantumRegister(3, 'q')
crz = ClassicalRegister(1, 'crz')
crx = ClassicalRegister(1, 'crx')
c = ClassicalRegister(1, 'c')
teleportation_circuit = QuantumCircuit(qr, crz, crx, c)

# Create an entangled Bell pair (Alice and Bob share qubits 1 and 2)
teleportation_circuit.h(qr[1])
teleportation_circuit.cx(qr[1], qr[2])

# Alice prepares the qubit to be teleported (qubit 0)
teleportation_circuit.barrier()
teleportation_circuit.h(qr[0])
teleportation_circuit.cx(qr[0], qr[1])
teleportation_circuit.measure(qr[0], crz)
teleportation_circuit.measure(qr[1], crx)

# Alice sends her classical measurement results to Bob
teleportation_circuit.barrier()
teleportation_circuit.x(qr[2]).c_if(crz, 1)
teleportation_circuit.z(qr[2]).c_if(crx, 1)

# Measure the teleported qubit by Bob
teleportation_circuit.measure(qr[2], c)

# Draw the quantum circuit
print(teleportation_circuit)

# Simulate and execute the circuit using Qiskit Aer simulator
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(teleportation_circuit, simulator)
job = execute(compiled_circuit, simulator, shots=1024)
result = job.result()

# Get and print the measurement results
counts = result.get_counts()
print("Measurement results:", counts)

