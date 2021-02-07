ray_x=800
ray_y=1000

cmd.set("ray_opaque_background","off")
cmd.viewport(ray_x,ray_y)
cmd.load("cover_cis_render.pse")
cmd.set_color("gold", [1.000000000,0.819607843,0.137254902])
cmd.set_color("hafnium", [0.301960784,0.760784314,1.000000000])
cmd.set_color("lithium", [0.800000000,0.501960784,1.000000000])
cmd.set_color("meitnerium", [0.921568627,0.000000000,0.149019608]) 
cmd.set_color("phosphorus", [1.000000000,0.501960784,0.000000000]) 
cmd.set_color("protactinium",[0.000000000,0.631372549,1.000000000]) 
cmd.set_color("radium", [0.000000000,0.490196078,0.000000000])
cmd.set_color("tellurium", [0.831372549,0.478431373,0.000000000]) 

colors =['gold', 'hafnium', 'lithium', 'meitnerium', 'phosphorus', 'protactinium', 'radium', 'tellurium']


for col in colors:
    cmd.color(col, "obj01")
    cmd.ray(ray_x,ray_y)
    cmd.png(("cover_%s.png") %col)
    cmd.save(("cover_%s.pse") % col)
