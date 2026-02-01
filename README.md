
# 🐍 Snake AI (Clean Architecture)

A **deterministic Snake simulation engine** built with **clean architecture principles** and **pluggable controllers**, designed as an **AI-ready environment** rather than a simple game clone.

This project demonstrates how to build **maintainable, testable, and extensible systems** where game logic, rendering, and decision-making are fully decoupled.

---

## 🎯 Why This Project Exists

Most Snake implementations tightly couple:
- input handling
- game logic
- rendering
- timing

This project **intentionally separates concerns** so the engine can support:
- Human players
- Heuristic AI agents
- Future ML / RL agents
- Deterministic replay and simulation

It is designed as a **simulation engine first**, game second.

---

## ✨ Key Features

- ✅ **Deterministic tick-based simulation** (engine ≠ FPS)
- ✅ **Clean Architecture**
  - `state` → pure data
  - `systems` → rules & mechanics
  - `engine` → orchestration
  - `input` → controllers (Human / AI)
  - `render` → read-only visualization
- ✅ **Hot-swappable controllers**
  - Press `T` to switch **Human ↔ AI** mid-game
- ✅ **AI controller**
  - Heuristic, policy-based (no randomness)
  - Collision-aware
  - Food-seeking behavior
- ✅ **Renderer contains ZERO game logic**
- ✅ **Restart & pause-safe**
- ✅ **AI / RL-ready environment**
- ✅ **Unit tests for core systems**

---

## 🧠 Architecture Overview

<p align="center">
  <img src="docs/Snake%20diagram.png" alt="Snake AI Clean Architecture Diagram" width="900"/>
</p>


````

---

## 🎮 Controls

| Key | Action |
|----|-------|
| Arrow Keys | Move (Human controller) |
| **T** | Toggle Human ↔ AI controller |
| **R** | Restart after game over |
| **ESC** | Quit |

---

## 🤖 AI Controller

The AI controller:
- Evaluates all possible directions
- Filters out unsafe moves (walls, self-collision)
- Selects the move minimizing **Manhattan distance** to food
- Operates deterministically (same input → same outcome)

This design makes it trivial to:
- Replace with an ML model
- Wrap with reinforcement learning
- Collect trajectories for training

---

## 🧪 Tests

Unit tests cover:
- Collision detection
- Movement logic
- Core system behavior

Tests validate **engine correctness independent of rendering**.

---

## 🚀 Getting Started

### Requirements
- Python 3.10+
- pygame

### Install
```bash
pip install -r requirements.txt
````

### Run

```bash
python main.py
```

---

## 📁 Project Structure

```
.
├── engine/        # Game loop & timing
├── input/         # Human & AI controllers
├── render/        # Pygame renderer (read-only)
├── state/         # Game state (pure data)
├── systems/       # Game mechanics
├── tests/         # Unit tests
├── utils/         # Shared utilities & types
├── config.py      # Configuration
└── main.py        # Entry point
```

---

## 🔮 Future Extensions

* Reinforcement Learning agent
* Headless simulation mode
* Replay & trajectory logging
* Multi-agent environments
* Gym-style API wrapper

---

## 👨‍💻 Author

Built by **Albert Glenn**
Focused on **AI systems, clean architecture, and production-grade design**.

---

## 🧠 Takeaway

This project demonstrates how to:

* Design systems for **change**
* Separate **decision-making from mechanics**
* Build AI-ready environments from day one

Not just a game,  a **foundation**.

```













