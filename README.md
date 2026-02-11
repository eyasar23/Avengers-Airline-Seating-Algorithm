# 🛡️ Avengers Airline Seating Protocol

**A Python-based constraint satisfaction algorithm designed for Stark Industries.**

> *"Using Python logic to prevent a Civil War at 30,000 feet."*

## 📖 Project Overview
This project simulates an intelligent flight booking system designed to allocate seats for the **Avengers**. Unlike standard airline algorithms, this system must handle strict hierarchy rules, complex interpersonal conflicts (e.g., Thor vs. Loki), and safety protocols (e.g., Hulk's seating), all while parsing 2D cabin layouts represented as strings.

## ⚙️ The "Avengers Protocol" (Logic & Constraints)
The core of this project implements a **Priority Queue** and **Constraint Satisfaction System**. The algorithm processes passengers based on a strict rank and specific attributes:

### 🏆 Priority Hierarchy & Rules
The algorithm sorts heroes by rank (Disabled > Tony > Steve...) and assigns seats left-to-right based on availability and the following constraints:

| Rank | Hero | Code | Constraint / Behavior |
| :--- | :--- | :--- | :--- |
| **1** | **Disabled/Injured** | `D` | **Critical:** Must be assigned an **Aisle** seat immediately. |
| **2** | **Iron Man** | `T` | **First Class Only:** Refuses to fly otherwise. **Window Only.** |
| **3** | **Captain America** | `S` | **Tactical Leader:** Prioritizes **Middle** seats (Self-sacrifice trait). |
| **4** | **Black Widow** | `N` | **Duo Logic:** Prefers sitting with **Hawkeye (C)** in Business Class. |
| **5** | **The Hulk** | `B` | **Safety Protocol:** Must have an **Aisle** seat (for rapid exit). |
| **6** | **Thor** | `A` | **Preference:** Refuses Window seats.  **Conflict:** Cannot sit in the same row as **Loki (L)**. |
| **7** | **Hawkeye** | `C` | Flexible, but prioritizes duo-seating with Black Widow. |
| **8** | **Loki** | `L` | Wildcard. Triggers row-blocking logic for Thor. |

## 🧩 Visual Logic Walkthrough
Here is a step-by-step trace of how the algorithm solves a complex allocation scenario using the rules above.

### Scenario: First Class Allocation
* **Cabin Layout:** `O|OO|O` (Empty | Empty-Empty | Empty)
* **Passenger Manifest:** Iron Man (`T`), Hulk (`B`), Thor (`A`)

#### Step 1: Priority Sorting
The algorithm reorders the input string based on rank:
`Input: "TBA"` -> **Sorted: [Tony, Bruce, Thor]**

#### Step 2: Allocation Loop
1.  **Tony Stark (`T`) is up:**
    * *Constraint Check:* Needs Window.
    * *Scan:* Index 0 (`O|...`) is a Window.
    * *Action:* Assign `T`.
    * *Current State:* `T|OO|O`

2.  **Bruce Banner (`B`) is up:**
    * *Constraint Check:* Needs Aisle.
    * *Scan:* Index 1 is Aisle? No (Window adjacency logic). Index 2 is Aisle? Yes.
    * *Action:* Assign `B`.
    * *Current State:* `T|BO|O`

3.  **Thor (`A`) is up:**
    * *Constraint Check:* Refuses Window.
    * *Scan:* Remaining seat at Index 3 is Aisle (Valid).
    * *Action:* Assign `A`.
    * *Final State:* `T|BA|O`

#### ✅ Final Result: `T|BA|O`
*(Tony gets his view, Bruce gets his safety aisle, and Thor avoids the "portal".)*

## 📂 Repository Structure
The solution is modularized into three levels of algorithmic complexity:

- **`q1*.py` (Core Engine):**
  - Parses string-based cabin layouts (e.g., `WXA|AXXA|AXW`).
  - Implements basic linear allocation logic.

- **`q2*.py` (Heuristic Engine):**
  - Identifies seat metadata: **Window (W)**, **Aisle (A)**, or **Middle (M)** based on adjacency to separators (`|`).
  - Validates class-specific geometry (e.g., No middle seats in First Class).

- **`q3*.py` (The Solver):**
  - The advanced module containing the full **Avengers Protocol**.
  - Handles **Edge Cases**:
    - *Dynamic Duo:* Adjusting logic if Natasha & Clint board together.
    - *Conflict Resolution:* Backtracking if Thor and Loki end up in the same row.

## 🛠️ Technical Skills
- **String Manipulation:** Advanced slicing/reconstruction of immutable strings to simulate 2D arrays.
- **Algorithm Design:** Implementing priority queues and conditional logic trees.
- **Input Validation:** Robust error handling for invalid configurations or unrecognized characters.

---
**Status:** Completed  Project
**Language:** Python 3

