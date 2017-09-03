from functions import * 
from plotter import *

if __name__ == "__main__":
	alpha(5,-10,0.01)
	sv(5,-10,0.01)
	vv(5,-10,0.01)

	fig = plt.figure()
	ax1 = fig.gca(projection='3d')

	z = t 
	ax1.plot( ry(z), z)

	plt.ylim(-6,6)


	plt.show()




