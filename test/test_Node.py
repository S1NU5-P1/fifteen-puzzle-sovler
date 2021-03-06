from unittest import TestCase
import node
import numpy as np


class TestNode(TestCase):
    def setUp(self) -> None:
        self.test_board = np.array([[1, 2, 3, 4],
                                    [5, 6, 7, 8],
                                    [9, 10, 11, 12],
                                    [13, 14, 15, 0]])
        self.test_board_L = np.array([[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9, 10, 11, 12],
                                      [13, 14, 0, 15]])
        self.test_board_U = np.array([[1, 2, 3, 4],
                                      [5, 6, 7, 8],
                                      [9, 10, 11, 0],
                                      [13, 14, 15, 12]])

        self.test_Node = node.Node.get_node(self.test_board)

    def test_get_node(self):
        test_node = node.Node.get_node(self.test_board)
        np.testing.assert_array_equal(np.array([3, 3]), test_node.zero_position)
        test_node = node.Node.get_node(self.test_board_L)
        np.testing.assert_array_equal(np.array([2, 3]), test_node.zero_position)

    def test_apply_operator(self):
        child_node = self.test_Node.apply_operator("L")
        np.testing.assert_array_equal(self.test_board_L, child_node.board)
        np.testing.assert_array_equal(np.array([2, 3]), child_node.zero_position)
        self.assertEqual(self.test_Node, child_node.parent)
        self.assertEqual("L", child_node.last_operator)

    def test_apply_operator_out_of_board(self):
        self.assertRaises(node.NewPositionIsOutOfBoardException, self.test_Node.apply_operator, "R")
        self.assertRaises(node.NewPositionIsOutOfBoardException, self.test_Node.apply_operator, "D")

        child_node = self.test_Node.copy()
        for i in range(3):
            child_node = child_node.apply_operator("U")
            child_node = child_node.apply_operator("L")

        self.assertRaises(node.NewPositionIsOutOfBoardException, child_node.apply_operator, "U")
        self.assertRaises(node.NewPositionIsOutOfBoardException, child_node.apply_operator, "L")

    def test_is_goal(self):
        self.assertTrue(self.test_Node.is_goal())

    def test_get_neighbours(self):
        neighbours = self.test_Node.get_neighbours()
        self.assertEqual(2, len(neighbours))
        self.assertEqual(neighbours[0], self.test_Node.apply_operator("L"))
        self.assertEqual(neighbours[1], self.test_Node.apply_operator("U"))

        test_node = self.test_Node.apply_operator("L")
        test_node = test_node.apply_operator("U")
        neighbours = test_node.get_neighbours("UDLR")

        self.assertEqual(neighbours[0], test_node.apply_operator("U"))
        self.assertEqual(neighbours[1], test_node.apply_operator("D"))
        self.assertEqual(neighbours[2], test_node.apply_operator("L"))
        self.assertEqual(neighbours[3], test_node.apply_operator("R"))

    def test_operator_to_string(self):
        self.assertEqual("L", str("L"))
        self.assertEqual("R", str("R"))
        self.assertEqual("U", str("U"))
        self.assertEqual("D", str("D"))

    def test_path(self):
        self.test_Node = self.test_Node.apply_operator("U")
        self.test_Node = self.test_Node.apply_operator("U")
        self.test_Node = self.test_Node.apply_operator("L")
        self.test_Node = self.test_Node.apply_operator("L")
        self.test_Node = self.test_Node.apply_operator("D")
        self.test_Node = self.test_Node.apply_operator("D")

        self.assertEqual("UULLDD", self.test_Node.path)
