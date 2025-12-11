#!/usr/bin/env python3
"""
Conway's Game of Life Implementation.

This module provides a class to simulate Conway's Game of Life and a CLI interface
to run the simulation in the terminal.
"""

import sys
import time
import random
import argparse
import os
from typing import List, Tuple, Set

class GameOfLife:
    """
    Represents the grid and logic for Conway's Game of Life.
    """

    def __init__(self, width: int = 40, height: int = 20, randomize: bool = True):
        """
        Initialize the game board.

        Args:
            width: Width of the grid.
            height: Height of the grid.
            randomize: Whether to start with a random pattern.
        """
        self.width = width
        self.height = height
        self.board: Set[Tuple[int, int]] = set()

        if randomize:
            self.randomize_board()

    def randomize_board(self, density: float = 0.2):
        """Populates the board with random live cells."""
        self.board.clear()
        for y in range(self.height):
            for x in range(self.width):
                if random.random() < density:
                    self.board.add((x, y))

    def set_pattern(self, pattern: List[Tuple[int, int]], offset_x: int = 0, offset_y: int = 0):
        """Sets a specific pattern of live cells."""
        for x, y in pattern:
            self.board.add((x + offset_x, y + offset_y))

    def get_neighbors(self, x: int, y: int) -> int:
        """Calculates the number of live neighbors for a cell."""
        count = 0
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Wrap around (toroidal grid) behavior could be added here,
                # but we'll stick to infinite/bounded plane logic where off-grid is dead.
                if (nx, ny) in self.board:
                    count += 1
        return count

    def next_generation(self):
        """
        Computes the next state of the board based on the rules:
        1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        2. Any live cell with two or three live neighbours lives on to the next generation.
        3. Any live cell with more than three live neighbours dies, as if by overpopulation.
        4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        new_board = set()
        candidates = set()

        # Only check existing live cells and their immediate neighbors
        for x, y in self.board:
            candidates.add((x, y))
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    candidates.add((x + dx, y + dy))

        for x, y in candidates:
            # Optional: constrain to grid boundaries for display purposes
            if not (0 <= x < self.width and 0 <= y < self.height):
               continue

            neighbors = self.get_neighbors(x, y)
            is_alive = (x, y) in self.board

            if is_alive and (neighbors == 2 or neighbors == 3):
                new_board.add((x, y))
            elif not is_alive and neighbors == 3:
                new_board.add((x, y))

        self.board = new_board

    def __str__(self) -> str:
        """Returns a string representation of the current board state."""
        output = []
        border = "+" + "-" * self.width + "+"
        output.append(border)
        for y in range(self.height):
            row = ["|"]
            for x in range(self.width):
                if (x, y) in self.board:
                    row.append("O") # Live cell
                else:
                    row.append(" ") # Dead cell
            row.append("|")
            output.append("".join(row))
        output.append(border)
        return "\n".join(output)

def clear_screen():
    """Clears the terminal screen."""
    if os.name == 'nt':
        os.system('cls')
    else:
        # Standard ANSI escape sequence to clear screen and move cursor to top-left
        sys.stdout.write("\033[2J\033[H")

def main():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument("--width", type=int, default=40, help="Grid width")
    parser.add_argument("--height", type=int, default=20, help="Grid height")
    parser.add_argument("--fps", type=int, default=10, help="Frames per second")
    parser.add_argument("--generations", type=int, default=100, help="Max generations to run")
    parser.add_argument("--glider", action="store_true", help="Start with a glider pattern")

    args = parser.parse_args()

    game = GameOfLife(width=args.width, height=args.height, randomize=not args.glider)

    if args.glider:
        # Clear random initialization if any
        game.board.clear()
        # Glider pattern
        glider = [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
        game.set_pattern(glider, offset_x=2, offset_y=2)

    try:
        for gen in range(args.generations):
            clear_screen()
            print(f"Generation: {gen + 1}")
            print(game)
            game.next_generation()
            time.sleep(1.0 / args.fps)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
