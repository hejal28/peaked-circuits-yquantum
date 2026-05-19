from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import time

qc = QuantumCircuit.from_qasm_file("P3_tiny_ripple.qasm")
qc.measure_all()
print(f"Qubits: {qc.num_qubits}, Depth: {qc.depth()}")

import psutil
ram_gb = psutil.virtual_memory().available / 1e9
print(f"Available RAM: {ram_gb:.1f} GB")

if ram_gb < 18:
    print("Not enough")
else:
    print("starting simulation...")
    simulator = AerSimulator(method="statevector")
    start = time.time()
    job = simulator.run(qc, shots=4096)
    counts = job.result().get_counts()
    print(f"Done in {time.time()-start:.1f}s")
    
    total = sum(counts.values())
    peak = max(counts, key=counts.get)
    print(f"\nPeak: {peak}")
    print(f"Confidence: {counts[peak]/total:.4%}")
    
    print("\nTop 10:")
    for bits, count in sorted(counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  {bits}: {count/total:.4%}")
