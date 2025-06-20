from statsbombpy import sb
import pandas as pd
from mplsoccer import VerticalPitch,Pitch

events_df = sb.competition_events(
country="Germany",
division="1. Bundesliga",
season="2023/2024",
gender="male")

# And to add 360 data:

frames_df = sb.competition_frames(
country="Germany",
division="1. Bundesliga",
season="2023/2024",
gender="male")

frames_df.rename(columns={'event_uuid': 'id'}, inplace = True)
merged_df=pd.merge(frames_df, events_df,
how="left", on=["match_id","id"])
