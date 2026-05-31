# README


## Installation

Install required libraries:

```bash
pip install networkx matplotlib pgmpy
```

All other files use only Python's standard library.

---

## Files & How to Run

### 1. `minimax.py` — Minimax Algorithm
Tic-Tac-Toe with Human vs AI. The AI explores all possible game states and picks the move that minimises the human's chances of winning.

```bash
python minimax.py
```

**Key concept:** Minimax builds a full game tree. The AI maximises its own score; the human minimises it.

---

### 2. `alpha_beta.py` — Alpha-Beta Pruning
Same as Minimax but skips branches that can't possibly affect the final decision. Faster, same result.

```bash
python alpha_beta.py
```

**Key concept:** `alpha` = best score AI is guaranteed. `beta` = best score Human is guaranteed. If `beta <= alpha`, prune the branch.

---

### 3. `alphabeta_heuristic.py` — Heuristic Alpha-Beta (Depth-Limited)
Alpha-Beta with a depth limit. When the search hits the limit, it uses a **heuristic function** to estimate how good the board looks instead of searching further.

```bash
python alphabeta_heuristic.py
```

**Key concept:** Useful for complex games (chess, etc.) where you can't search all the way to the end. The heuristic here counts open winning lines.

---

### 4. `montecarlo.py` — Monte Carlo Tree Search (MCTS)
Instead of calculating exact scores, MCTS runs hundreds of **random simulations** from each possible move and picks the one with the best win rate.

```bash
python montecarlo.py
```

**Key concept:** No tree traversal logic needed — just simulate random games and count outcomes. Works surprisingly well.

---

### 5. `trip_planning.py` — Rule-Based Travel Recommender
An AI travel assistant. You enter your budget, climate preference, and interests, and it scores destinations from a small knowledge base and recommends the top 3.

```bash
python trip_planning.py
```

**Key concept:** Rule-based AI — no ML needed. Scoring based on attribute matching.

---

### 6. `KG_and_KB_example.py` — Knowledge Graph
Builds a knowledge graph about animals using **NetworkX**. Nodes are entities (Dog, Bird, etc.) and edges are labelled relationships (is-a, has-property). Saves a visual PNG.

```bash
python KG_and_KB_example.py
```

**Key concept:** Knowledge Graphs represent facts as (Subject, Relation, Object) triples. Querying = traversing edges.

> Output: `knowledge_graph.png`

---

### 7. `bayesian.py` — Bayesian Network
Models the relationship between Flu, Fever, and Cough using **pgmpy**. Defines prior probabilities and conditional probability tables (CPTs), then runs inference queries like "What is P(Flu | Fever=Yes)?"

```bash
python bayesian.py
```

**Key concept:** Bayesian Networks use probability to reason under uncertainty. Evidence (symptoms) updates our belief about causes (disease).

---

## Quick Reference

| File | Algorithm | Library |
|------|-----------|---------|
| minimax.py | Minimax | None |
| alpha_beta.py | Alpha-Beta Pruning | None |
| alphabeta_heuristic.py | Heuristic Alpha-Beta | None |
| montecarlo.py | MCTS | None (random) |
| trip_planning.py | Rule-based AI | None |
| KG_and_KB_example.py | Knowledge Graph | networkx, matplotlib |
| bayesian.py | Bayesian Network | pgmpy |
