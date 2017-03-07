from display import *
from matrix import *
from draw import *


def parse_file( fname, points, transform, screen, color ):
    cmd = open(fname,"r")
    script = cmd.read().split("\n")
    cmd.close()
    print script
    
    save_ppm(screen, fname)


