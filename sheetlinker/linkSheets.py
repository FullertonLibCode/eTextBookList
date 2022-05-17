#%%
import pandas as pd
#alma_df = pd.read_excel('OwnedEbooks2022.xlsx',sheet_name=0)
# import alma data
alma_df = pd.read_csv('alma.csv')	
print(alma_df.shape)
# convert ISBN from ; seperated to list
alma_df.ISBN=alma_df['ISBN'].str.split(';')
# use explode method to flatten the ISBN cell
alma_df = alma_df.explode('ISBN')
print(alma_df.shape)
# check for any extra spaces and drop any where ISBN is missing
alma_df.ISBN=alma_df.ISBN.str.strip(' ')
alma_df.dropna(subset=['ISBN'], inplace=True)
print(alma_df.shape)
# push results to a file
alma_df.to_csv('explodedISBN.csv')

#%%
#courses_df = pd.read_excel('OwnedEbooks2022.xlsx',sheet_name=1)
# import bookstore information and force ISBN to string so it doesn't get treated like a float
courses_df = pd.read_csv('bookstore.csv',converters={'ISBN':str})

courses_df.ISBN = courses_df.ISBN.str.strip(' ')
print(courses_df.shape)
# filter out any entries where there is no ISBN
courses_df = courses_df[courses_df['ISBN'].astype(bool)]
print(courses_df.shape)
# drop any where ISBN is NA; should be unnecessary since previous filter
courses_df.dropna(subset=['ISBN'], inplace=True)
print(courses_df.shape)
#%%
# merge alma and bookstore data, dropping all where there is no match
combined_df = courses_df.merge(alma_df,on='ISBN',how='inner')
# dump results to file
combined_df.to_excel('textbookInput.xlsx')
print(combined_df.shape)

# %%
# %%

