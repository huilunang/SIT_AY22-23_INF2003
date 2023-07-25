import utils.mariadb_queries as maria_q
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pytz


def get_suggestions(search_query):
    if len(search_query) >= 2:
        suggested_words = [row[0] for row in maria_q.suggestion(search_query)]

        return suggested_words
    return False


def generateGraph():
    end_date = datetime.datetime.now(pytz.timezone('Asia/Singapore')).date()
    start_date = end_date - datetime.timedelta(days=6)
    df = maria_q.getRecycleAcivity()
    # Map the day of the week to its corresponding name
    day_mapping = {
        1: 'Sunday',
        2: 'Monday',
        3: 'Tuesday',
        4: 'Wednesday',
        5: 'Thursday',
        6: 'Friday',
        7: 'Saturday'
    }

    df['DayOfWeek'] = df['DayOfWeek'].map(day_mapping)
    print(df['DayOfWeek'] )

    # Create a DataFrame with all days of the week
    all_days = pd.DataFrame({'DayOfWeek': list(day_mapping.values())})
    df = pd.merge(all_days, df, on='DayOfWeek', how='left')
    df['TotalRecycled'] = df['TotalRecycled'].fillna(0)

    # Determine the starting day index based on the current day of the week
    current_day_index = end_date.weekday()

    # Calculate the number of days to offset the x-axis labels
    if current_day_index < 5:
        current_day_index+=2
    elif current_day_index >= 5 & current_day_index <= 6:
        current_day_index = current_day_index-5
        
    # Rearrange the days of the week starting from the current day
    print(current_day_index)
    all_days = all_days.reindex(list(range(current_day_index, 7)) + list(range(0, current_day_index)))
    print(all_days)
    # Reset the index of the DataFrame
    all_days.reset_index(drop=True, inplace=True)

    # Merge the all_days DataFrame with the data from the database query
    df = pd.merge(all_days, df, on='DayOfWeek', how='left')

    # Fill any missing values in TotalRecycled with 0
    df['TotalRecycled'].fillna(0, inplace=True)

    # Create a line graph using matplotlib
    plt.plot(all_days['DayOfWeek'], df['TotalRecycled'], marker='o')

    # Set the chart title and labels
    plt.title('Total Number of Recycled Items in the Last 7 Days')
    plt.xlabel('Day of the Week (GMT+8)')
    plt.ylabel('Total Recycled')

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Set the y-axis lower limit to 0
    plt.ylim(bottom=0)

    # Display the chart
    plt.savefig('static/assets/graphs/recentActivity.png')