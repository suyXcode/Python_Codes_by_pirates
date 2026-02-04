var = open("suy.txt",'w') # read is default mode
d1 = "hello world\n"
d2 = "welcome to python programming\n"
d3 = "file handling in python\n"
var.write(d1)
var.writelines([d2,d3])
# var.flush()  # Ensure data is written to the file
var.close()