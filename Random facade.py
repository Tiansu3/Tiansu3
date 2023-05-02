import rhinoscriptsyntax as rs
import random
x=rs.GetInteger("x number",8)
y=rs.GetInteger("y number",8)
d=rs.GetReal("length",5)
smin=rs.GetReal("minimun scale factor",0.2)
smax=rs.GetReal("maximum scale factor",0.6)

for i in range(x):
    for j in range(y):
        rs.EnableRedraw(False)
        rec1=rs.AddPolyline([(d*i,0,d*j),(d*i,0,d*(j+1)),(d*(i+1),0,d*(j+1)),(d*(i+1),0,d*j),(d*i,0,d*j)])
        
        center=rs.CurveAreaCentroid(rec1)[0]
        rec2=rs.ScaleObject(rec1,center,(random.uniform(smin,smax),0,random.uniform(smin,smax)),True)
        
        rs.MoveObject(rec2,(random.uniform(-0.2*d,0.2*d),random.uniform(0.2*d,1*d),random.uniform(-0.2*d,0.2*d)))
        rs.AddLoftSrf([rec1,rec2])
        rs.DeleteObjects([rec1,rec2])