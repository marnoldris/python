
def csp_calc(Q, m, T) -> float:
    return Q/(m*T)
Q = float(input("Please enter Q: "))
m = float(input("Please enter m: "))
T = float(input("Please enter delta T: ")) 
#Q, m, T = float(input("Please enter Q, m, and T separated by a space: ").split(' '))
print(f"Csp = {csp_calc(Q, m, T)}")
