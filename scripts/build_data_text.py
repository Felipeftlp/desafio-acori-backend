import pandas as pd
import os

BASE_PATH = "data/lol"
OUTPUT_PATH = "data/matchs_by_league"

os.makedirs(OUTPUT_PATH, exist_ok=True)

matchinfo = pd.read_csv(f"{BASE_PATH}/matchinfo.csv")
bans = pd.read_csv(f"{BASE_PATH}/bans.csv")
kills = pd.read_csv(f"{BASE_PATH}/kills.csv")
monsters = pd.read_csv(f"{BASE_PATH}/monsters.csv")
structures = pd.read_csv(f"{BASE_PATH}/structures.csv")

for i, (_, match) in enumerate(matchinfo.iterrows(), start=1):
    match_id = i

    blue_team = match.get("blueTeamTag", "Desconecido")
    red_team = match.get("redTeamTag", "Desconecido")
    league = match.get("League", "Desconecido")

    content = []
    content.append("=== PARTIDA ===")
    content.append(f"MatchID: {match_id}")
    content.append(f"SourceAddress: {match.get('Address','')}")
    content.append(f"Campeonato: {league}")
    content.append(f"Ano: {match.get('Year', 'Desconhecida')}")
    content.append(f"Fase: {match.get('Type', 'Desconhecida')}")
    content.append(f"Temporada: {match.get('Season', 'Desconhecida')}")
    content.append(f"Time Azul: {blue_team}")
    content.append(f"Time Vermelho: {red_team}")

    blue_result = match.get('bResult', 0)
    red_result = match.get('rResult', 0)

    if blue_result > red_result:
        vencedor = match.get('blueTeamTag', '')
    elif red_result > blue_result:
        vencedor = match.get('redTeamTag', '')
    else:
        vencedor = "Empate"
    
    content.append(f"Vencedor: {vencedor}")
    content.append(f"Placar: {f"{blue_team}: {blue_result} x {red_result} :{red_team}"}")

    # BANS
    match_bans = bans[bans["Address"] == match["Address"]]
    if not match_bans.empty:
        content.append("\n=== BANS ===")
        for _, b in match_bans.iterrows():
            team = b.get("Team", "")
            
            for i in range(1, 6):
                ban_col = f"Ban_{i}"
                if ban_col in b and pd.notna(b[ban_col]):
                    content.append(f"{team} baniu {b[ban_col]}")

    # MONSTROS
    match_monsters = monsters[monsters["Address"] == match["Address"]]
    if not match_monsters.empty:
        content.append("\n=== OBJETIVOS ===")
        for _, m in match_monsters.iterrows():
            
            if m.get('Team', '')[0] == 'b':
                team = blue_team
            else:
                team = red_team

            content.append(
                f"Aos {m.get('Time', '')} minutos, "
                f"{team} eliminou {m.get('Type', '')}"
            )

    # KILLS
    match_kills = kills[kills["Address"] == match["Address"]]
    if not match_kills.empty:
        content.append("\n=== ABATES ===")
        for _, k in match_kills.head(10).iterrows():  # limitar p/ não explodir tamanho
            content.append(
                f"Aos {k.get('Time', '')} minutos, "
                f"{k.get('Killer', '')} eliminou {k.get('Victim', '')}"
            )

    with open(f"{OUTPUT_PATH}/league_{league}_info.txt", "a", encoding="utf-8") as f:
        f.write("\n".join(content))
        f.write("\n\n" + "="*50 + "\n\n")

print("Base textual criada com sucesso!")