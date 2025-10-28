triangle_sides = [2, 4, 5]
def is_triangle(l):
    l = sorted(l)
    if ((l[0] + l[1]) > l[2]) and ((l[0] + l[2]) > l[1]) and ((l[1] + l[2]) > l[0]): 
        return True
    return False
    
print(is_triangle(triangle_sides))