"""
Incremental Delaunay and Voronoi Diagram Visualization

Description:
This Python script visualizes the incremental construction of Delaunay triangulations
and Voronoi diagrams as a sequence of 2D points are added one at a time. It provides
an educational, step-by-step illustration of how these geometric structures evolve
with additional input data.

Key Features:
- Starts with 3 non-collinear fixed points to ensure valid triangulation.
- Incrementally adds random points to the 2D plane.
- Recomputes and renders Delaunay triangulation and Voronoi diagram at each step.
- Animates each frame to illustrate dynamic updates in the topology.
- Gracefully handles degenerate or invalid configurations.

Dependencies:
- numpy
- matplotlib
- scipy.spatial
"""

import matplotlib

matplotlib.use('TkAgg')

from matplotlib.axes import Axes

import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
from matplotlib.animation import FuncAnimation
from scipy.spatial import Voronoi, voronoi_plot_2d

# Seed the random number generator for reproducibility
np.random.seed(42)

POINT_COUNT = 1000
ANIMATION_INTERVAL_MS = 500

all_points = np.array([
    [0.2, 0.2],
    [0.8, 0.2],
    [0.5, 0.8],
    *np.random.rand(POINT_COUNT, 2)
])


def configure_axes(ax: Axes):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')


"""
update(frame: int)

Animation update callback for matplotlib FuncAnimation.

Parameters:
- frame (int): The current animation frame index, corresponding to the number of points included.

Behavior:
- Appends the next point from `all_points` to the current dataset.
- Clears and redraws the plot, updating:
    - Red point markers for each existing point.
    - Blue lines for Delaunay triangles.
    - Green lines for Voronoi cells.
- Handles exceptions if configurations are invalid for Delaunay/Voronoi computation.
"""


def main():
    fig, ax = plt.subplots()
    configure_axes(ax)
    ax.set_title("Incremental Delaunay Triangulation")

    current_points = []

    def update(frame):
        # Add the next point to the current set
        current_points.append(all_points[frame])
        ax.clear()

        # Reset the plot and configure axes for this frame
        configure_axes(ax)
        ax.set_title(f"Step {frame + 1}: {len(current_points)} Points")

        pts = np.array(current_points)
        ax.plot(pts[:, 0], pts[:, 1], 'ro')

        if len(pts) >= 3:
            try:
                # Draw Delaunay Diagram
                tri = Delaunay(pts)
                for triangle in tri.simplices:
                    simplex = pts[triangle]
                    simplex = np.vstack([simplex, simplex[0]])
                    ax.plot(simplex[:, 0], simplex[:, 1], 'b-')
                # Draw Voronoi Diagram
                try:
                    vor = Voronoi(pts)
                    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='green')
                except Exception as e:
                    print(f"Voronoi diagram failed at frame {frame}: {e}")
            except Exception as e:
                ax.set_title(f"Step {frame + 1}: Delaunay failed due to flat configuration\nError: {e}")
        return []

    _ = FuncAnimation(fig, update, frames=len(all_points), interval=ANIMATION_INTERVAL_MS, repeat=False)
    plt.show()


if __name__ == "__main__":
    main()
