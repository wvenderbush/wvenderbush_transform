from display import *
from matrix import *
from draw import *
from time import sleep

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
	 Every command is a single character that takes up a line
	 Any command that requires arguments must have those arguments in the second line.
	 The commands are as follows:
		 line: add a line to the edge matrix - 
		takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
		then multiply the transform matrix by the scale matrix - 
		takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
		then multiply the transform matrix by the translation matrix - 
		takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
		then multiply the transform matrix by the rotation matrix -
		takes 2 arguments (axis, theta) axis should be x, y or z
	 yrotate: create an y-axis rotation matrix,
		then multiply the transform matrix by the rotation matrix -
		takes 1 argument (theta)
	 zrotate: create an z-axis rotation matrix,
		then multiply the transform matrix by the rotation matrix -
		takes 1 argument (theta)
	 apply: apply the current transformation matrix to the 
		edge matrix
	 display: draw the lines of the edge matrix to the screen
		display the screen
	 save: draw the lines of the edge matrix to the screen
		save the screen to a file -
		takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
	with open(fname) as f:
		content = f.readlines()
		content = [x.strip() for x in content]
		
	count = 0;
	plen = len(content)

	while (count < plen):
		cmd = content[count]
		arg = content[count + 1]

		if (cmd == "line"):
			print("Adding line...\n")
			args = arg.split(" ")
			add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
			count += 2

		if (cmd == "ident"):
			print("Reverting to identity...\n")
			ident(transform)
			count += 1

		if (cmd == "scale"):
			print("Scaling matrix...\n")
			args = arg.split(" ")
			newmat = make_scale(int(args[0]), int(args[1]), int(args[2]))
			matrix_mult(newmat, transform)
			count += 2

		if (cmd == "move"):
			print("Moving matrix...\n")
			args = arg.split(" ")
			newmat = make_translate(int(args[0]), int(args[1]), int(args[2]))
			matrix_mult(newmat, transform)
			count += 2

		if (cmd == "rotate"):
			args = arg.split(" ")
			if (args[0] == "x"):
				print("Rotating by x...\n")
				newmat = make_rotX(int(args[1]))
			if (args[0] == "y"):
				print("Rotating by y...\n")
				newmat = make_rotY(int(args[1]))
			if (args[0] == "z"):
				print("Rotating by z...\n")
				newmat = make_rotZ(int(args[1]))
			
			matrix_mult(newmat, transform)
			count += 2

		if (cmd == "apply"):
			print("Applying transformation...\n")
			matrix_mult(transform, points)
			count += 1

		if (cmd == "display"):
			print("Starting display...\n")
			draw_lines(points, screen, color)
			display(screen)
			sleep(.25)
			clear_screen(screen)
			count += 1

		if (cmd == "save"):
			print("Saving file...\n")
			save_extension(screen, arg)
			#clear_screen(screen)
			count += 2

		print_matrix(points)
