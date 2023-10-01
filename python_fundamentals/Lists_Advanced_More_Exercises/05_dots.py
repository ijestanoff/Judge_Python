rows = int(input())
maze = [list(input().split()) for i in range(rows)]
spaces = []  # possible spaces to move to
dots = 0  # dots and dots_max will help me keep memory of the dots and choose the group with max dots
dots_max = 0
position = [0, 0]  # target position


def find_dots(position_, maze_space):
    dot_up = []
    dot_right = []
    dot_down = []
    dot_left = []
    if position_[0] != 0 and maze_space[position_[0] - 1][position_[1]] == '.':
        dot_up = [position_[0] - 1, position_[1]]
    if position_[1] < (len(maze_space[position_[0]]) - 1) and maze_space[position_[0]][position_[1] + 1] == '.':
        dot_right = [position_[0], position_[1] + 1]
    if position_[0] < (len(maze_space) - 1) and maze_space[position_[0] + 1][position_[1]] == '.':
        dot_down = [position_[0] + 1, position_[1]]
    if position_[1] != 0 and maze_space[position_[0]][position_[1] - 1] == '.':
        dot_left = [position_[0], position_[1] - 1]
    return [dot_up, dot_right, dot_down, dot_left]
    # list of available dots in each direction


def move(position_, spaces_, visited_, maze_, dots_):
    for i in range(len(spaces_)):  # all available spaces around target, spaces_ is the output from def find_dots
        if spaces_[i] not in visited_ and bool(spaces_[i]):  # if the space is not visited and is free
            position_ = spaces_[i]  # target moves there
            visited_.append(spaces_[i])
            return position_, visited_, dots_

        elif all(i in visited_ for i in
                 list(filter(lambda x: bool(x), spaces_))):  # if all available spaces are already visited
            maze_[position_[0]][position_[1]] = '@'
            # target marks the space with @ BECAUSE this position doesn't lead to any new spaces
            position_ = visited_[-2]  # target moves one step back
            del visited_[-1]  # target removes the marked with @ space from the visited spaces as
            # it is clearly a dead end and from now on will be part of the Maze dashes
            dots_ += 1  # as the target moves back, we increase dots
            return position_, visited_, dots_


for row in range(rows):
    for col in range(len(maze[0])):
        if maze[row][col] == '.':
            position[0], position[1] = row, col
            dots = 1
            visited = [[position[0], position[1]]]  # all spaces that target has visited
            while True:
                spaces = find_dots(position, maze)  # check where target can go to collect dots
                if not sum((lambda x: bool(x))(x) for x in spaces):
                    dots_max = max(dots_max, dots)
                    break
                position, visited, dots = move(position, spaces, visited, maze, dots)
print(dots_max)
