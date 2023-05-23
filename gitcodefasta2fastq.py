import os
import sys
from os.path import exists

class fastq2fastaconverter:
    
    
    def __init__(self, inputfilepath):
        self.path= inputfilepath
        
    def openfile (self):   
        f = open( inputfilepath , "r")
        first_character=(f.read(1))
        if first_character == "@" :
            print ("Yes" + first_character )
        else :
            print("no" + first_character)
            sys.exit(1)
        return f
        
        
        
    #def openfile (self):
        #inputopenfile = open(self.path , "r")
        #return inputopenfile
        
        
    def convertfile (self, inputfastqfile, outputfilename):
        #if file exists then delete file otherwise proceed
        file_exists= exists(outputfilename)
        if file_exists == True:
            os.remove(outputfilename)
        lineindex=0 
        file_obj = open(outputfilename, "a")   
        for line in inputfastqfile:
            #chk line number by modulus
            #after every iteration add one in line index variable
            lineindex = lineindex + 1
            isfirstline=(lineindex%4==1)
            #check if this the first line
            #replace file extension .fastq by .fa
            if isfirstline ==True:
        
                fastaline = line.replace('@', '>')
                file_obj.write(fastaline)
            
            #check if this is the second line
            #after every iteration add one in line index variable
            issecondline=(lineindex%4==2)
            if  issecondline ==True:
                file_obj.write(line)
        file_obj.close()
            
            
            
print('Enter file path')
inputfilepath = input()
outputfilename = inputfilepath.replace('.fastq','.fa')
print('File path is' + inputfilepath)       
    
        
Fqf= fastq2fastaconverter (inputfilepath)
fastqfile= Fqf.openfile()  
It=Fqf.convertfile (fastqfile, outputfilename)