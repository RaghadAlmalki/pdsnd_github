import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    city = ''
    print("Hello! Let's explore some US bikeshare data!")

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        print("Would you like to see data for chicago, new york city, or washington?")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("Sorry you choose city that is not include in our data, please choose another city. ")

    MONTH_LIST = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = ''
    while month not in MONTH_LIST:
        print("Which month? january, february, march, april, may, june or all")
        month = input().lower()

        if month not in MONTH_LIST:
            print("Sorry you choose month that is not include in our data, please choose another month. ")

    DAY_LIST = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    day = ''
    while day not in DAY_LIST:
        print("Which day? sunday, monday, tuesday, wednesday, thursday, friday, saturday or all")
        day = input().lower()

        if day not in DAY_LIST:
            print("Sorry choose invalid day")
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most common Month:', common_month)

    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', popular_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly Start station: ", common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly end station: ", common_end_station)

    # display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station'])
    combination_station = combination.size().sort_values(ascending=False).head(1)
    print("the most frequent combination of start station and end station trip",combination_station )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("total travel time: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("total travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print("Counts of user type: ", count_user_type)

    # Display counts of gender
    if city != 'washington':
        count_of_gender = df['Gender'].value_counts()
        print("Counts of gender: ", count_of_gender)

    # Display earliest, most recent, and most common year of birth
        earlist_year = df['Birth Year'].min()
        print("The earliest year: ", earlist_year)

        most_recent_year = df['Birth Year'].max()
        print("The most recent year: ", most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print("The most common year: ", most_common_year)

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def row_data(df):
        print('Enter yes to see row data, enter no to skip')
        row = 0
        while (input() != 'no'):
            row += 5
            print(df.head(row))



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
