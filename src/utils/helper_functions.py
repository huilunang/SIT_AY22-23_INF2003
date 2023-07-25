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
    end_date = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    start_date = end_date - datetime.timedelta(days=6)
    df = maria_q.getUserRecycleAcivity()
    # Map the day of the week to its corresponding name
    day_mapping = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }

    df["DayOfWeek"] = df["DayOfWeek"].map(day_mapping)
    print(df["DayOfWeek"])

    # Create a DataFrame with all days of the week
    all_days = pd.DataFrame({"DayOfWeek": list(day_mapping.values())})
    df = pd.merge(all_days, df, on="DayOfWeek", how="left")
    df["TotalRecycled"] = df["TotalRecycled"].fillna(0)

    # Determine the starting day index based on the current day of the week
    current_day_index = end_date.weekday()

    # Calculate the number of days to offset the x-axis labels
    if current_day_index < 5:
        current_day_index += 2
    elif current_day_index >= 5 & current_day_index <= 6:
        current_day_index = current_day_index - 5

    # Rearrange the days of the week starting from the current day
    print(current_day_index)
    all_days = all_days.reindex(
        list(range(current_day_index, 7)) + list(range(0, current_day_index))
    )
    print(all_days)
    # Reset the index of the DataFrame
    all_days.reset_index(drop=True, inplace=True)

    # Merge the all_days DataFrame with the data from the database query
    df = pd.merge(all_days, df, on="DayOfWeek", how="left")

    # Fill any missing values in TotalRecycled with 0
    df["TotalRecycled"].fillna(0, inplace=True)

    # Create a line graph using matplotlib
    plt.plot(all_days["DayOfWeek"], df["TotalRecycled"], marker="o")

    # Set the chart title and labels
    plt.title("Your Total Number of Recycled Items in the Last 7 Days")
    plt.xlabel("Day of the Week (GMT+8)")
    plt.ylabel("Total Recycled")

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Set the y-axis lower limit to 0
    plt.ylim(bottom=0)

    # Display the chart
    plt.savefig("static/assets/graphs/recentActivity.png")


def generateActivities(result):
    end_date = datetime.datetime.now(pytz.timezone("Asia/Singapore")).date()
    start_date = end_date - datetime.timedelta(days=59)
    df = result

    # Create a DataFrame with all dates of the last 60 days
    all_days = pd.DataFrame(
        {"Date": pd.date_range(start=start_date, end=end_date, freq="D")}
    )

    # Convert 'Date' column to 'datetime64[ns]' data type
    df["Date"] = pd.to_datetime(df["Date"])

    # Merge the all_days DataFrame with the data from the database query
    df = pd.merge(all_days, df, on="Date", how="left")
    df["TotalRecycled"].fillna(0, inplace=True)

    # Calculate the intervals for plotting 7 points
    interval = len(df) // 7
    plot_points_indices = list(range(0, len(df), interval))
    plot_points = df.iloc[plot_points_indices]

    # Calculate the cumulative total recycled within each interval group
    df["IntervalGroup"] = df.index // interval
    df["CumulativeTotalRecycled"] = df.groupby("IntervalGroup")["TotalRecycled"].sum()

    # Create a line graph using matplotlib
    plt.figure(figsize=(10, 6))  # Adjust the figure size
    plt.plot(df["CumulativeTotalRecycled"], marker="x", linestyle="-", color="b")

    # Set the chart title and labels
    plt.title(
        "Cumulative Total Number of Recycled Items in the Last 60 Days", fontsize=16
    )
    plt.xlabel("Increments by Weeks", fontsize=12)
    plt.ylabel("Cumulative Total Recycled", fontsize=12)

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45, ha="right", fontsize=10)

    # Set the y-axis lower limit to 0
    plt.ylim(bottom=0)

    # Add grid lines to the plot
    plt.grid(True, linestyle="--", alpha=0.7)

    # Display the chart
    plt.tight_layout()  # Adjusts the layout to prevent overlapping labels
    plt.savefig("static/assets/graphs/last60DaysActivity.png")
