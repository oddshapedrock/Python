from PIL import Image, ImageDraw
import sys, os
sys.path.insert(0, f"{os.path.dirname(__file__)}..\\..\\maze_files")

import importlib

def createMaze(userID, new):
    maze = importlib.import_module(userID)
    if new:
        importlib.reload(maze)
    gridmap = maze.getData()
    values = maze.getValues()

    height = 672
    width = 672
    image = Image.new(mode="RGB", size=(height, width), color=(255, 255, 255))

    draw = ImageDraw.Draw(image)

    x_start = 5
    y_start = 5
    for row in gridmap:
        for cell in row:
            
            if cell["location"] == values["exit_loc"]:
                draw.rectangle([(x_start, y_start), (x_start+60, y_start+60)], fill=("#EEEE9B"))
                
            if cell["location"] == values["player_pos"]:
                draw.ellipse([(x_start + 10, y_start + 10), (x_start+50, y_start+50)], fill=("#0000FF"))
        
            if cell["walls"][0] == True:
                line = ((x_start, y_start + 60), (x_start + 60, y_start + 60))
                draw.line(line, width=10, fill = (0, 0, 0))
            if cell["walls"][1] == True:
                line = ((x_start, y_start), (x_start + 60, y_start))
                draw.line(line, width=10, fill = (0, 0, 0))
            if cell["walls"][2] == True:
                line = ((x_start, y_start), (x_start, y_start + 60))
                draw.line(line, width=10, fill = (0, 0, 0))
            if cell["walls"][3] == True:
                line = ((x_start + 60, y_start), (x_start + 60, y_start + 60))
                draw.line(line, width=10, fill = (0, 0, 0))
            y_start += 60
        y_start = 5
        x_start += 60

    del draw
    image.save("os.path.dirname(__file__)..\\..\\maze_images\\i" + userID + ".png")
