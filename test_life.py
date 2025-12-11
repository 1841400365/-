import unittest
from life import GameOfLife

class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.game = GameOfLife(width=10, height=10, randomize=False)

    def test_underpopulation(self):
        # 1. Any live cell with fewer than two live neighbours dies
        self.game.board = {(5, 5)} # Single cell
        self.game.next_generation()
        self.assertNotIn((5, 5), self.game.board)

    def test_survival(self):
        # 2. Any live cell with two or three live neighbours lives
        # Create a block (stable)
        # OO
        # OO
        block = {(5, 5), (6, 5), (5, 6), (6, 6)}
        self.game.board = block.copy()
        self.game.next_generation()
        self.assertEqual(self.game.board, block)

    def test_overpopulation(self):
        # 3. Any live cell with more than three live neighbours dies
        # Cross pattern where center has 4 neighbors
        #  O
        # OXO
        #  O
        center = (5, 5)
        neighbors = {(5, 4), (4, 5), (6, 5), (5, 6)}
        self.game.board = neighbors.union({center})
        self.game.next_generation()
        # Center should die
        self.assertNotIn(center, self.game.board)

    def test_reproduction(self):
        # 4. Any dead cell with exactly three live neighbours becomes a live cell
        # Blinker (horizontal) -> Vertical
        # OOO -> becomes vertical
        blinker = {(4, 5), (5, 5), (6, 5)}
        self.game.board = blinker
        self.game.next_generation()

        expected = {(5, 4), (5, 5), (5, 6)}
        self.assertEqual(self.game.board, expected)

    def test_glider_logic(self):
        # Glider moves diagonally
        # .O.
        # ..O
        # OOO
        glider_t0 = {(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)}
        self.game.board = glider_t0

        # Run 4 generations, it should shift (1, 1)
        for _ in range(4):
            self.game.next_generation()

        glider_t4 = {(x+1, y+1) for x, y in glider_t0}
        self.assertEqual(self.game.board, glider_t4)

if __name__ == '__main__':
    unittest.main()
