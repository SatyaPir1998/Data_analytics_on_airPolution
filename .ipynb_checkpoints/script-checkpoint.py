import pandas as pd


if __name__ == "__main__":
    data_df = pd.read_csv('data.csv', sep=',') # I've download the data from the link
    # Data cleaning section
    # Converting all the nan values to some other format for future calculation
    data_df.rspm.fillna(0.0,inplace=True) # convert nan values to float 0.0
    data_df.spm.fillna(0.0,inplace=True)    # convert nan to float 0.0
    data_df.pm2_5.fillna(0.0,inplace=True)  # convert nan to float 0.0
    data_df.date = data_df.date.astype('str')   # convert datatype to str to calculate the year and month

    ## getting the year value by using the date column and replacing the nan values with 0000

    data_df['year'] = data_df.date.apply(lambda x: x.split('-')[0] if x != 'nan' else '0000')

    ## getting the month value by using the date column and replacing the nan values with 00

    data_df['month'] = data_df.date.apply(lambda x: x.split('-')[1] if x != 'nan' else '00')

    ########## Top_10_polluted_cities :-

    cities_polluted = data_df.groupby(['year', 'location'])['so2','no2','rspm','spm', 'pm2_5'].mean().reset_index()
    top_10_polluted_cities = cities_polluted.sort_values(by=['so2','no2','rspm','spm', 'pm2_5'], ascending=False).head(10).reset_index(drop=True)

    ########## Top_10_polluted_states :-

    state_polluted = data_df.groupby(['year', 'state'])['so2','no2','rspm','spm', 'pm2_5'].mean().reset_index()
    top_10_polluted_states = state_polluted.sort_values(by=['so2','no2','rspm','spm', 'pm2_5'], ascending=False).head(10).reset_index(drop=True)
    
    ########## Month wise Air quality od Delhi for the year 2021

    delhi_2021 = data_df.query("location == 'Delhi' and year == '2021'") # record does not present for the year 2021