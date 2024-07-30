#!/usr/bin/python3
"""
Island perimeter challenge.
"""


def island_perimeter(grid):
    """
    Initialize cell_perimeter = 4.
    For each cell checkUpSide, checkDownSide, checkLeftSide, checkRightSide.
    """
    grid_perimeter = 0
    for row_index, row in enumerate(grid):
        for cell_index, cell in enumerate(row):
            if cell == 1:
                grid_perimeter += 4
                if row_index == 0:
                    upper_row = None
                else:
                    upper_row = grid[row_index - 1]
                if row_index == len(grid) - 1:
                    lower_row = None
                else:
                    lower_row = grid[row_index + 1]
                current_row = row
                grid_perimeter += check_up_side(cell_index, upper_row)
                grid_perimeter += check_down_side(cell_index, lower_row)
                grid_perimeter += check_left_side(cell_index, current_row)
                grid_perimeter += check_right_side(cell_index, current_row)
    return grid_perimeter


def check_up_side(current_cell_index, upper_row):
    """
    Checks if there's a cell above it.
    Args:
        current_cell_index
        upper_row
    Returns -1 or 0
    """
    if not upper_row:
        return 0
    if upper_row[current_cell_index] == 1:
        return -1
    return 0


def check_down_side(current_cell_index, lower_row):
    if not lower_row:
        return 0
    if lower_row[current_cell_index] == 1:
        return -1
    return 0


def check_left_side(current_cell_index, current_row):
    previousCellIndex = current_cell_index - 1
    if previousCellIndex >= 0 and current_row[previousCellIndex] == 1:
        return -1
    return 0


def check_right_side(current_cell_index, current_row):
    nextCellIindex = current_cell_index + 1
    if nextCellIindex < len(current_row) and current_row[nextCellIindex] == 1:
        return -1
    return 0
