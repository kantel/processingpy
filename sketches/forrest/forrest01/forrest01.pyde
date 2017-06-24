import csv
import random as r

def setup():
    size(800, 640)
    tree1 = loadImage("laub.png")
    tree2 = loadImage("nadel.png")
    tree3 = loadImage("plant.png")
    fire  = loadImage("fire.png")
    fileHandle = open("forrest.tsv")
    trees = csv.DictReader(fileHandle, delimiter = "\t")
    background(220)
    for row in trees:
        tree = int(row["type"])
        x = int(row["x"])
        y = int(row["y"])
        if tree == 1:
            image(tree1, x, y)
        elif tree == 2:
            image(tree2, x, y)
        elif tree == 3:
            image(tree3, x, y)
        elif (tree == 4) and (r.randint(0, 99) == 0):
            image(fire, x, y)