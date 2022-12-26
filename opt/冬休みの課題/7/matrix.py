import numpy as np

def ex4():
    a = np.array([[1,2],[3,4]])
    b = np.array([[3,2],[0,-1]])
    ans = []

    ans.append(3 * b)
    ans.append((2*a) -b)
    ans.append(a + b)
    ans.append(np.identity(2))
    ans.append(np.zeros((2,2)))

    for i in range(0, 5):
        print("---(4-",i+1,")---", sep='')
        print(ans[i])

    return 0

def ex5():
    a = np.array([[1,2],[2,1]])
    b = np.array([[1,1], [2,-1]])
    e = np.identity(2)
    ans = []

    ans.append(a*b)
    ans.append(a*e)

    a = np.array([[1,2],[0,1],[1,0]])
    b = np.array([[0,0,1],[1,0,1],[1,0,0]])
    c = np.array([[1],[3],[0]])
    d = np.array([0,1,0])

    try:
        b * a
    except ValueError:
        ans.append("errer")
    ans.append(d*c)
    try:
        a * b
    except ValueError:
        ans.append("errer")

    ans.append(b*c)

    for i in range(0, 6):
        print("---(4-",i+1,")---", sep='')
        print(ans[i])

    return 0

def ex6():
    a = np.array([[2,3],[5,-2]])
    xy = np.array([[31],[30]])
    ans = []

    ans.append(a)
    ans.append(np.linalg.inv(a))
    ans.append(ans[0]*ans[1])

    for i in range(0, 3):
        print("---(4-",i+1,")---", sep='')
        print(ans[i])

    return 0
ex6()