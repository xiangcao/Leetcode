"""
Given a robot cleaner in a room modeled as a grid.

Each cell in the grid can be empty or blocked.

The robot cleaner with 4 given APIs can move forward, turn left or turn right. Each turn it made is 90 degrees.

When it tries to move into a blocked cell, its bumper sensor detects the obstacle and it stays on the current cell.

Design an algorithm to clean the entire room using only the 4 given APIs shown below.

Notes:

The input is only given to initialize the room and the robot's position internally. You must solve this problem "blindfolded". In other words, you must control the robot using only the mentioned 4 APIs, without knowing the room layout and the initial robot's position.
The robot's initial position will always be in an accessible cell.
The initial direction of the robot will be facing up.
All accessible cells are connected, which means the all cells marked as 1 will be accessible by the robot.
Assume all four edges of the grid are all surrounded by wall.
"""

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """
"""
ask yourself these questions:
What do do if after the right turn there is an obstacle just in front ?
Turn right again.


How to explore the alternative paths from the cell ?
Go back to that cell and then turn right from your last explored direction.


When to stop ?
Stop when you explored all possible paths, i.e. all 4 directions (up, right, down, and left) for each visited cell.
"""
class Solution(object):
    # To track the cells the robot has cleaned, start a index pair (i, j) from (0, 0). When go up, i-1; go down, i+1; go left, j-1; go right: j+1. 
    # Also use DIR to record the current direction of the robot
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        self.dfs(robot, 0, 0, -1, 0, set())

    # always turn left
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        # the robot can to four directions, we use left turn to switch to next direction
        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                # move according to current direction directly. Find the (x, y) for the next cell based on current direction
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                # go back to the starting position
                robot.turnLeft()
                robot.turnLeft()
                robot.move()
                robot.turnLeft()
                robot.turnLeft()
            # turn to next direction
            robot.turnLeft()
            direction_x, direction_y = -direction_y, direction_x 

    # always turn right
    def dfs(self, robot, x, y, direction_x, direction_y, visited):
        robot.clean()
        visited.add((x, y))

        # the robot can to four directions, we use left turn to switch to next direction
        for k in range(4):
            neighbor_x = x + direction_x
            neighbor_y = y + direction_y
            if (neighbor_x, neighbor_y) not in visited and robot.move():
                # move according to current direction directly. Find the (x, y) for the next cell based on current direction
                self.dfs(robot, neighbor_x, neighbor_y, direction_x, direction_y, visited)
                # go back to the starting position
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
            # turn to next direction
            robot.turnRight()
            direction_x, direction_y = direction_y, -direction_x
