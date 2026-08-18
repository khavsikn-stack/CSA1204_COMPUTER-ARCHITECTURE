# Computational Performance Simulations

Simulations for the project **"Enhancing Computational Performance Using Modern Processor, Memory, and Bus Architectures"**.

Compares **traditional** vs **modern** computing architectures and generates an interactive dashboard you can use in your presentation.

## What Gets Simulated

| Module | Simulation | Metrics |
|--------|-----------|---------|
| Module 1 & 2 | **Processor** – 1 core vs 8 cores | Execution time, throughput, speedup |
| Module 1 & 2 | **Memory** – RAM-only vs cache hierarchy (L1/L2/L3) | Latency, bandwidth, hit rates |
| Module 1 & 2 | **Bus** – slow vs high-bandwidth interconnect | Transfer time, utilization |
| Module 3 | **Scalability** – increasing workload | Throughput, resource utilization, improvement % |

## Run Simulations

No installation needed — just Python 3:

```bash
python run_simulations.py
```

## Output

Files saved in `output/`:

- **`simulation_dashboard.html`** — open in Chrome/Edge; all charts in one page
- **`simulation_results.json`** — numeric results for your report

## How to Use in Your PPT

1. Run `python run_simulations.py`
2. Open `output/simulation_dashboard.html` in your browser
3. Take screenshots of each chart (Win + Shift + S)
4. Insert into:
   - **Module 2 slides** — processor, memory, bus charts
   - **Module 3 slides** — scalability & resource utilization
   - **Conclusion slide** — overall summary chart

## Team

- M. Harsha (192525108)
- K. Gnaneswar Kumar (192572105)
- S. Khavsik Narayanan (192511261)

Guided by: Dr. Rashmitha Khilar
