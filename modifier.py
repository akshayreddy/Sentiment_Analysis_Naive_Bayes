import os


home = os.getcwd()
f = open("movie_reviews.txt","a")

path = os.path.join(home,'pos')
os.chdir(path)

for filename in os.listdir(path):
    input_text = open(filename,"r").read()
    f.write("1\t"+str(input_text).replace("<br />","")+"\n")


path = os.path.join(home,'neg')
os.chdir(path)

for filename in os.listdir(path):
    input_text = open(filename,"r").read()
    f.write("0\t"+str(input_text).replace("<br />","")+"\n")



f.close()
