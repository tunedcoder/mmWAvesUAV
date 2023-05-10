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

def check_pl(u,d,blockers):
    if check_los(u, d, blockers):
        return -(61.4 + 2*np.log10(np.sqrt((d[0]-u[0])**2 + (d[1]-u[1])**2 + (d[2]-u[2])**2)))
    else:
        return -(72 + 2.92*np.log10(np.sqrt((d[0]-u[0])**2 + (d[1]-u[1])**2 + (d[2]-u[2])**2)))