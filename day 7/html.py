
colors = {0: (255,255,255),1:(192,192,192),2:(128,128,128),3:(0,0,0),4:(255,0,0),5:(128,0,0),6:(255,255,0),7:(128,128,0),8:(0,255,0),9:(0,128,0),10:(0,255,255),11:(0,128,128),12:(0,0,255),13:(0,0,128),14:(255,0,255),15:(128,0,128)}
maping = ["White","Silver","Gray","Black","Red","Maroon","Yellow","Olive","Lime","Green","Aqua","Teal","Blue","Navy","Fuchsia","Purple"]

def distance(A,B):
    # A: named color:
    # B: new color;

    return ((A[0]-B[0])**2 + (A[1]-B[1])**2 + (A[2]-B[2])**2 )**0.5

line = input()

while line != "-1 -1 -1":
    a,b,c = map(int, line.split(" "))

    B = (a,b,c)
    min = float("inf")
    ans =""

    for i in range(16):
        x = distance(colors[i],B)
        if x < min:
            min = x
            ans = maping[i]

    print(ans)
    line = input()
