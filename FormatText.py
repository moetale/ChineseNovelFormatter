import os
import argparse
import argparse

parser = argparse.ArgumentParser(description='Format text.')
parser.add_argument("--input_home_path",type=str,help="Input home path for scanning.",default="data/input")
parser.add_argument("--output_home_path",type=str,help="Output home path for yielding formatted text.",default="data/output")
args=parser.parse_args()
input_home_path=vars(args)["input_home_path"]
output_home_path=vars(args)["output_home_path"]
print("received input home path:"+input_home_path)
print("received output home path:"+output_home_path)

input_encoding="gbk"
output_encoding="utf-8"
names=os.listdir(input_home_path)
for name in names:
    print("detected:"+name)
    if(name[-4:]!=".txt"):
        print("skip irrelevant:"+name)
        continue
    input_path=input_home_path+"/"+name
    f_input=open(input_path,"r",-1,input_encoding,errors="ignore")
    content=f_input.read()
    f_input.close()
    output_path=output_home_path+"/"+name
    f_output=open(output_path,"w",-1,output_encoding)
    f_output.write(content)
    f_output.flush()
    print("finished formatting:"+name)
print("Done")