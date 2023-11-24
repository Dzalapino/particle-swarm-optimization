if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np
    from swarm import Swarm
    from vector2 import Vector2

    # Function too check
    def function(vector: Vector2):
        return (
                np.power((1.5 - vector.x - vector.x * vector.y), 2) +
                np.power((2.25 - vector.x + vector.x * np.power(vector.y, 2)), 2) +
                np.power((2.625 - vector.x + vector.x * np.power(vector.y, 3)), 2)
        )


    swarm = Swarm(function, 100, (-4.5, 4.5), 1.0, 0.2, 0.05, 5, 7.5)

    # Init contour plot with the global minimum
    x, y = np.array(np.meshgrid(np.linspace(-4.5, 4.5, 300), np.linspace(-4.5, 4.5, 300)))
    z = function(Vector2(x, y))
    x_min = x.ravel()[z.argmin()]
    y_min = y.ravel()[z.argmin()]
    plt.figure(figsize=(8, 6))
    plt.imshow(z, extent=(-4.5, 4.5, -4.5, 4.5), origin='lower', cmap='viridis', alpha=0.5)
    plt.colorbar()
    scatter = plt.scatter([], [], color='blue', label=f'Particles (n = {len(swarm.particles)})')
    # Mark minimum by the white cross
    plt.plot(
        [x_min], [y_min], marker='x', markersize=5, color="white",
        label=f'objective_best({x_min:.3f}, {y_min:.3f})={function(Vector2(x_min, y_min)):.4f}'
    )
    contours = plt.contour(x, y, z, 10, colors='black', alpha=0.4)
    plt.clabel(contours, inline=True, fontsize=8, fmt="%.0f")
    # Mark g_best by the black cross
    global_best_cross, = plt.plot([], [], marker='x', markersize=5, color="black", label='')

    # Perform particle movement updates and visualize
    for i in range(200):  # for n iterations
        # Plot particles positions
        scatter.set_offsets(np.column_stack((swarm.get_x_positions(), swarm.get_y_positions())))
        # Mark new g_best
        global_best_cross.set_data(swarm.global_best.x, swarm.global_best.y)
        global_best_cross.set_label(
            f'g_best({swarm.global_best.x:.3f}, {swarm.global_best.y:.3f})={function(swarm.global_best):.4f}'
        )

        plt.title(f'Iteration {i + 1}')
        plt.legend(loc='upper left')

        plt.pause(0.2)  # Pause to visualize updates
        plt.draw()

        swarm.update_particles()  # Update swarm

    plt.show()
