# Peaked Circuits: YQuantum × BlueQubit Hackathon

Quantum circuit simulation work from the YQuantum × BlueQubit hackathon 
at Yale (Spring 2026). A 3-person team effort, we solved 8 of the 10 
Peaked Circuit challenges in 24 hours, placing in the top 30. This 
repository includes our solutions for 7 of them.

## The Problem

A "peaked circuit" is a quantum circuit whose measurement distribution is 
sharply concentrated on a single bitstring. The challenge: identify that 
peak bitstring for each circuit — and do so at qubit counts where direct 
statevector simulation becomes infeasible.

Direct statevector simulation tracks 2^n amplitudes, which exhausts a 
laptop's memory well before 40 qubits. The harder challenges reached 60 
qubits, beyond the brute-force limit.

## Approach

Rather than applying one method everywhere, we matched the technique to 
each circuit's structure:

- **Analytic solution (P1, 4 qubits)**: for a circuit with no entangling 
  gates, no simulation is needed. We walked the circuit gate by gate, 
  flipping bits for X gates and comparing rotation probabilities for RY 
  gates, to compute the peak directly.

- **Exact statevector (P2, 12 qubits; P3)**: for small circuits, full 
  statevector simulation. P3 includes a runtime memory check that 
  confirms enough available RAM before launching the simulation.

- **Matrix Product State approximation (P4, 40 qubits; P6, 60 qubits)**: 
  for large circuits, MPS simulation with a bounded bond dimension (64 for 
  P4, 256 for P6), which stays tractable when circuit entanglement is 
  limited.

- **Approximate transpilation (P6)**: transpiling at approximation degree 
  0.99 removed roughly 96% of the circuit's gates before simulation, 
  sharply cutting cost while preserving the peak. Final confidence on the 
  peak bitstring was ~99%.

- **Circuit decomposition (P7, 42 qubits)**: we detected that the circuit 
  separated into two independent qubit groups by running a connected-
  components search over the graph of two-qubit gates. Each subcircuit was 
  simulated separately as a smaller problem, and the partial peaks were 
  recombined into the full 42-bit result.

## Repository Contents
- `p1_little_peak.ipynb` - analytic solution (4 qubits)
- `p2_small_bump.ipynb` - exact statevector (12 qubits)
- `p3_tiny_ripple.py` - statevector with memory check
- `p4_gentle_mound.ipynb` - MPS, bond dimension 64 (40 qubits)
- `p5_soft_rise.ipynb` - Pauli-path expectation values (50 qubits)
- `p6_low_hill.ipynb` - MPS + approximate transpilation (60 qubits)
- `p7_rolling_ridge.ipynb` - circuit decomposition (42 qubits)

## What We'd Improve

Built in 24 hours, so there's clear room to strengthen it:

- The notebooks repeat setup code; the shared simulation logic would be 
  better factored into a single module imported by each.
- MPS bond dimension was chosen by hand per circuit, an adaptive scheme 
  that raises it until the peak stabilizes would be more robust.

## Context

Built at the YQuantum × BlueQubit hackathon, Yale University, Spring 2026, 
as a 3-person team, we worked together on separate problems throughout. 
Tools: Python, Qiskit, Qiskit Aer, NumPy.
