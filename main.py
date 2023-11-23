# Press Shift+F10 to execute it or replace it with your code.


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import numpy as np

    # Number of particles
    num_particles = 20

    # Initialize particle positions and velocities randomly
    particle_positions = np.random.rand(num_particles, 2)  # 2D space
    particle_velocities = np.random.rand(num_particles, 2) * 0.1  # Random small velocities

    # Initialize plot
    plt.figure(figsize=(6, 6))

    # Perform particle movement updates and visualize
    for i in range(100):  # Example: 100 iterations
        # Update particle positions
        particle_positions += particle_velocities

        # Plot particles' positions
        plt.clf()
        plt.scatter(particle_positions[:, 0], particle_positions[:, 1], label='Particles')
        plt.title(f'Iteration {i + 1}')
        plt.legend()
        plt.xlim(0, 1)  # Adjust x-axis limit if needed
        plt.ylim(0, 1)  # Adjust y-axis limit if needed
        plt.pause(0.1)  # Pause to visualize updates (adjust as needed)
        plt.draw()

    plt.show()
