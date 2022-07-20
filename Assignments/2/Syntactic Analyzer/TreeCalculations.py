from nltk import ChartParser
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree
from nltk.data import load
from PIL import Image,EpsImagePlugin

class TreeCalculations():

    def calculateTree(self,grammar,input_sentence):
        parser = ChartParser(grammar)
        for tree in parser.parse(input_sentence):
            return(tree)


    # Print the syntactic tree in the console 
    # Same as printig in Prolog with functor in the example given
    def printTree(self,tree):
            print("Syntactic Tree is:\n",tree ,"\n")

    def createTreeImage(self,tree):
        # Save created Tree 
        cf = CanvasFrame()
        syntactic_tree = Tree.fromstring(str(tree))
        tc = TreeWidget(cf.canvas(), syntactic_tree)

        # Add some colors and bigger font sizes
        tc['node_font'] = "calibri 16 bold"
        tc['leaf_font'] = "arial 16"
        tc['node_color'] = "#005990"
        tc['leaf_color'] = "#3F8F57"
        tc['line_color'] = "#175252"

        cf.add_widget(tc , 10, 10) # (10,10) offsets
        cf.print_to_file("tree.ps")
        print("Creating syntactic tree image file..\n")
        cf.destroy()

        # Convert .ps file to .png in order to open it
        print("Converting file to PNG so we can view it..\n")
        # placing the path for Ghostscript (you need to install it from https://ghostscript.com/releases/gsdnld.html)
        EpsImagePlugin.gs_windows_binary =  r'C:\Program Files\gs\gs9.56.1\bin\gswin64c'
        ps_file = Image.open("tree.ps")
        ps_file.save('tree.png')
        print("Done! Locate the file as 'tree.png' in the working directory.\n")