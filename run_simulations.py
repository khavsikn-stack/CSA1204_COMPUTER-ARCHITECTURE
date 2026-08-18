"""Run all computational performance simulations and generate charts."""

from __future__ import annotations

from pathlib import Path

from simulations.bus_sim import run_bus_simulation
from simulations.memory_sim import run_memory_simulation
from simulations.processor_sim import run_processor_simulation
from simulations.report import write_report
from simulations.scalability_sim import run_scalability_simulation


def main() -> None:
    root = Path(__file__).resolve().parent
    output_dir = root / "output"
    output_dir.mkdir(exist_ok=True)

    print("=" * 60)
    print("Computational Performance Simulations")
    print("Traditional vs Modern Processor, Memory, and Bus")
    print("=" * 60)

    processor = run_processor_simulation()
    print("\n[Module 1/2] Processor Simulation")
    print(f"  1000 tasks - Traditional: {processor['traditional_time_s']:.3f}s")
    print(f"  1000 tasks - Modern:     {processor['modern_time_s']:.3f}s")
    print(f"  Speedup: {processor['speedup']:.1f}x")

    memory = run_memory_simulation()
    print("\n[Module 1/2] Memory Simulation")
    print(f"  Avg latency - Traditional: {memory['traditional_avg_latency_cycles']:.0f} cycles")
    print(f"  Avg latency - Modern:      {memory['modern_avg_latency_cycles']:.1f} cycles")
    print(f"  Latency improvement: {memory['latency_improvement_pct']:.1f}%")

    bus = run_bus_simulation()
    print("\n[Module 1/2] Bus Simulation")
    print(f"  256 MB transfer - Traditional: {bus['traditional_sample_ms']:.1f} ms")
    print(f"  256 MB transfer - Modern:      {bus['modern_sample_ms']:.1f} ms")
    print(f"  Speedup: {bus['speedup']:.1f}x")

    scalability = run_scalability_simulation()
    print("\n[Module 3] Scalability Simulation")
    print(f"  Average improvement: {scalability['avg_improvement_pct']:.1f}%")
    print(f"  Max improvement:     {scalability['max_improvement_pct']:.1f}%")

    results = {
        "processor": processor,
        "memory": memory,
        "bus": bus,
        "scalability": scalability,
    }
    html_path, json_path = write_report(output_dir, results)

    print("\n" + "=" * 60)
    print("Output saved to:", output_dir)
    print("  Dashboard:", html_path.name)
    print("  Results:  ", json_path.name)
    print("=" * 60)
    print("\nOpen simulation_dashboard.html in your browser.")
    print("Take screenshots of each chart and add them to your PPT.")


if __name__ == "__main__":
    main()
