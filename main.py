from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single word that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix -
	 scale: create a scale matrix,
	    then multiply the transform matrix by the scale matrix -
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix,
	    then multiply the transform matrix by the translation matrix -
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing
See the file script for an example of the file format
"""

def parse_file( fname, edges, transform, screen, color ):
    cmd = open(fname,"r")
    script = cmd.read().split("\n")
    cmd.close()
    #print script

    m = new_matrix()

    for i in range(len(script)):
        if script[i]=="display":
            draw_lines(edges, screen, color)
            display(screen)
        if script[i]=="apply":
            edges = matrix_mult(transform, edges) 
        if script[i]=="line":
            points=(script[i+1]).split()
            #print points
            add_edge(edges, int(points[0]), int(points[1]),int(points[2]),int(points[3]),int(points[4]),int(points[5]))
        if script[i]=="ident":
            ident(m)
            transform = m
            print_matrix(transform)
        if script[i]=="scale":
            scalar = (script[i+1]).split()
            scal = make_scale(int(scalar[0]),int(scalar[1]),int(scalar[2]))
            #print_matrix(scal)
            #print_matrix(transform)
            transform = matrix_mult(scal,transform)
        if script[i]=="move":
            trans = (script[i+1]).split()
            move = make_scale(int(trans[0]),int(trans[1]), int(trans[2]))
            transform = matrix_mult(move,transform)
        if script[i]=="rotate":
            rot = (script[i+1]).split()
            if rot[0] == 'x':
                transform = matrix_mult(make_rotX(int(rot[1])),transform)
            if rot[0] == 'y':
                transform = matrix_mult(make_rotY(int(rot[1])),transform)
            if rot[0] == 'z':
                transform = matrix_mult(make_rotZ(int(rot[1])),transform)
        if script[i]=="save":
            draw_lines(edges, screen, color)
            save_extention(screen, script[i+1])
        if script[i]=="quit":
            break

parse_file( 'script', edges, transform, screen, color )
