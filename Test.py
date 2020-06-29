#!/usr/bin/env python3

from shutil import copyfile, move
import os
import glob


def main():
    BasePath = './'
    Files = glob.glob(BasePath + '*.html')
    CopyFileName = 'CopyFromFooter.html'
    Keyword = 'EDIT FOOT'

    for FileName in Files:
        print(FileName)
        if('Edit' in FileName or FileName == CopyFileName):
            continue
        else:
            # FileName = 'index.html'
            if(not (os.path.isdir(BasePath +'Bak/'))):
               os.makedirs(BasePath + 'Bak/')

            copyfile(BasePath + FileName, BasePath + 'Bak/'+FileName+'.bak')
            with open(BasePath + FileName, 'r') as f1, open(BasePath +'Edit'+FileName.split(BasePath)[-1], 'w') as f2:
                WriteFlag = True
                for Line in f1.readlines():
                    if(Keyword in Line):
                        f2.write(Line)  
                        Tabs = Line.split('<!-- ' + Keyword + ' -->')[0]
                        if(WriteFlag):
                            with open(BasePath + CopyFileName, 'r') as f3:
                                for CopyLine in f3.readlines():
                                    f2.write(Tabs + '\t' + CopyLine)
                        WriteFlag = not WriteFlag

                    if(WriteFlag and not (Keyword in Line)):
                        f2.write(Line)  
            # Replace original file
            move(BasePath +'Edit'+FileName.split(BasePath)[-1], BasePath + FileName)





if __name__=='__main__':
    main()