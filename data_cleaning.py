import pandas as pd
from ucimlrepo import fetch_ucirepo

def fetch_and_clean_data():
    # fetch dataset 
    tetouan = fetch_ucirepo(id=849) 
    
    # data (as pandas dataframes) 
    X = tetouan.data.features 
    y = tetouan.data.targets 
    
    # Convert X Datetime column timestamps into datetime format
    X.loc[:, 'DateTime_cleaned'] = pd.to_datetime(X['DateTime'])

    # Create new columns to show day of the week and category of the day from the DateTime_cleaned column
    X.loc[:, 'DayOfWeek'] = X['DateTime_cleaned'].dt.day_name()
    
    def categorize_time_of_day(hour):
        if 5 <= hour < 12:
            return 'Morning'
        elif 12 <= hour < 17:
            return 'Afternoon'
        elif 17 <= hour < 21:
            return 'Evening'
        else:
            return 'Night'

    # Apply the function to create the 'TimeOfDay' column
    X.loc[:, 'TimeOfDay'] = X['DateTime_cleaned'].dt.hour.apply(categorize_time_of_day)

    # Concatenate tetouan features and targets into a single dataframe
    tetouan_df = pd.concat([X, y], axis=1)

    # Get_dummies for categorical columns
    tetouan_df = pd.get_dummies(tetouan_df, columns=['DayOfWeek', 'TimeOfDay'])

    # Reorganize the 3 power consumption to the end of the column list 
    # Ensure all columns exist in the DataFrame
    expected_columns = [
        'DateTime_cleaned', 'Temperature', 'Humidity', 'Wind Speed',
        'DayOfWeek_Monday', 'DayOfWeek_Tuesday', 'DayOfWeek_Wednesday', 
        'DayOfWeek_Thursday', 'DayOfWeek_Friday', 'DayOfWeek_Saturday', 
        'DayOfWeek_Sunday', 'TimeOfDay_Morning', 'TimeOfDay_Afternoon', 
        'TimeOfDay_Evening', 'TimeOfDay_Night', 
        'Zone 1 Power Consumption', 'Zone 2  Power Consumption', 'Zone 3  Power Consumption'
    ]

    # Select only the expected columns
    tetouan_df_cleaned = tetouan_df[expected_columns]

    

    return tetouan_df_cleaned

if __name__ == "__main__":
    cleaned_data = fetch_and_clean_data()
    print(cleaned_data.head())