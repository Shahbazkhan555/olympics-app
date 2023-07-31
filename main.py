import streamlit as st
import preprocessor, helper
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff

# importing data
df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")

# processing data
df = preprocessor.preprocess(df, region_df)

# creating sidebar with options
st.sidebar.title("Olympics Data Analysis")
user_menu = st.sidebar.radio("Choose the Options", ("Medal Tally", "Overall Analysis","Country-wise Analysis", "Athlete-wise Analysis"))


if user_menu == "Medal Tally":
    # Years and Country dropbox
    st.sidebar.header("Medal Tally")
    Year, Country = helper.country_year_list(df)
    selected_year = st.sidebar.selectbox("Select Year", Year)
    selected_country = st.sidebar.selectbox("Select Country", Country)

    # Displaying medal tally of every country with most Gold Medal
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == "Overall" and selected_country == "Overall":
        st.title("Overall Medal Tally")
    if selected_year != "Overall" and selected_country == "Overall":
        st.title("Medal Tally in " + str(selected_year) + " Olympics")
    if selected_year == "Overall" and selected_country != "Overall":
        st.title(selected_country + " overall performance")
    if selected_year != "Overall" and selected_country != "Overall":
        st.title(selected_country + " performance in " + str(selected_year))

    st.table(medal_tally)

if user_menu == "Overall Analysis":
    # no of olympics, cities, events, sports, athletes, nations
    years = df["Year"].nunique() - 1  # as 1906 olympics committee so removing it
    cities = df["City"].nunique()
    events = df["Event"].nunique()
    sports = df["Sport"].nunique()
    athletes = df["Name"].nunique()
    nations = df["region"].nunique()

    # top statistics
    st.title("Top Statistics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Editions")
        st.title(nations)
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.header("Events")
        st.title(events)
    with col2:
        st.header("Nations")
        st.title(nations)
    with col3:
        st.header("Athletes")
        st.title(athletes)

    # no of nations participated in olympics over the time
    nations_over_time = helper.participating_country_over_time(df)
    fig = px.line(nations_over_time, x='Edition', y='No of Countries')
    st.title("Participating Nations over the years")
    st.plotly_chart(fig)

    # no of events in olympics increased/decreased over the time
    events_over_time = helper.participating_event_over_time(df)
    fig = px.line(events_over_time, x='Edition', y='No of Events')
    st.title("Events over the years")
    st.plotly_chart(fig)

    # no of athletes participated in olympics over the time
    athletes_over_time = helper.participating_athlete_over_time(df)
    fig = px.line(athletes_over_time, x='Edition', y='No of Athletes')
    st.title("Athletes over the years")
    st.plotly_chart(fig)

    # heatmap of events with respect to year and sport
    st.title("No. of Event over time(Every Sport)")
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(["Sport", "Year", "Event"])
    ax = sns.heatmap(pd.pivot_table(x, index="Sport", columns="Year", values="Event", aggfunc="count").fillna(0), annot=True)
    st.pyplot(fig)

    # making function for to display the most successful athletes
    st.title("Most Successful Athletes")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, "Overall")
    selected_sport = st.selectbox("Choose a Sport", sport_list)
    successful_athletes = helper.most_successful(df, selected_sport)
    st.table(successful_athletes)


if user_menu == "Country-wise Analysis":

    st.sidebar.title('Country-wise Analysis')

    # medal tally over the years of a country
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox("Choose a Country", country_list)
    country_medal = helper.country_medal_tally(df, selected_country)
    fig = px.line(country_medal, x="Year", y="Medal")
    st.title(selected_country + " Medal Tally over the years")
    st.plotly_chart(fig)

    # What countries are good at what sport (heatMap)
    st.title(selected_country + " best in the following Sports")
    ptable = helper.country_best_sport_heatmap(df, selected_country)
    fig, ax = plt.subplots(figsize=(20,20))
    ax = sns.heatmap(ptable, annot=True)
    st.pyplot(fig)

    # top athletes of a country
    st.title("Top Athletes of " + selected_country)
    best_athletes = helper.country_best_athletes(df, selected_country)
    st.table(best_athletes)


if user_menu == "Athlete-wise Analysis":

    # At which age of athlete the probability of winning Gold, Silver or Bronze is high or low
    athlete_df = df.drop_duplicates(["Name", "region"])  # grabbing athlete name by dropping duplicates athletes name
    x1 = athlete_df["Age"].dropna()
    x2 = athlete_df[athlete_df["Medal"] == "Gold"]["Age"].dropna()
    x3 = athlete_df[athlete_df["Medal"] == "Silver"]["Age"].dropna()
    x4 = athlete_df[athlete_df["Medal"] == "Bronze"]["Age"].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4], ["Overall Age", "Gold Medalist", "Silver Medalist", "Bronze Medalist"],
                       show_rug=False, show_hist=False)
    fig.update_layout(autosize=False, width=900, height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    # Probability of winning GOLD Medal at every sport wrt Athlete age
    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    # Men and women participation in olympics over the years
    st.title("Men Vs Women Participation Over the Years")
    final = helper.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=900, height=600)
    st.plotly_chart(fig)

    # weight and height distribution of Athlete over the sport
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    # temp_df = helper.weight_vs_height(df, selected_sport)
    # fig, ax = plt.subplots()
    # ax = sns.scatterplot(temp_df['Weight'], temp_df['Height'], hue=temp_df['Medal'],style=temp_df['Sex'], s=60)
    # st.pyplot(fig)


    temp_df = helper.weight_vs_height(df, selected_sport)
    fig, ax = plt.subplots()
    ax = sns.scatterplot(data=temp_df, x='Weight', y='Height', hue='Medal', style='Sex', s=60)
    st.pyplot(fig)


    








