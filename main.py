from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

def parse_file( fname, edges, transform, screen, color ):
    cmd = open(fname,"r")
    script = cmd.read().split("\n")
    cmd.close()
    #print script

    m = new_matrix()

    for i in range(len(script)):
        if script[i]=="display":
            clear_screen(screen)
            draw_lines(edges, screen, color)
            save_ppm( screen, "pic.ppm")
        if script[i]=="apply":
            matrix_mult(transform, edges)
        if script[i]=="line":
            points=(script[i+1]).split()
            #print points
            add_edge(edges, float(points[0]), float(points[1]),float(points[2]),float(points[3]),float(points[4]),float(points[5]))
        if script[i]=="ident":
            ident(m)
            transform = m
        if script[i]=="scale":
            scalar = (script[i+1]).split()
            scal = make_scale(float(scalar[0]),float(scalar[1]),float(scalar[2]))
            #print_matrix(scal)
            transform = matrix_mult(transform, scal)
            print_matrix(transform)
        if script[i]=="move":
            trans = (script[i+1]).split()
            move = make_translate(float(trans[0]),float(trans[1]), float(trans[2]))
            transform = matrix_mult(transform, move)
            print_matrix(transform)
        if script[i]=="rotate":
            rot = (script[i+1]).split()
            if rot[0] == 'x':
                transform = matrix_mult(transform,make_rotX(float(rot[1])))
            if rot[0] == 'y':
                transform = matrix_mult(transform,make_rotY(float(rot[1])))
            if rot[0] == 'z':
                transform = matrix_mult(transform,make_rotZ(float(rot[1])))
            print_matrix(transform)
        if script[i]=="save":
            draw_lines(edges, screen, color)
            save_ppm(screen, script[i+1])
        if script[i]=="quit":
            break

parse_file( 'script', edges, transform, screen, color )


