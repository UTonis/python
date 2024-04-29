import turtle
t = turtle.Turtle()
t.shape("turtle")

while(True):
    n = int(input("몇각형을 그리시겠어요?(3-6): "))
    if(n==0) : break
    t.clear()
    for i in range(n) : 
        t.forward(100)
        t.left(360//n)
#turtle.done()