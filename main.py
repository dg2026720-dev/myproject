Na=sphere(pos=vector(-65,68,3),radius=8)
OH=sphere(pos=vector(-65,60,3),radius=8,color=color.red)
NaOH = compound([Na,OH])
K=sphere(pos=vector(-38,60,3),radius=8)
OH=sphere(pos=vector(-38,60,3),radius=8)
KOH = compound([K,OH])
NA4=sphere(pos=vector(-10,60,3),radius=8)
OH=sphere(pos=vector(-10,60,3),radius=8,color=color.red)
NA4OH= compound([NA4,OH])
H=sphere(pos=vector(15,60,3),radius=8)
CL=sphere(pos=vector(15,60,3),radius=8,color=color.cyan)
HCL=compound([H,CL])
H=sphere(pos=vector(40,60,3),radius=8)
NO3=sphere(pos=vector(40,60,3),radius=8,color=color.orange)
HNO3=compound([H,NO3])
H=sphere(pos=vector(60,60,3),radius=8)
H2=sphere(pos=vector(60,60,3),radius=8)
CO3=sphere(pos=vector(60,60,3),radius=8,color=color.blue)
H2CO3=compound([H,H2,CO3])


box(size = vec(1,130,40) , pos = vec(80,10,0))
box(size = vec(1,130,40) , pos = vec(-80,10,0))
box(size = vec(160,130,1) , pos= vec(0,10,-20))
box(size = vec(160,1,40), pos = vec(0,-55,0))
box(size = vec(160,130,1) , pos= vec(0,10,20),opacity = 0)

def checkbox_event(checkbox):
    if checkbox.checked:
        if checkbox.text == 'NaOH':
            NaOH.visible = True
        elif checkbox.text == 'KOH':
            KOH.visible = True
        elif checkbox.text == 'NA4OH':
            NA4OH.visible = True
        elif checkbox.text == 'HCL':
            HCL.visible = True
        elif checkbox.text == 'HNO3':
            HNO3.visible = True
        elif checkbox.text == 'H2CO3':
            H2CO3.visible = True
    
    else:
        if checkbox.text == 'NaOH':
            NaOH.visible = False
        elif checkbox.text == 'KOH':
            KOH.visible = False
        elif checkbox.text == 'NA4OH':
            NA4OH.visible = False
        elif checkbox.text == 'HCL':
            HCL.visible = False
        elif checkbox.text == 'HNO3':
            HNO3.visible = False
        elif checkbox.text == 'H2CO3':
            H2CO3.visible = False
           
checkbox1 = checkbox(pos=scene.title_anchor, text='NaOH', checked=True, bind=checkbox_event)
checkbox2 = checkbox(pos=scene.title_anchor, text='KOH', checked=True, bind=checkbox_event)
checkbox3 = checkbox(pos=scene.title_anchor, text='NA4OH', checked=True, bind=checkbox_event)
checkbox4 = checkbox(pos=scene.title_anchor, text='HCL', checked=True, bind=checkbox_event)
checkbox5 = checkbox(pos=scene.title_anchor, text='HNO3', checked=True, bind=checkbox_event)
checkbox6 = checkbox(pos=scene.title_anchor, text='H2CO3', checked=True, bind=checkbox_event)

import random

while True :
    rate(100)
    k = keysdown()
    if ' ' in k :
        NaOH.pos.x = random.uniform(-50,50)
        NaOH.pos.y=random.uniform(-50,50)
