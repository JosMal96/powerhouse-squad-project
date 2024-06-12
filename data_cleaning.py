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
    'TimeOfDay_Evening', 'TimeOfDay_Night' , 'general diffuse flows', 'diffuse flows', 
    'Zone 1 Power Consumption', 'Zone 2  Power Consumption', 'Zone 3  Power Consumption'
    ]

    # Select only the expected columns
    tetouan_df_cleaned = tetouan_df[expected_columns]

    def rename_col(pc_data_col:str):
        """
        Renames columns in the power consumption dataframe
    
        Arguments : pc_data_col  - column in power comsumption dataframe
        Returns : Str - reformatted column
        """
        if pc_data_col == 'DateTime_cleaned':
            return 'DateTime' 
        if pc_data_col == 'Temperature':
            return 'Temp'
        if pc_data_col == 'Wind Speed':
            return 'Wind_Speed'
        if 'Zone' in pc_data_col:
            zone = pc_data_col.split('Power Consumption')[0].strip().replace(' ', '_')
            return zone + '_PC'
        if 'Day' in pc_data_col and '_' in pc_data_col:
            return pc_data_col.split('_')[1]
        return pc_data_col

    tetouan_df_cleaned.columns = [rename_col(col) for col in tetouan_df_cleaned.columns]
    
    
    # Convert temperature from C to F 
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    tetouan_df_cleaned['Temp'] = tetouan_df_cleaned['Temp'].apply(celsius_to_fahrenheit)
    

    # Converting columns from boolean to int
    columns_to_convert = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Morning', 'Afternoon', 'Evening', 'Night']
    for column in columns_to_convert:
        tetouan_df_cleaned[column] = tetouan_df_cleaned[column].astype(int)

    # Convert DateTime columns into months and season column
    tetouan_df_cleaned['Month'] = tetouan_df_cleaned['DateTime'].dt.month
    
    columns = ['Month', 'Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Morning','Afternoon', 'Evening', 'Night', 'Temp', 'Humidity', 'Wind_Speed','general diffuse flows', 'diffuse flows', 'Zone_1_PC', 'Zone_2_PC', 'Zone_3_PC']
    tetouan_df_cleaned = tetouan_df_cleaned[columns]

    return tetouan_df_cleaned

if __name__ == "__main__":
    cleaned_data = fetch_and_clean_data()
    print(cleaned_data.head())