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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Which city would you like to see data for? We offer data for Chicago, New York City, and Washington ').lower()
    while city:
        if city in("chicago", "new york city", "washington"):
            print("Ok, let's explore {}'s data!".format(city))
        else: 
            print("That isn't a valid city")
        break

          
                  

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    month = input('For which month would you like to see data? ').title()
        
                             
    while month:
        if month in months:
            print('Ok! Let\'s take a peek at data for the month of {}'.format(month))
        else: 
            print("Data for that month isn't available!")
        break              
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dow = input('What day of the week are you planning your trip? ').title()
    
    
    while dow:
        if dow in day:
            print('Alrighty, let\'s filter for {}'.format(dow))
        else:
            print('That\'s not a valid day!')
        break

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] =  df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
#    print(type(month))
#    month = int(month)
#    print(type(month))
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    busiest_month = df['month'].mode()[0]
    print('The busiest month is {}'.format(busiest_month))
    # TO DO: display the most common day of week
    busiest_day = df['day_of_week'].mode()[0]
    print('The busiest day is {}'.format(busiest_day))
    # TO DO: display the most common start hour
    busiest_hour = df['hour'].mode()[0]
    print('The busiest hour is {}'.format(busiest_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most popular start station is {}'.format(start_station))
    # TO DO: display most commonly used end station
    #remove error
    end_station = df['End Station'].mode()[0]
    print('The most popular end station is {}'.format(end_station))
    # TO DO: display most frequent combination of start station and end station trip
    trip_combo = df["Start Station"] + " to " + df["End Station"]
    trip_combo.describe()
    popular_combo = trip_combo.describe()["top"]
    print('The most popular start/end combo is {}'.format(popular_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    agg_travel_time = df["Trip Duration"].sum()
    print("Total time of travel: ", agg_travel_time)

    # TO DO: display mean travel time
    average_travel_time = df["Trip Duration"].mean()
    print("The average travel-time: ", average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types - counts: ", df["User Type"].value_counts())

    # TO DO: Display counts of gender
    gender_count = df["Gender"].value_counts()
try:   
    print('Gender data:', gender_count)
except:
    print('Data for Washington doesn\'t exist')


        



    # TO DO: Display earliest, most recent, and most common year of birth
try:
    min_year = df["Birth Year"].min()
    max_year = df["Birth Year"].max()
    most_common = df["Birth Year"].mode()[0]
    print("the earliest year is {}, the most recent year is {}, and the most common year is {}".format(min_year,max_year, most_common))
except:
    print('That data doesn\'t exist for Washington!')

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
    
def display_data():
    row_count = 0
    total_rows = df.count
while row_count <= total_rows:
        yes_no = input('Would you like to see five rows of data? Yes/No').lower()
if yes_no == 'yes':
    df_count = df.head(5)
    print(df_count)
    row_count += 5
    df_count += 5
else:
        print('Ok! No data for you')
        
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
