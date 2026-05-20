NaOH = compound([sphere(pos=vector(-65,60,3),radius=8),sphere(pos=vector(-65,60,3),radius=8,color=color.red)])
KOH = compound([sphere(pos=vector(-45,60,3),radius=8),sphere(pos=vector(-45,60,3),radius=8)])

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
        elif checkbox.text == 'Ca(OH)':
            Ca(OH).visible = True
        elif checkbox.text == 'HCL':
            HCL.visible = True
        elif checkbox.text == 'HNO3':
            HNO3.visible = True
        elif checkbox.text == 'H2SO4':
            H2SO4.visible = True
        elif checkbox.text == 'H2CO3':
            H2CO3visible = True
    
    else:
        if checkbox.text == 'NaOH':
            NaOH.visible = False
        elif checkbox.text == 'KOH':
            KOH.visible = False
        elif checkbox.text == 'NA4OH':
            NA4OH.visible = False
        elif checkbox.text == 'Ca(OH)':
            Ca(OH).visible = False
        elif checkbox.text == 'HCL':
            HCL.visible = False
        elif checkbox.text == 'HNO3':
            HNO3.visible = False
        elif checkbox.text == 'H2SO4':
            H2SO4.visible = False
        elif checkbox.text == 'H2CO3':
            H2CO3.visible = False
           
checkbox1 = checkbox(pos=scene.title_anchor, text='NaOH', checked=True, bind=checkbox_event)
checkbox2 = checkbox(pos=scene.title_anchor, text='KOH', checked=True, bind=checkbox_event)
checkbox3 = checkbox(pos=scene.title_anchor, text='NA4OH', checked=True, bind=checkbox_event)
checkbox4 = checkbox(pos=scene.title_anchor, text='Ca(OH)', checked=True, bind=checkbox_event)
checkbox5 = checkbox(pos=scene.title_anchor, text='HCL', checked=True, bind=checkbox_event)
checkbox6 = checkbox(pos=scene.title_anchor, text='HNO3', checked=True, bind=checkbox_event)
checkbox7 = checkbox(pos=scene.title_anchor, text='H2SO4', checked=True, bind=checkbox_event)
checkbox8 = checkbox(pos=scene.title_anchor, text='H2CO3', checked=True, bind=checkbox_event)
