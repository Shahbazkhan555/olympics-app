import numpy as np


def fetch_medal_tally(df, Year, Country):
    # removing duplicates rows to count sum of medals properly
    medal_df = df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])
    flag = 0

    if Year == "Overall" and Country == "Overall":
        temp_df = medal_df

    if Year == "Overall" and Country != "Overall":
        flag = 1
        temp_df = medal_df[medal_df["region"] == Country]

    if Year != "Overall" and Country == "Overall":
        temp_df = medal_df[medal_df["Year"] == int(Year)]

    if Year != "Overall" and Country != "Overall":
        temp_df = medal_df[(medal_df["Year"] == int(Year)) & (medal_df["region"] == Country)]

    if flag == 1:
        # show the medals of all years of a particular country
        x = temp_df.groupby("Year").sum()[["Gold", "Silver", "Bronze"]].sort_values("Year").reset_index()
    else:
        x = temp_df.groupby("region").sum()[["Gold", "Silver", "Bronze"]].sort_values("Gold",
                                                                                      ascending=False).reset_index()

    x["total"] = x["Gold"] + x["Silver"] + x["Bronze"]

    return x


def country_year_list(df):

    Year = df["Year"].unique().tolist()
    Year.sort()
    Year.insert(0, "Overall")

    Country = np.unique(df["region"].dropna().values).tolist()
    Country.sort()
    Country.insert(0, "Overall")

    return Year, Country


# no of nations participated in olympics over the time
def participating_country_over_time(df):
    # per year how many countries participated
    nations_over_time = df.drop_duplicates(["Year", "region"])["Year"].value_counts().reset_index().sort_values("index")
    nations_over_time.rename(columns={"index": "Edition", "Year": "No of Countries"}, inplace=True)
    return nations_over_time


# no of events in olympics increased/decreased over the time
def participating_event_over_time(df):
    # per year how many evnets held
    events_over_time = df.drop_duplicates(["Year", "Event"])["Year"].value_counts().reset_index().sort_values("index")
    events_over_time.rename(columns={"index": "Edition", "Year": 'No of Events'}, inplace=True)
    return events_over_time


# no of athletes participated in olympics over the time
def participating_athlete_over_time(df):
    # per year how many evnets held
    athletes_over_time = df.drop_duplicates(["Year", "Name"])["Year"].value_counts().reset_index().sort_values("index")
    athletes_over_time.rename(columns={"index": "Edition", "Year": 'No of Athletes'}, inplace=True)
    return athletes_over_time


# making function for to display the most successful athletes
def most_successful(df, sport):
    temp_df = df.dropna(subset=["Medal"])
    if sport != "Overall":
        temp_df = temp_df[temp_df["Sport"] == sport]

    x = temp_df["Name"].value_counts().reset_index().head(15).merge(df, left_on="index", right_on="Name", how="left")[
        ["index", "Name_x", "Sport", "Event", "region"]].drop_duplicates("index")
    x.rename(columns={"index": "Name", "Name_x": "Meadals"}, inplace=True)
    return x


# medal tally over the years of a country
def country_medal_tally(df, selected_country):
    temp_df = df.dropna(subset=["Medal"])
    temp_df = temp_df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])

    new_df = temp_df[temp_df["region"] == selected_country]
    final_df = new_df.groupby("Year").count()["Medal"].reset_index()
    return final_df


# What countries are good at what sport (heatMap)
def country_best_sport_heatmap(df, selected_country):
    # What countries are good at what sport (heatMap)
    temp_df = df.dropna(subset=["Medal"])
    temp_df = temp_df.drop_duplicates(subset=["Team", "NOC", "Games", "Year", "City", "Sport", "Event", "Medal"])

    new_df = temp_df[temp_df["region"] == selected_country]
    ptable = new_df.pivot_table(index="Sport", columns="Year", values="Medal", aggfunc="count").fillna(0)
    return ptable


# most successful athletes of a country (top 15)
def country_best_athletes(df, country):
    temp_df = df.dropna(subset=["Medal"])

    temp_df = temp_df[temp_df["region"] == country]

    x = temp_df["Name"].value_counts().reset_index().head(10).merge(df, left_on="index", right_on="Name", how="left")[
        ["index", "Name_x", "Sport", "Event"]].drop_duplicates("index")
    x.rename(columns={"index": "Name", "Name_x": "Meadals"}, inplace=True)
    return x


# Dataframe of men and women participated in each year
def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final


# weight and heigt distribution of Athlete over the sport
def weight_vs_height(df, sport):
    # grabbing athlete name by dropping duplicates athletes name
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)
    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        return temp_df
    else:
        return athlete_df


