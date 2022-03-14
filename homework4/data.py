# code marking Jayson Tatum's statsitical growth through his three postseasons.
# graphs/plots give a visual representation on how he has gotten better every year in the league

import requests
import pandas as pd
import numpy as np
from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonTypeAllStar
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.library.parameters import SeasonID
from nba_api.stats.endpoints import playergamelog
import matplotlib.pyplot as plt

p_dict = players.get_active_players()
for player in p_dict:
    if player['full_name'] == "Jayson Tatum":
        JT_id = player['id']

#print (JT_id)

JT_2018 = playergamelog.PlayerGameLog(player_id=JT_id, season= '2017', season_type_all_star= SeasonTypeAllStar.playoffs)
JT_2018_df = JT_2018.get_data_frames()[0]
df_2018 = pd.DataFrame(JT_2018_df)
csv_2018 = df_2018.to_csv("2018.csv")
csv_2018

JT_2019 = playergamelog.PlayerGameLog(player_id=JT_id, season= '2018', season_type_all_star= SeasonTypeAllStar.playoffs)
JT_2019_df = JT_2019.get_data_frames()[0]
df_2019 = pd.DataFrame(JT_2019_df)
csv_2019 = df_2019.to_csv("2019.csv")
csv_2019

JT_2020 = playergamelog.PlayerGameLog(player_id=JT_id, season= '2019', season_type_all_star= SeasonTypeAllStar.playoffs)
JT_2020_df = JT_2020.get_data_frames()[0]
df_2020 = pd.DataFrame(JT_2020_df)
csv_2020 = df_2020.to_csv("2020.csv")
csv_2020

# JT_all = playergamelog.PlayerGameLog(player_id=JT_id, season= SeasonAll.all, season_type_all_star= SeasonTypeAllStar.playoffs)
# JT_all_df = JT_all.get_data_frames()[0]
# df_all = pd.DataFrame(JT_all_df)
# csv_all = df_all.to_csv("all.csv")

years = ['Playoffs 2018', 'Playoffs 2019', 'Playoffs 2020']
ppg = [round(df_2018['PTS'].sum()/19, 1), round(df_2019['PTS'].sum()/9, 1), round(df_2020['PTS'].sum()/17, 1)] #19 playoff games 2018, 9 in 2019, 17 in 2020
apg = [round(df_2018['AST'].sum()/19, 1), round(df_2019['AST'].sum()/9, 1), round(df_2020['AST'].sum()/17, 1)]
rpg = [round(df_2018['REB'].sum()/19, 1), round(df_2019['REB'].sum()/9, 1), round(df_2020['REB'].sum()/17, 1)]
fg = [round(df_2018['FG_PCT'].sum()/19, 3) * 100, round(df_2019['FG_PCT'].sum()/9, 2) * 100, round(df_2020['FG_PCT'].sum()/17, 3) * 100]
three = [round(df_2018['FG3_PCT'].sum()/19, 3) * 100, round(df_2019['FG3_PCT'].sum()/9, 3) * 100, round(df_2020['FG3_PCT'].sum()/17, 3) * 100]
ft = [round(df_2018['FT_PCT'].sum()/19, 3) * 100, (round(df_2019['FT_PCT'].sum()/9, 4) * 100), round(df_2020['FT_PCT'].sum()/17, 3) * 100]
plusminus = [df_2018['PLUS_MINUS'].sum(), df_2019['PLUS_MINUS'].sum(), df_2020['PLUS_MINUS'].sum()]

# plt.bar(years, ppg)
# plt.title("Jayson Tatum's PPG by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Points Per Game")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(ppg):
#     plt.text(xlocs[i] - .11, v - 1.4, str(v), fontsize = 12)
# plt.show()

# plt.bar(years, apg)
# plt.title("Jayson Tatum's APG by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Assists Per Game")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(apg):
#     plt.text(xlocs[i] - .07, v - .25, str(v), fontsize = 12)
# plt.show()
# plt.close()

# plt.bar(years, rpg)
# plt.title("Jayson Tatum's RPG by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Rebounds Per Game")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(rpg):
#     plt.text(xlocs[i] - .075, v - .6, str(v), fontsize = 12)
# plt.show()

# plt.bar(years, fg)
# plt.title("Jayson Tatum's FG Percentage by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Field Goal Percentage Per Game")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(fg):
#     plt.text(xlocs[i] - .11, v - 2.25, str(v), fontsize = 12)
# plt.show()

# plt.bar(years, three)
# plt.title("Jayson Tatum's Three Point Percentage by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Three Point Percentage Per Game")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(three):
#     plt.text(xlocs[i] - .11, v - 1.75, str(v), fontsize = 12)
# plt.show()

plt.bar(years, ft, color = (1.0, 0.0, 0.0, 1.0))
plt.title("Jayson Tatum's Free Throw Percentage by Postseason")
plt.xlabel("Playoff Year")
plt.ylabel("Free Throw Percentage Per Game")
xlocs, xlabs = plt.xticks()
plt.xticks(xlocs, xlabs)
for i, v in enumerate(ft):
    plt.text(xlocs[i] - .12, v - 3.75, str(v), fontsize = 12)
plt.show()

# plt.bar(years, plusminus)
# plt.title("Jayson Tatum's +/- by Postseason")
# plt.xlabel("Playoff Year")
# plt.ylabel("Playoff Net Plus/Minus")
# xlocs, xlabs = plt.xticks()
# plt.xticks(xlocs, xlabs)
# for i, v in enumerate(plusminus):
#     plt.text(xlocs[i] - .11, v + 2, str(v), fontsize = 12)
# plt.show()