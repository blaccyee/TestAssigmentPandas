"""

Used here randomly generated dataset was created with https://extendsclass.com/csv-generator.html

To see how it works please follow this link -
https://colab.research.google.com/drive/1_9wgJl-qb1d1jSgDBE30MNl_Hf2F72eI?usp=sharing

"""

import pandas as pd


def prepare_generated_csv() -> pd.DataFrame:
    """
    Reads and corrects a dataframe from a generated csv file
    Make sure you have generated file in the directory
    :return: a Pandas DataFrame for testing sessions update
    """
    try:
        df = pd.read_csv('./generated0.csv')
        df['timestamp'] = pd.to_datetime(df['timestamp'], format="%Y-%m-%d %H:%M:%S")
        df = df.sort_values(by='timestamp').reset_index(drop=True)
        return df

    except FileNotFoundError:
        print("Warning: Please, add generated file into a project directory!")
        return None


def update_with_sessions(df: pd.DataFrame):
    """
    Puts session numbers within 3 minutes for each customer
    :param df: Pandas DataFrame
    :return: None, the given dataframe is updated in-place
    """
    cacl_session = lambda time: time.diff().gt(pd.Timedelta('3m')).cumsum()
    df['session_id'] = df.groupby('customer_id', group_keys=False)[['timestamp']].apply(cacl_session) + 1


if __name__ == '__main__':
    given_df_exists = False  # a DataFrame which we have to update
    if given_df_exists:
        pass
    else:                    # if we don't have a given df let's update generated one
        df = prepare_generated_csv()
        update_with_sessions(df)
