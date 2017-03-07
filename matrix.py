import math
import random

def make_translate( x, y, z ):
    m = new_matrix()
    for r in range(len(m[0])):
        for c in range(len(m)):
            if c == r:
                m[c][r]=1
    m[3][0]=x
    m[3][1]=y
    m[3][2]=z
    return m              
                

def make_scale( x, y, z ):
    diagonal = [x, y, z, 1]
    m = new_matrix()
    for i in range(len(m)):
        m[i][i] = diagonal[i]
    return m

def make_rotX( theta ):    
    angle = math.radians(theta)
    m = new_matrix()
    m[0][0] = 1
    m[1][0] = math.cos(angle)
    m[1][2] = (-1)*(math.sin(angle))
    m[2][2] = math.cos(angle)
    m[2][1] = math.sin(angle)
    m[3][3] = 1
    return m

def make_rotY( theta ):
    angle = math.radians(theta)
    m = new_matrix()
    m[0][0] = math.cos(angle)
    m[0][2] = math.sin(angle)
    m[2][0] = math.cos(angle)
    m[2][2] = (-1)*(math.cos(angle))
    m[3][3] = 1
    return m

def make_rotZ( theta ):
    angle = math.radians(theta)
    m = new_matrix()
    m[0][0] = math.cos(angle)
    m[0][1] = (-1)*(math.sin(angle))
    m[1][0] = math.sin(angle)
    m[1][1] = math.cos(angle)
    m[2][2] = 1
    m[3][3] = 1
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + '\t'
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):

    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1
    return m2

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

#testing
'''
m1 = new_matrix(4,4)
for r in range(len(m1[0])):
    for c in range(len(m1)):
        m1[c][r]= random.randint(0,9)
        if (r == 3):
            m1[c][r]=1
print_matrix(m1)
t1 = make_translate(1,4,2)
print_matrix(t1)
print_matrix(matrix_mult(t1,m1))
'''
