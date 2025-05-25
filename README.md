# Incremental Delaunay and Voronoi Visualization
This Python project visualizes the **step-by-step construction** of two important 2D geometric structures: **Delaunay Triangulation** and **Voronoi Diagram**.

## What It Does
- Starts with a few predefined 2D points and adds random points incrementally.
- Recomputes and redraws:
  - **Delaunay Triangulation** (shown in blue)
  - **Voronoi Diagram** (shown in green)
- Uses `matplotlib.animation` to animate the process frame by frame.

## Delaunay & Voronoi Diagrams

### Delaunay Triangulation
A triangulation where no point is inside the **circumcircle** of any triangle. It creates well-shaped triangles and is useful in mesh generation, interpolation, and graphics.

### Voronoi Diagram
Divides the plane into regions based on proximity to a set of points. Each cell contains the area closer to one specific point than any other — common in geography, biology, and network planning.

## 🛠 Requirements
- Python 3.7+
- `numpy`
- `matplotlib`
- `scipy`

Install dependencies using:
```bash
pip install -r requirements.txt
