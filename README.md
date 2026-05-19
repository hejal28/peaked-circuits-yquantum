# Peaked Circuits: YQuantum × BlueQubit Hackathon

Quantum circuit simulation work from the YQuantum × BlueQubit hackathon 
at Yale (Spring 2026). Our 3-person team solved 8 of 10 Peaked Circuit 
challenges in 24 hours, placing in the top 30.

## The Problem

A "peaked circuit" is a quantum circuit whose output distribution is 
sharply concentrated on a single bitstring, rather than spread across 
many. The challenge: given a target peak, construct and simulate circuits 
that reproduce it, and do so at qubit counts where direct statevector the 
simulation becomes intractable.

The core difficulty is scale. A direct statevector simulation of an 
n-qubit circuit requires tracking 2^n amplitudes, which becomes infeasible 
on a laptop well before 40 qubits. The challenges pushed into the 40–60 
qubit range, beyond classical brute-force limits.

## Approach

We scaled our simulation strategy with the size of the circuit:

- **Small circuits**: direct statevector simulation, used as a baseline 
  and for verifying correctness.
- **Larger circuits (40–60 qubits)**: Matrix Product State (MPS) 
  approximation, which represents the quantum state in a compressed form 
  that stays tractable when entanglement is bounded.
- **Circuit optimization**: Qiskit transpilation and gate-cancellation 
  to reduce circuit depth before simulation, lowering the computational 
  cost of each run.
