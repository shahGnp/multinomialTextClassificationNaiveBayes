import fitz
import pandas as pd
import os

def get_all_info(title,text):
    path=get_path()
    for folder in os.listdir(path):
        for file in os.listdir(path+'\\'+folder):
            title.append(folder)
            text.append(file)
    return title,text

def get_topics():
    path=get_path()
    return os.listdir(path)

def get_path():
      path=os.getcwd()
      path=path+'\\TextClassification\\Training\\dataset'
      return path

def get_Data_and_Label(df):
    title=[]
    text=[]
    title,text=get_all_info(title,text)
    df['Text']=pd.DataFrame(text)
    df['Title']=pd.DataFrame(title) 
    return df,title

def get_Text_from_pdf(info):
    path=get_path()
    path=path+'\\'+info['Title']
    file=info['Text']
    doc=fitz.open(path+'\\'+file)
    page=doc[0]
    content=page.get_text()
    return content

def pre_process_Data_and_Label(df,title):
    #Iterating over each index and getting content of each file.
    title=get_topics()
    print('This is your dataframe',df)
#     print('df.title: ',df['Title'])
    for i in range(df.shape[0]):
        df.at[i,'Text']=get_Text_from_pdf(df.iloc[i])
        df.at[i,'Title']= title.index(df['Title'][i]) if (df['Title'][i] in title) else None

#     print('The topics are:', (len(title)))
#     for i in range(len(title)):
#         df.loc[df['Title']==title[i],'Title']=i
    return df

def Generator():
    df=pd.DataFrame(columns=['Text','Title'])
    df,title=get_Data_and_Label(df) # Here we got dataframe with folder name and file name
    df=pre_process_Data_and_Label(df,title) #Getting file names
    df.to_csv('Dataset_final.csv')

if __name__=='__main__':
    Generator()
    print('Dataset Generated Successfully')