from unittest import TestCase

import numpy as np

import bfs
from node import Node


class algorithm_test(TestCase):
    test_nodes = []
    test_board_0 = np.array([
        [1, 2, 3, 4],
        [5, 6, 0, 8],
        [9, 11, 7, 12],
        [13, 10, 14, 15]
    ])
    test_nodes.append(Node.get_node(test_board_0))

    test_board_1 = np.array([
        [1, 2, 3, 4],
        [0, 5, 7, 8],
        [9, 6, 10, 11],
        [13, 14, 15, 12]
    ])
    test_nodes.append(Node.get_node(test_board_1))

    test_board_2 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 10, 12],
        [13, 14, 11, 15]
    ])
    test_nodes.append(Node.get_node(test_board_2))

    test_board_3 = np.array([
        [1, 2, 0, 4],
        [5, 6, 3, 8],
        [9, 10, 7, 11],
        [13, 14, 15, 12]
    ])
    test_nodes.append(Node.get_node(test_board_3))

    test_board_4 = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [0, 9, 10, 11],
        [13, 14, 15, 12]
    ])
    test_nodes.append(Node.get_node(test_board_4))
    test_nodes.append(Node.get_node(test_board_2))

    def test_bfs_algorithm(self):
        try:
            result = bfs.bfs_algorithm(self.test_nodes[0])
        except:
            self.fail("Couldn't find solution")
        else:
            self.assertTrue(result.is_goal())
