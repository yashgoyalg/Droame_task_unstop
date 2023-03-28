import pygame
import math
import time
from queue import PriorityQueue

# Set the dimensions of the grid
GRID_WIDTH = 20
GRID_HEIGHT = 20

# Set the size of each cell in the grid
CELL_SIZE = 30

# Set the radius of each drone
DRONE_RADIUS = 5

# Set the colors for the drones and obstacles
DRONE_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
PATH_COLOR = (0, 0, 255)

# Set the speed of the simulation
FPS = 60

# Define the Node class to represent each cell in the grid
class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = col * CELL_SIZE + CELL_SIZE // 2
        self.y = row * CELL_SIZE + CELL_SIZE // 2
        self.color = (255, 255, 255)
        self.neighbors = []
        self.obstacle = False
        self.visited = False

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), CELL_SIZE // 2)

    def add_neighbors(self, grid):
        if self.row > 0:
            self.neighbors.append(grid[self.row - 1][self.col])
            if self.col > 0:
                self.neighbors.append(grid[self.row - 1][self.col - 1])
            if self.col < GRID_WIDTH - 1:
                self.neighbors.append(grid[self.row - 1][self.col + 1])
        if self.row < GRID_HEIGHT - 1:
            self.neighbors.append(grid[self.row + 1][self.col])
            if self.col > 0:
                self.neighbors.append(grid[self.row + 1][self.col - 1])
            if self.col < GRID_WIDTH - 1:
                self.neighbors.append(grid[self.row + 1][self.col + 1])
        if self.col > 0:
            self.neighbors.append(grid[self.row][self.col
