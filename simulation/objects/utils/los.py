import numpy as np

def check_los(u,d,blockers):
    l_du = d-u
    for b in blockers:
        l_bu = b.position-u
        a = l_du[:2]
        b = l_bu[:2] 
        if bool(np.cross(a,b)):
            if l_du[2] <= (np.sqrt(a[0]**2 + a[1]**2)/np.sqrt(b[0]**2 + b[1]**2))*l_bu[2] :
                return False         
    return True