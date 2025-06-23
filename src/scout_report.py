import pandas as pd
import numpy as np
from mplsoccer import Pitch


class ScoutReport:
    def __init__(self, df):
        self.df = df
        self.pitch = Pitch(
            pitch_type="statsbomb", pitch_color="green", line_color="white"
        )

    def filter_match(self, match_id, team):
        df_game = self.df[
            (self.df["match_id"] == match_id) & (self.df["team"] == team)
        ].copy()
        df_game[["x", "y"]] = df_game["location_x"].apply(pd.Series)
        df_game[["end_x", "end_y"]] = df_game["pass_end_location"].apply(pd.Series)
        self.df_game = df_game
        return df_game

    def plot_pass_map(self, ax):
        passes = self.df_game[
            (self.df_game["type"] == "Pass") & (self.df_game["pass_outcome"].isnull())
        ]
        self.pitch.draw(ax=ax)
        self.pitch.arrows(
            passes["x"],
            passes["y"],
            passes["end_x"],
            passes["end_y"],
            ax=ax,
            color="blue",
            alpha=0.5,
        )
        ax.set_title("Mapa de Passes")

    def plot_heatmap(self, ax):
        passes = self.df_game[
            (self.df_game["type"] == "Pass") & (self.df_game["pass_outcome"].isnull())
        ]
        bin_stat = self.pitch.bin_statistic(
            passes["x"], passes["y"], statistic="count", bins=(10, 8)
        )
        self.pitch.draw(ax=ax)
        self.pitch.heatmap(bin_stat, ax=ax, cmap="Reds", alpha=0.6)
        self.pitch.label_heatmap(bin_stat, ax=ax, color="black")
        ax.set_title("Zonas de Passes")

    def plot_passing_network(self, ax):
        passes = self.df_game[
            (self.df_game["type"] == "Pass") & (self.df_game["pass_outcome"].isnull())
        ]
        player_pos = (
            passes.groupby("player")
            .agg({"x": "mean", "y": "mean", "id": "count"})
            .reset_index()
        )
        player_pos.rename(columns={"id": "num_passes"}, inplace=True)
        pass_between = (
            passes.groupby(["player", "pass_recipient"])
            .size()
            .reset_index(name="pass_count")
        )
        pass_between = pass_between[pass_between["pass_count"] >= 3]
        self.pitch.draw(ax=ax)
        for _, row in pass_between.iterrows():
            passer = row["player"]
            recipient = row["pass_recipient"]
            count = row["pass_count"]
            p_pos = player_pos[player_pos["player"] == passer]
            r_pos = player_pos[player_pos["player"] == recipient]
            if not p_pos.empty and not r_pos.empty:
                x1, y1 = p_pos["x"].values[0], p_pos["y"].values[0]
                x2, y2 = r_pos["x"].values[0], r_pos["y"].values[0]
                self.pitch.lines(
                    x1,
                    y1,
                    x2,
                    y2,
                    ax=ax,
                    lw=count * 0.5,
                    color="#1f77b4",
                    alpha=0.4,
                    zorder=1,
                )
        sizes = player_pos["num_passes"] / player_pos["num_passes"].max() * 1200
        self.pitch.scatter(
            player_pos["x"],
            player_pos["y"],
            s=sizes,
            color="#d62728",
            edgecolors="black",
            linewidth=1.5,
            ax=ax,
            zorder=2,
        )
        for idx, row in player_pos.iterrows():
            ax.text(
                row["x"],
                row["y"],
                row["player"],
                ha="center",
                va="center",
                fontsize=8,
                color="white",
                bbox=dict(facecolor="black", alpha=0.6),
            )
        ax.set_title("Passing Network")

    def plot_zones_of_control(self, ax):
        players = self.df_game.groupby("player")[["x", "y"]].mean().reset_index()
        teams = np.array([True] * len(players))
        self.pitch.draw(ax=ax)
        team1, team2 = self.pitch.voronoi(players["x"], players["y"], teams)
        self.pitch.polygon(team1, ax=ax, fc="dodgerblue", ec="black", lw=1.5, alpha=0.4)
        self.pitch.scatter(
            players["x"], players["y"], ax=ax, c="blue", s=80, ec="black"
        )
        ax.set_title("Zonas de Controle")

    def plot_pressure_map(self, ax):
        pressures = self.df_game[(self.df_game["type"] == "Pressure")]
        self.pitch.draw(ax=ax)
        self.pitch.scatter(
            pressures["x"],
            pressures["y"],
            ax=ax,
            color="red",
            s=60,
            ec="black",
            alpha=0.6,
        )
        ax.set_title("Mapa de Pressão (Pressões aplicadas)")

    def calculate_summary_stats(self):
        passes = self.df_game[(self.df_game["type"] == "Pass")]
        total_passes = len(passes)
        completed_passes = len(passes[passes["pass_outcome"].isnull()])
        under_pressure = len(passes[passes["under_pressure"] == True])
        progressive_passes = len(passes[passes["end_x"] - passes["x"] > 15])
        final_third_passes = len(passes[passes["end_x"] > 80])
        stats = {
            "Total de passses": total_passes,
            "Passes completos": completed_passes,
            "% Acurácia": round(completed_passes / total_passes * 100, 2),
            "Passes sob pressão": under_pressure,
            "Passes progressivos (>15m de distância)": progressive_passes,
            "Passes no terço final": final_third_passes,
        }
        return stats
