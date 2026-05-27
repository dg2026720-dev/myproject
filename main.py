Na=sphere(pos=vector(-65,60,3),radius=8)
OH=sphere(pos=vector(-65,60,3),radius=8,color=color.red)
NaOH = compound([Na,OH])
K=sphere(pos=vector(-38,60,3),radius=8)
OH=sphere(pos=vector(-38,60,3),radius=8)
KOH = compound([K,OH])
NA4=sphere(pos=vector(-10,60,3),radius=8)
OH=sphere(pos=vector(-10,60,3),radius=8,color=color.red)
NA4OH= compound([NA4,OH])
H=sphere(pos=vector(15,60,3),radius=8)
Cl=sphere(pos=vector(15,60,3),radius=8,color=color.cyan)
HCl=compound([H,Cl])
H=sphere(pos=vector(40,60,3),radius=8)
NO3=sphere(pos=vector(40,60,3),radius=8,color=color.orange)
HNO3=compound([H,NO3])
H=sphere(pos=vector(60,60,3),radius=8)
H2=sphere(pos=vector(60,60,3),radius=8)
CO3=sphere(pos=vector(60,60,3),radius=8,color=color.yellow)
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
        elif checkbox.text == 'HCl':
            HCl.visible = True
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
        elif checkbox.text == 'HCl':
            HCl.visible = False
        elif checkbox.text == 'HNO3':
            HNO3.visible = False
        elif checkbox.text == 'H2CO3':
            H2CO3.visible = False
           
checkbox1 = checkbox(pos=scene.title_anchor, text='NaOH', checked=True, bind=checkbox_event)
checkbox2 = checkbox(pos=scene.title_anchor, text='KOH', checked=True, bind=checkbox_event)
checkbox3 = checkbox(pos=scene.title_anchor, text='NA4OH', checked=True, bind=checkbox_event)
checkbox4 = checkbox(pos=scene.title_anchor, text='HCl', checked=True, bind=checkbox_event)
checkbox5 = checkbox(pos=scene.title_anchor, text='HNO3', checked=True, bind=checkbox_event)
checkbox6 = checkbox(pos=scene.title_anchor, text='H2CO3', checked=True, bind=checkbox_event)

import random

while True:
    rate(50)
    
    k = keysdown()

    if 'a' in k:
        NaOH.pos.x = random.uniform(-60, 60)
        NaOH.pos.y = random.uniform(-40, 50)
        
    if 's' in k:
        HCl.pos.x = random.uniform(-60, 60)
        HCl.pos.y = random.uniform(-40, 50)

    d = mag(NaOH.pos - HCl.pos)

    if d < 15:
        print("드디어 물분자생성!") 

        NaOH.visible = False
        HCl.visible = False

        mid_pos = (NaOH.pos + HCl.pos) / 2
        water = sphere(pos=mid_pos, radius=12, color=color.blue)

        break
