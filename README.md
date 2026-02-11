# 🛡️ Avengers Airline Seating Protocol

**A sophisticated Python-based seating allocation algorithm designed for Stark Industries.**

> *"Using Python logic to prevent a Civil War at 30,000 feet."*

## 📖 Project Overview
This project simulates an intelligent flight booking system capable of handling complex seating arrangements and strict priority constraints. The algorithm parses string-based cabin layouts (representing First, Business, and Economy classes) and assigns seats to passengers—specifically the **Avengers**—based on a hierarchy of rules, personal preferences, and safety protocols.

## ⚙️ How It Works (The Logic)
The system represents the airplane cabin using **2D-like string structures**:
- `O`: Empty Seat
- `X`: Occupied Seat
- `|`: Aisle Divider
- `H`: Hero (Newly Assigned)

**Example Input:** `WXA|AXXA|AXW` (Window-Occupied-Aisle | Aisle-Occupied-Occupied-Aisle | ...)

The algorithm processes these strings to solve allocation problems in three distinct stages of complexity:

### 🧩 Part 1: Basic Allocation Logic
* **Goal:** Fill empty seats sequentially from left to right.
* **Challenge:** Parsing strings with variable row lengths (1-2-1 vs 3-4-3 configurations) while ignoring aisle markers (`|`).

### 🪟 Part 2: Preference Management
* **Goal:** Assign seats based on specific requests: **Window (W)**, **Aisle (A)**, or **Middle (M)**.
* **Logic:** The code identifies seat types based on their position relative to the aisle markers (`|`) and boundary indices.
* **Validation:** Ensures a passenger requesting a "Middle" seat isn't placed in First Class (where no middle seats exist).

### ⚡ Part 3: The "Avengers Protocol" (Complex Constraints)
This is the core of the project. The algorithm implements a **Priority Queue** and **Constraint Satisfaction System** to seat heroes based on their rank and specific traits:

| Rank | Hero / Group | Constraint Implemented |
| :--- | :--- | :--- |
| **1 (Highest)** | **Disabled/Injured** | Must be seated in an **Aisle** seat for accessibility. |
| **2** | **Iron Man (Tony Stark)** | Must be in **First Class**, **Window** seat only. (Refuses to fly otherwise). |
| **3** | **Captain America** | Prefers **Middle** seats (Self-sacrifice trait). |
| **4** | **The Hulk (Bruce Banner)** | Must have an **Aisle** seat (Safety measure for... incidents). |
| **5** | **Thor** | Refuses Window seats (Dislikes "portals"). **Cannot sit in the same row as Loki.** |
| **6** | **Black Widow & Hawkeye** | Dynamic duo preference: They prefer sitting together in Business Class. |

## 📂 Repository Structure

| File | Component | Description |
| :--- | :--- | :--- |
| `q1*.py` | **Basic Engine** | Handles linear seat filling and string parsing. |
| `q2*.py` | **Preference Engine** | Logic for detecting Window/Aisle/Middle attributes. |
| `q3*.py` | **Priority Engine** | The complex Avengers logic handling conflicts and edge cases. |
| `*_test.py` | **Unit Tests** | *Provided by instructors* to validate edge cases and algorithmic correctness. |

> **⚠️ Academic Integrity Note:** The test files (`*_test.py`) were provided as part of the project specification. All algorithmic logic, string manipulation, and solution code in `q1`, `q2`, and `q3` files were developed by me.

## 🛠️ Technical Skills Demonstrated
- **String Manipulation:** Advanced slicing and concatenation to modify immutable string structures.
- **Conditional Logic:** Handling conflicting constraints (e.g., "Seat Thor, but ensure Loki isn't in the row").
- **Input Validation:** robust error handling for invalid cabin configurations or unrecognized characters.

## 🚀 Usage Example

```python
from q3a import can_allocate_priority_seats

# Scenario: Seating Tony Stark (T), Bruce Banner (B), and Thor (A) in First Class
# Layout: Empty | Empty-Empty | Empty
cabin_layout = "O|OO|O"
heroes = "TBA"

# The algorithm places Tony (Window), Bruce (Aisle), Thor (Aisle - Not Window)
result = show_priority_seats("First", cabin_layout, heroes)
print(result)

# Output: 'T|BA|O'
