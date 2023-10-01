rows = int(input())
maze = [list(input()) for i in range(rows)]
get_out_flag = False  # Flag to notify if Kate cant get out
spaces = []  # possible spaces to move to
steps = 0  # steps and old_steps will help me keep memory of the routs lenghts and choose the longest
steps_old = -1  # because if K is on the edge of the Maze she is already at possible exit position, and
# i need invalid value for old steps

for i in range(rows):  # find Kate
    if 'k' in maze[i]:
        kate_position = [i, maze[i].index('k')]
        break

maze[kate_position[0]][kate_position[1]] = ' '  # make the space occupied by Kate as a free space to move over
# in case a closed path was chosen and a new one is needed that passes
# through K's initial position

visited = [[kate_position[0], kate_position[1]]]  # all spaces that Kate has visited


def find_space(kate_pos, maze_space):
    space_up = []
    space_right = []
    space_down = []
    space_left = []
    if kate_pos[0] != 0 and maze_space[kate_pos[0] - 1][kate_pos[1]] == ' ':
        space_up = [kate_pos[0] - 1, kate_pos[1]]
    if kate_pos[1] < (len(maze_space[kate_pos[0]]) - 1) and maze_space[kate_pos[0]][kate_pos[1] + 1] == ' ':
        space_right = [kate_pos[0], kate_pos[1] + 1]
    if kate_pos[0] < (len(maze_space) - 1) and maze_space[kate_pos[0] + 1][kate_pos[1]] == ' ':
        space_down = [kate_pos[0] + 1, kate_pos[1]]
    if kate_pos[1] != 0 and maze_space[kate_pos[0]][kate_pos[1] - 1] == ' ':
        space_left = [kate_pos[0], kate_pos[1] - 1]
    return [space_up, space_right, space_down,
            space_left]  # list of available spaces in each direction , busy spaces are empty,
    # Edge spaces are covered separatly


def move(kate_pos, spaces_, visited_, maze_, steps_):
    for i in range(len(spaces_)):  # all available spaces around kate, spaces_k is the output from def find_space
        if spaces_[i] not in visited_ and bool(spaces_[i]):  # if the space is not visited and is free
            kate_pos = spaces_[i]  # Kate moves there
            visited_.append(spaces_[i])
            steps_ += 1
            return kate_pos, visited_, steps_

        elif all(i in visited_ for i in list(filter(lambda x: bool(x), spaces_))):  # if all available spaces are already visited
            maze_[kate_pos[0]][kate_pos[1]] = '@'
            # Kate marks the space with @ BECAUSE this position doesn`t lead to any new spaces or exits
            kate_pos = visited_[-2]  # Kate moves one step back
            del visited_[-1]  # Kate removes the marked with @ space from the visited spaces as
            # it is clearly a dead end and from now on will be part of the Maze walls
            steps_ -= 1  # as Kate moves back, we decrease the steps
            return kate_pos, visited_, steps_


while kate_position[0] <= (rows - 1):
    if kate_position[1] == 0 or kate_position[1] == len(maze[0]) - 1 or kate_position[0] == 0 or kate_position[0] == rows - 1:
        steps_old = max(steps, steps_old)  # if Kate is on the Edge then we have a (possible) exit
        # but will explore other options

    spaces = find_space(kate_position, maze)  # check where Kate can go
    #  now check if there are spaces to go
    if not sum((lambda x: bool(x))(x) for x in spaces) and kate_position[0] < (rows - 1) and steps_old == -1:
        # if we didn't encounter a possible exit in the past (steps_old==-1)
        # and we have ways to go now, then there is no exit
        print("Kate cannot get out")
        get_out_flag = True
        break
    elif not sum((lambda x: bool(x))(x) for x in spaces) and steps_old != -1:
        steps = steps_old  # if we have no ways to go, and we have a possible exit, then that's the exit
        break
    # then if there are spaces to go, GO
    test_move = list(filter(lambda x: bool(x), spaces))
    kate_position, visited, steps = move(kate_position, spaces, visited, maze, steps)

if not get_out_flag:
    print(f"Kate got out in {max(steps, steps_old) + 1} moves")
