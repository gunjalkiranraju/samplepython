import pandas as pd


def reco(df1, df2):
    df = pd.DataFrame()
    df['Name_status'] = None
    df['Age_status'] = None
    df['Address_status'] = None
    df['Qualification_status'] = None
    for index, row in df1.iterrows():
        if row['Name'] in list(df2['Name']):
            if row['Name'] == df2.loc[df2['Name'] == row['Name'], 'Name'].values[0]:
                df.loc[index,'Name_status'] = 1
            else:
                df.loc[index,'Name_status'] = 0

            if str(row['Age']) == str(df2.loc[df2['Name'] == row['Name'], 'Age'].values[0]):
                df.loc[index, 'Age_status'] = 1
            else:
                df.loc[index, 'Age_status'] = 0

            if row['Address'] == df2.loc[df2['Name'] == row['Name'], 'Address'].values[0]:
                df.loc[index,'Address_status'] = 1
            else:
                df.loc[index,'Address_status'] = 0


            if row['Qualification'] == df2.loc[df2['Name'] == row['Name'], 'Qualification'].values[0]:
                df.loc[index,'Qualification_status'] = 1
            else:
                df.loc[index,'Qualification_status'] = 0
        else:
            df.loc[index,'Name']= 0
    print(df.to_string())


df1 = pd.read_csv("new.csv")
df2 = pd.read_excel('new1.xlsx')
# print(df1.to_string())
# print(df1.to_string())
df = reco(df1, df2)
# hi i am kiran i have am trying to use git