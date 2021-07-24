import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs]
   
    #Defining city, month, and day as a list.
    city = ['all', 'chicago', 'new york city', 'washington'] 
    day = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    while True:
        city = input("Which city are you traveling from: chicago, new york city, or washington?")
        city = city.lower()
        if city == 'chicago' or city =='new york city' or city == 'washington':
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month are you traveling: all, january, february, march, april, may, or june?")
        month = month.lower()
        if month in ('all','january','february','march','april','may','june'): 
            break
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day are you traveling: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?")
        day = day.lower()
        if day in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            break
    print('-'*40)        
    return (city, month, day)

def load_data(city,month, day):    
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]     
    if day != 'all':
            df = df[df['day'] == day.title()]             
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is', common_month)
    
    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most common day is', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('Most common start hour is', df['hour'].mode()[0])
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is', common_start_station)
    

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_frequent_combo = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('Most commonly used frequent combination of Start and End Station is', common_frequent_combo)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time is", total_time)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print('Mean travel time is', mean_travel)
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts for user types are', user_type)
               
    if city != 'washington':
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('The counts for Gender are', gender_count) 

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        print('The earliest birth year is', earliest_year)
        most_recent_year = df['Birth Year'].max()
        print('The most recent birth year is', most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('The most common birth year is', most_common_year)
          

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    """ Displays 5 rows of data at a time based on user input"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input("Do you wish to continue? (yes or no): ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


#Added change 1