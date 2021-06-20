from typing import List, Tuple

Image = List[List[int]]
Coordinates = Tuple[int, int]

def is_edge(row: int, col: int, image: Image) -> bool:
    '''
    Trivial case for keeping the coordinates.
    '''

    return row in [0, len(image) - 1] or col in [0, len(image[0]) - 1]


def in_to_keep(row: int, col: int, to_keep: List[Coordinates]) -> bool:
    '''
    Check if the coordinates are already checked before.
    '''

    return (row, col) in to_keep


def keep(row: int, col: int, image: Image, to_keep: List[Coordinates], part_of_cycle: List[Coordinates] = []) -> bool:
    '''
    Checks if a coordinate is *not* part of an island. If not, then return True, because we want to keep the 1.
    '''

    if image[row][col] == 0:
        # Coordinate can't be part of an island if it is zero.
        return False

    if is_edge(row, col, image):
        # The edge is not an island.
        return True

    left = (row, col - 1)
    top = (row - 1, col)
    right = (row, col + 1)
    bottom = (row + 1, col)

    for r, c in [left, top, right, bottom]:
        # Check if either of the adjacent cells are connected to the edge.
        part_of_cycle.append((row, col))  # Remember which coordinates are part of this recursion cycle
        if (r, c) not in part_of_cycle:
            # Check these coordinates ONLY if they are NOT part of the cycle.
            if in_to_keep(r, c, to_keep) or keep(r, c, image, to_keep, part_of_cycle):
                # If they are already in to_keep array, then True
                # Check if the coordinates are to keepby calling this function again.
                return True

    return False


def islands(image: Image) -> Image:
    '''
    Remove island from the image and return the image without islands.
    '''

    to_keep: List[Coordinates] = []
    new_image = image.copy()  # Make a copy of the original image

    for row, row_array in enumerate(image):
        for col, value in enumerate(row_array):
            if keep(row, col, image, to_keep, part_of_cycle=[]):
                to_keep.append((row, col))

    for row, row_array in enumerate(image):
        for col, value in enumerate(row_array):
            if (row, col) not in to_keep:
                new_image[row][col] = 0

    return new_image
