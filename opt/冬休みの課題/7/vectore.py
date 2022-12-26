import numpy as np

def ex1():
    O = np.array([0,0,0])
    P = np.array([1,4,-3])
    Q = np.array([-1,3,2])

    OP = np.linalg.norm(P - O)
    PQ = np.linalg.norm(Q-P)

    print("---(1-1)---")
    print(OP)
    print("---(1-2)---")
    print(PQ)

    return 0

def ex2():
    a = np.array([1,2,3])
    b = np.array([2,3,1])
    c = np.array([3,1,2])
    ans = []

    ans.append(np.linalg.norm(c))
    ans.append(a + b)
    ans.append(a + b + c)
    ans.append(a + (2*b) - (3*c))
    ans.append( c + (b - a))

    for i in range(0, 5):
        print("---(2-",i,")---", sep='')
        print(ans[i])
    
    return 0

def ex3():
    a = np.array([1,1,0])
    b = np.array([2,0,2])
    ans = []

    ans.append(format(np.linalg.norm(a), '.1f'))
    ans.append(format(np.linalg.norm(b), '.1f'))
    ans.append(np.dot(a,b))
    ans.append( np.rad2deg ( np.dot(a,b)/ float(ans[0])*float(ans[1]) ) )
    ans.append( a*b / (np.linalg.norm(a*b)))

    for i in range(0, 5):
        print("---(3-",i+1,")---", sep='')
        print(ans[i])

    return 0


ex3()