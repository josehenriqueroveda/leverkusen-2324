# --- scouting_report.ipynb ---

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from report_generator import ScoutingReport

# Carregar o arquivo (ajuste o caminho se necessário)
data_path = 'merged_data.csv'

# Criar o objeto de relatório
report = ScoutingReport(data_path)

# Definir partida e time desejado
match_id = 3895232
team_name = 'Bayer Leverkusen'
player_sonar = 'Florian Wirtz'

# Filtrar dados do jogo
report.filter_match(match_id, team_name)

# Estatísticas numéricas
stats = report.calculate_summary_stats()
print("\n=== Estatísticas da Partida ===")
for k, v in stats.items():
    print(f"{k}: {v}")

# Layout dos gráficos
fig, axs = plt.subplots(3, 2, figsize=(16, 18))

# Gráfico 1 - Mapa de passes
report.plot_pass_map(axs[0,0])

# Gráfico 2 - Heatmap de zonas
report.plot_heatmap(axs[0,1])

# Gráfico 3 - Pass Sonar
report.plot_pass_sonar(axs[1,0], player_name=player_sonar)

# Gráfico 4 - Passing Network PRO
report.plot_passing_network(axs[1,1])

# Gráfico 5 - Zones of Control
report.plot_zones_of_control(axs[2,0])

# Gráfico 6 - Espaço livre
axs[2,1].axis('off')

plt.suptitle(f'Relatório Profissional - {team_name} (match {match_id})', fontsize=20)
plt.tight_layout()
plt.show()
