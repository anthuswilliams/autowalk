import ode

world = ode.World()
world.setGravity( (0,-9.81,0) )

body = ode.Body(world)
mass = ode.Mass()
mass.setSphere(2500.0, 0.05)
mass.mass = 1.0
body.setMass(mass)

body.setPosition( (0,2,0) )
body.addForce( (0,200,0) )

t = 0.0
dt = 0.04
while t < 2.0:
    x,y,z = body.getPosition()
    u,v,w = body.getLinearVel()
    
    print "%1.2fsec: pos=(%6.3f, %6.3f, %6.3f) vel=(%6.3f, %6.3f, %6.3f)" % (t, x, y, z, u, v, w)
    world.step(dt)
    t += dt
