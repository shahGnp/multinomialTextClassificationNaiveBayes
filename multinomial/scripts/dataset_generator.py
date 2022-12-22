import fitz
import pandas as pd
import os

def get_all_info(title,text):
    path=os.getcwd()
    path=path+'//'+'dataset'
    for folder in os.listdir(path):
        for file in os.listdir(path+'\\'+folder):
            title.append(folder)
            text.append(file)

    return title,text


def get_Data_and_Label(df):
    title=[]
    text=[]
    title,text=get_all_info(title,text)
    df['Text']=pd.DataFrame(text)
    df['Title']=pd.DataFrame(title) 
    return df,title

def Generator():
    df=pd.DataFrame(columns=['Text','Title'])
    df,title=get_Data_and_Label(df) # Here we got dataframe with folder name and file name
#     df=pre_process_Data_and_Label(df,title) #Getting file names
    df.to_csv('Dataset_final.csv')



if __name__=='__main__':
    Generator()
    print('Dataset Generated Successfully')