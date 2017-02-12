size(600, 450)

# Import the library
try:
    # This is the statement you normally use.
    pixie = ximport("pixie")
except:
    # But since this example is "inside" the library
    # we may need to try something different when
    # the library is not located in /Application Support
    pixie = ximport("__init__")
    reload(pixie)

# Draw a big heading
pixie.heading("Hello, World", 40, 120, 200, 60)

# Set the amount of errors, and draw a paragraph
pixie.distraction(0.5)
pixie.text("This is Pixie", 40, 250, 1000, 32)

# Don't make errors anymore
pixie.distraction(0.0)

# Draw a tree
nodes = ( ("parent1", ("child1", "child2")), ("parent2", ("child2.1", "child2.2")) )
pixie.tree("root", nodes, WIDTH/2, 350, 400, 400)