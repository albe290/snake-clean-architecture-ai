
# 🐍 Snake AI (Clean Architecture)

A **deterministic Snake simulation engine** built with **clean architecture principles** and **pluggable controllers**, designed as an **AI-ready environment** rather than a simple game clone.

This project demonstrates how to build **maintainable, testable, and extensible systems** where game logic, rendering, timing, and decision-making are fully decoupled.

---

## 🎯 Why This Project Exists

Most Snake implementations tightly couple:

* input handling
* game logic
* rendering
* timing

This repository intentionally **separates concerns** so the engine can support:

* Human players
* Heuristic AI agents
* Future ML / RL agents
* Deterministic replay and simulation

It is designed as a **simulation engine first**, game second.

---

## ✨ Key Features

* ✅ **Deterministic tick-based simulation** (engine ≠ FPS)
* ✅ **Clean Architecture Layering**

  * `state` → pure data only
  * `systems` → rules & mechanics
  * `engine` → orchestration & timing
  * `input` → controllers (Human / AI)
  * `render` → read-only visualization
* ✅ **Hot-swappable controllers**

  * Press **`T`** to switch **Human ↔ AI** mid-game
* ✅ **Heuristic AI controller**

  * Policy-based (no randomness)
  * Collision-aware
  * Food-seeking behavior
* ✅ **Renderer contains zero game logic**
* ✅ **Pause-safe & restart-safe**
* ✅ **AI / RL-ready environment**
* ✅ **Unit-tested core systems**

---

## 🧠 Architecture Overview

<p align="center">
  <img src="docs/Snake%20diagram.png" alt="Snake AI Clean Architecture Diagram" width="900"/>
</p>

The diagram above illustrates how inputs, systems, and state are orchestrated by a deterministic engine, while rendering remains a pure read-only concern.

---

## 🎥 Controller Demos

This project supports **hot-swappable controllers** that can be changed **at runtime** without restarting the engine.

### 🧑 Human Controller

Manual control using keyboard input, demonstrating direct human interaction with the deterministic simulation.

📹 **Watch demo:**
[Human Controller Demo](docs/Human-controller.mp4)

---

### 🤖 AI Controller

A deterministic, heuristic-based AI that navigates toward food while avoiding walls and self-collisions.

📹 **Watch demo:**
[AI Controller Demo](docs/AI-controller.mp4)

---

💡 Press **`T`** during gameplay to toggle between **Human** and **AI** controllers in real time.

---

## 🎮 Controls

| Key        | Action                       |
| ---------- | ---------------------------- |
| Arrow Keys | Move (Human controller)      |
| **T**      | Toggle Human ↔ AI controller |
| **R**      | Restart after game over      |
| **ESC**    | Quit                         |

---

## 🤖 AI Controller

The AI controller operates **deterministically** and follows a transparent policy:

* Evaluates all possible movement directions
* Filters out unsafe moves (walls, self-collision)
* Selects the move minimizing **Manhattan distance** to food
* Produces identical outcomes given identical state

This design makes it trivial to:

* Replace heuristics with ML models
* Wrap the environment with reinforcement learning
* Collect trajectories for training
* Support explainable decision-making

---

## 🧪 Tests

Unit tests cover:

* Collision detection
* Movement logic
* Core system behavior

Tests validate **engine correctness independently of rendering**, reinforcing the simulation-first design.

---

## 🚀 Getting Started

### Requirements

* Python **3.10+**
* `pygame`

### Install

```bash
pip install -r requirements.txt
```

### Run

```bash
python main.py
```

---

## 📁 Project Structure

```
.
├── engine/     # Game loop & deterministic timing
├── input/      # Human & AI controllers
├── render/     # Pygame renderer (read-only)
├── state/      # Game state (pure data)
├── systems/    # Game mechanics
├── tests/      # Unit tests
├── utils/      # Shared utilities & types
├── config.py   # Configuration
└── main.py     # Entry point
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
* Build **AI-ready environments** from day one

Not just a game a **foundation**.

---



