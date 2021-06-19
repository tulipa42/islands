def is_checked_already(row, col, part_of_island):
    '''
    If already known that 
    it is a part of an island,
    no further recursive are needed.
    '''

    return (row, col) in part_of_island


def is_part_of_island(row, col, image, part_of_island, start_rc=[]):

    if image[row][col] == 0:
        return False

    if row in [0, len(image) - 1] or col in [0, len(image[0]) - 1]:
        # if at the edge
        return True

    left, top, right, bottom = (row, col - 1), (row - 1, col), (row, col +1), (row + 1, col)

    for r, c in [left, top, right, bottom]:
        # append to this array all the cells already checked - so it doens't loop
        start_rc.append((row, col))
        if (r, c) not in start_rc and (is_checked_already(r, c, part_of_island) or is_part_of_island(r, c, image, part_of_island, start_rc=start_rc)):
            return True

    return False


def islands(image):

    part_of_island = []
    new_image = image

    for row, row_array in enumerate(image):
        for col, value in enumerate(row_array):
            if is_part_of_island(row, col, image, part_of_island, start_rc=[]):
                part_of_island.append((row, col))

    for row, row_array in enumerate(image):
        for col, value in enumerate(row_array):
            if (row, col) not in part_of_island:
                new_image[row][col] = 0

    return new_image


image1 = [
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1]
]

image_outcome1 = [
    [0,1,0,0,1],
    [0,0,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,1]
]

image2 = [
    [0,1,1,0,1,1,1,0,1],
    [0,0,1,0,1,0,0,0,1],
    [1,1,0,1,0,1,1,1,1],
    [0,0,1,0,0,0,1,0,1],
    [0,0,0,0,1,1,0,0,1],
    [0,0,1,0,1,1,0,0,1],
    [0,0,1,0,0,0,1,0,1]
]

image_outcome2 = [
    [0,1,1,0,1,1,1,0,1],
    [0,0,1,0,1,0,0,0,1],
    [1,1,0,0,0,1,1,1,1],
    [0,0,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,0,0,1],
    [0,0,1,0,0,0,0,0,1],
    [0,0,1,0,0,0,1,0,1]
]

#print(islands(image2))

assert(islands(image1) == image_outcome1)
assert(islands(image2) == image_outcome2)