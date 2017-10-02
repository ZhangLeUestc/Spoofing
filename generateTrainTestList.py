#!/usr/bin/env python
import os,sys,random,glob
Clientpath = '/home/m2a01/Data/NormalizedFace/ClientNormalized/'
Imposterpath = '/home/m2a01/Data/NormalizedFace/ImposterNormalized/'

    

def generate_list(Clientpath, Imposterpath):
    
    with open('trainlist.txt','w') as f1:
      with open('client_train_normalized.txt','r') as f2:
         for lines in f2:
             lines=lines.strip('\n\r')
             data=Clientpath+lines+' '
             flag=os.path.isfile(data)
             if flag==False:
                print '{} does not exist!\n'.format(data)
             idx=data.find('bmp')
             outputline = '{}  {} \n'.format(data[0:idx+3],1)
             f1.write(outputline)  
      with open('imposter_train_normalized.txt','r') as f2:
         for lines in f2:
             lines=lines.strip('\n\r')
             data=Imposterpath+lines+' '
             flag=os.path.isfile(data)
             if flag==False:
                print '{} does not exist !\n'.format(data)
             idx=data.find('bmp')
             outputline = '{}  {} \n'.format(data[0:idx+3],0)
             f1.write(outputline)            
    with open('testlist.txt','w') as f1:
      with open('client_test_normalized.txt','r') as f2:
         for lines in f2:
             lines=lines.strip('\n\r')
             data=Clientpath+lines+' '
             flag=os.path.isfile(data)
             if flag==False:
                print '{} does not exist!\n'.format(data)
             idx=data.find('bmp')
             outputline = '{}  {} \n'.format(data[0:idx+3],1)
             f1.write(outputline)  
      with open('imposter_test_normalized.txt','r') as f2:
         for lines in f2:
             lines=lines.strip('\n\r')
             data=Imposterpath+lines+' '
             flag=os.path.isfile(data)
             if flag==False:
                print '{} does not exist !\n'.format(data)
             idx=data.find('bmp')
             outputline = '{}  {} \n'.format(data,[0:idx+3],0)
             f1.write(outputline) 
             
             
    

def main():
    generate_list(Clientpath,Imposterpath)
    

if __name__ == '__main__':
    main()
