import pandas as pd

# This part is abstraction on the extracting data from any datasources: DBs, APIs, etc.
def extract_data(path):
    df = pd.read_excel(path)
    return df


# Any needed data transformatiion could be performed in this part
def transform(df):
    df['WITHDRAWAL AMT'].fillna(0, inplace=True)
    df['DEPOSIT AMT'].fillna(0, inplace=True)
    grouped = df.groupby(['Account No']).sum()[['WITHDRAWAL AMT', 'DEPOSIT AMT']]
    return grouped


# Finally, the results of the transformation should be saved somewhere, for example, in the database
def load_data(df, name):
    df.to_csv('{}.csv'.format(name))


if __name__ == '__main__':
	df = extract_data('bank.xlsx')
	transformed_df = transform(df)
	load_data(transformed_df, 'result')