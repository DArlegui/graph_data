# 📓 Notes on `RandomWalk` Class

### Purpose

* Simulates a **random walk** — a path made by taking a sequence of random steps on a 2D plane.
* Useful for visualizing randomness, probability, or generating interesting paths.

---

### How It Works

1. **Initialization**

   * Start with `num_points` (default 5000).
   * First position is `(0,0)`.
   * Store positions in two lists: `x_values` and `y_values`.

2. **Filling the Walk (`fill_walk`)**

   * Repeat until we have `num_points` total coordinates.
   * For each step:

     * Pick a random **x direction**: `1` (right) or `-1` (left).
     * Pick a random **x distance**: `0–4`.
     * Multiply them → `x_step`.
     * Do the same for **y**: direction up/down, distance 0–4.
   * Skip the step if both `x_step` and `y_step` are `0` (no movement).
   * Otherwise, add the new step to the **last point** to get the new `(x,y)`.
   * Append the new coordinates to `x_values` and `y_values`.

---

### Important Details

* The walk **always starts at (0,0)**.
* Each new step starts from the **last recorded position** (not from 0,0 again).
* Steps can be:

  * Horizontal only (if `y_distance=0`).
  * Vertical only (if `x_distance=0`).
  * Diagonal (if both nonzero).
* Step size ranges from `1` to `4`.
* The walk can **cross itself** or **revisit the same point**.
* At the end, `x_values` and `y_values` contain the full path for plotting.

---

👉 In short: **This code makes a random squiggly path on graph paper, starting at (0,0), where each step is chosen randomly in direction and distance, and the entire history of the walk is stored for visualization.**

---
