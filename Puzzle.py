# Name: Megan Grant
# OSU Email: granmega@oregonstate.edu
# Course: CS325 - Analysis of Algorithms
# Assignment: 8
# Start Date: 5/15/23
# Description: Finds a path through a puzzle that requires the minimum effort
# heavily inspired by the Dijkstra algorithm at this URL:
# https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/

import heapq

def solve_puzzle(Board, Source, Destination):
    """A function that returns the minimum effort path of a puzzle
    ::param Board:: represents the given puzzle
    ::param Source:: represents the starting place
    ::param Destination:: represents the ending place
    ::param row, col:: represents the rows and columns of the board
    ::param been_there:: tracks where we've gone for the solution
    ::param priority:: represents a priority queue
    ::param directions:: represents the directions of each move as a string
    ::param effort, current_row, current_col:: represents the effort, current row and column of the puzzle
    ::param shifts:: represents the possible directions of the path in the puzzle
    ::param path:: represents the path through the puzzle with minimum effort
    ::param update_row, update_col:: represents the movement of the rows and columns location"""

    # getting breadth and depth dimensions
    row, col = len(Board), len(Board[0])
    # establishing a way to store locations
    been_there = {}
    # creating a priority queue: effort, row, column
    priority = [(0, Source[0], Source[1])]
    # establishing a string to store the movements
    directions = ""
    while len(priority) > 0:
        effort, current_row, current_col = heapq.heappop(priority)
        # setting up checks through the rows/cols
        shifts = [[1,0], [-1, 0], [0, 1], [0, -1]]
        if (current_row, current_col) == Destination:  # at the end
            path, directions = get_path(Source, current_row, current_col, been_there, directions)
            path.reverse()
            string = string_reversal(directions)
            return path, string
        for move_row, move_col in shifts:
            update_row = current_row + move_row
            update_col = current_col + move_col
            # not blocked or out of bounds
            if 0 <= update_row < row and 0 <= update_col < col and Board[update_row][update_col] == '-' \
                    and (update_row, update_col) not in been_there:
                heapq.heappush(priority, (effort + 1, update_row, update_col))
                been_there[(update_row, update_col)] = current_row, current_col
    return None


def get_path(source, curr_row, curr_col, locations, directions):
    """A method that returns the optimal path of the puzzle
    ::param way_forward:: tracks the current location moving back through the path
    ::param previous_row, previous_col:: tracks the coordinates prior to the move
    ::param answer:: packages the path and the string to send back to main function"""
    way_forward = [(curr_row, curr_col)]
    # while we are not back at the beginning
    while way_forward[-1] != source:
        previous_row, previous_col = locations[way_forward[-1]]
        # add the current move to the directions string
        directions += check_route(previous_row, previous_col, way_forward)
        # add the next coordinates
        way_forward.append(locations[way_forward[-1]])
    answer = (way_forward, directions)
    return answer


def check_route(prev_row, prev_col, way_forward):
    """A method that returns each movement direction in the puzzle path"""
    if prev_row > way_forward[-1][0]:
        return "U"
    if prev_row < way_forward[-1][0]:
        return "D"
    if prev_col > way_forward[-1][1]:
        return "L"
    if prev_col < way_forward[-1][1]:
        return "R"


def string_reversal(directions):
    """A method that reverses the movement string so it's accurate"""
    string = directions[::-1]
    return string

