
def alpha(y,a,dt):
	p_y = y
	t = 0
	
	while(y>0):
		t += dt;
		t_flag = y
		y = y*2 - p_y + a*dt*dt
	print t

def sv(y,a,dt):
	p_y = y
	v = 0
	t = 0
	while(y>0):
		t += dt
		t_y = y
		y = y*2 - p_y + a*dt*dt
		v += a*dt

	print t

def vv(y,a,dt):
	v = 0
	t = 0
	while(y>0):
		t += dt
		y += v*dt + 0.5*a*dt*dt
		v = a*dt
	print t


	
