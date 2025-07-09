# 🚚 Optimal Route Planner

**Optimal Route Planner** leverages [Google OR-Tools](https://developers.google.com/optimization/) to solve the Vehicle Routing Problem (VRP): finding the most efficient routes for a fleet of vehicles to visit a set of locations.

---

## 📂 Getting Started

- **Main Script:**  
  The core logic is in [`ortools.py`](ortools.py).

- **Distance Matrix:**  
  Input is read from an Excel file (`dist_mtrx.xlsx`) containing the pairwise distances between locations.

---

## ✨ Features

- **Route Optimization:**  
  Calculates optimal routes for multiple vehicles, minimizing total travel distance.

- **Flexible Fleet Size:**  
  Easily adjust the number of vehicles (targets) to experiment with different routing scenarios.

- **Detailed Output:**  
  Prints each vehicle's route, total distance, and the maximum route distance.

---

## 🧩 How It Works (Step by Step)

1. **Read Distance Matrix:**  
   Loads the distance matrix from `dist_mtrx.xlsx` using pandas.

2. **Define the Routing Problem:**  
   - Sets up the number of vehicles and the depot (starting location).
   - Prepares the data model for OR-Tools.

3. **Create Routing Model:**  
   - Uses OR-Tools to create a routing index manager and routing model.
   - Registers a callback to fetch distances between locations.

4. **Set Constraints and Parameters:**  
   - Defines the cost function (distance).
   - Adds constraints (e.g., maximum route distance).
   - Sets search parameters (strategy, time limit, logging).

5. **Initial Solution:**  
   - Optionally provides an initial guess for the routes.

6. **Solve the Problem:**  
   - OR-Tools searches for the optimal set of routes.

7. **Display Results:**  
   - Prints each vehicle's route and distance.
   - Shows the maximum distance among all routes.

---

## 🛠️ What is OR-Tools?

[OR-Tools](https://developers.google.com/optimization/) is an open-source operations research suite by Google. It can solve:

- Vehicle Routing Problems (VRP)
- Traveling Salesman Problem (TSP)
- Scheduling, assignment, and constraint programming problems

It's widely used for logistics, transportation, and supply chain optimization.

---

## 📚 References

- [OR-Tools Routing Tasks (Python)](https://developers.google.com/optimization/routing/routing_tasks#python)
- [GitHub Issue #3398](https://github.com/google/or-tools/issues/3398)
- [GitHub Issue #1180](https://github.com/google/or-tools/issues/1180)
- [Stack Overflow: Vehicle Routing Problem](https://stackoverflow.com/questions/59389623/vehicle-routing-problem-how-to-call-data)
