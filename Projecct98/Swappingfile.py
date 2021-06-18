f=open("C:\PythonProjects\Projects\Projecct98\sample1.txt","r")
a=f.read()

p=open("C:\PythonProjects\Projects\Projecct98\sample2.txt","r")
b=p.read()
p=open("C:\PythonProjects\Projects\Projecct98\sample2.txt","w")
p.write(a)
f=open("C:\PythonProjects\Projects\Projecct98\sample1.txt","w")
f.write(b)

