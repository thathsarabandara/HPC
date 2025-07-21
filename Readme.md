
# High Performance Computing Practice

This repository contains practice exercises and example programs for the **High Performance Computing** (HPC) module. The focus is on learning and experimenting with:

- **CUDA Programming** for GPU parallelism
- **MPI Programming** using `mpi4py` for distributed memory parallelism

## 📁 Structure

```
.
├── CUDA/               # CUDA programming exercises
├── MPI/                # MPI programming exercises (with mpi4py)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🛠️ Setup Instructions

Follow these steps to set up a Python environment for MPI development:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/hpc-practice.git
cd hpc-practice
```

### 2. Install OpenMPI (Linux)

```bash
sudo apt update
sudo apt install libopenmpi-dev openmpi-bin
```

> 💡 You must install an MPI implementation (like OpenMPI) before using `mpi4py`.

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run MPI Code

Use `mpiexec` to run your scripts with multiple processes. Example:

```bash
mpiexec -n 4 python MPI/basic.py
```

---

## 📦 requirements.txt

```txt
mpi4py
numpy
```

---

## 🚀 Goals

- Practice writing and executing CUDA C/C++ programs.
- Understand the basics of MPI communication using Python (`mpi4py`).
- Learn to configure a virtual development environment for HPC programming.

---

## 📚 Related Topics

- Massively Parallel Architectures (GPUs)
- Distributed Computing with MPI
- Python multiprocessing and hybrid CPU+GPU workflows

---

## ✍️ Author

- **Thathsara Bandara** – Undergraduate in Software Engineering

---

## 📜 License

This project is for academic and practice purposes under the [MIT License](LICENSE).