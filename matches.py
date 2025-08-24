from base.models import Match
from django.utils import timezone
import json
from datetime import datetime

# Public_ids CORRECTOS de Cloudinary
public_ids_correctos = {
    "Córdoba CF": "cordoba-c-f-escudo-actual-desde-marzo-seeklogo_ytjurr",
    "Unión Viera": "CF_Unión_Viera_uhlaue",
    "Málaga": "malaga-football-seeklogo_qtv7ac",
    "CFF Olympia": "olympia-icon-512x512_rroiua",
    "Sporting de Huelva": "sportingclubdehuelva-color-chico-2_a0r4co", 
    "Juan Grande": "juan_ytmlbm",
    "Getafe": "getafe-cf-sad-seeklogo_rlois3",
    "Real Betis B": "beetiss_npkhm7",  # Added
    "Granada B": "granada_nb0vaf",  # Added
    "Cacereño II": "cpc-pantalla-presentacion-128x128_scyrtt",  # Added
    "Pozuelo Alarcón": "Escudo-CF-Pozuelo_jjyhty",  # Added
    "Guiniguada": "guiniguada_glymuh",  # Added
    "Femarguín": "CD-Fermaguin-128x128_mci1f9",  # Added
    "Sport Extremadura": "escudo-12698_hkpzrc",  # Added
}


# Datos de todos los partidos
partidos = [
    # Jornada 1
    {
        'home_team': "Córdoba CF",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Córdoba CF"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 9, 7, 11, 0),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Copa de la Reina
    {
        'home_team': "CFF Olympia", 
        'away_team': "Getafe",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Getafe"],
        'date': datetime(2025, 9, 10),
        'competition': "Copa de la Reina",
        'is_olympia_home': True
    },
    
    # Jornada 2
    {
        'home_team': "CFF Olympia", 
        'away_team': "Málaga",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Málaga"],
        'date': datetime(2025, 9, 14, 17, 0),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 3
    {
        'home_team': "CFF Olympia", 
        'away_team': "Unión Viera",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Unión Viera"],
        'date': datetime(2025, 9, 21, 11, 15),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 4
    {
        'home_team': "Sporting de Huelva",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Sporting de Huelva"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 9, 28),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 5
    {
        'home_team': "CFF Olympia", 
        'away_team': "Juan Grande",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Juan Grande"],
        'date': datetime(2025, 10, 5),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 6
    {
        'home_team': "Real Betis B",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Real Betis B"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 10, 12),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 7
    {
        'home_team': "CFF Olympia", 
        'away_team': "Getafe",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Getafe"],
        'date': datetime(2025, 10, 19),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 8
    {
        'home_team': "Granada B",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Granada B"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 11, 2),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 9
    {
        'home_team': "CFF Olympia", 
        'away_team': "Cacereño II",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Cacereño II"],
        'date': datetime(2025, 11, 9),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 10
    {
        'home_team': "Pozuelo Alarcón",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Pozuelo Alarcón"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 11, 16),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 11
    {
        'home_team': "CFF Olympia", 
        'away_team': "Guiniguada",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Guiniguada"],
        'date': datetime(2025, 11, 23),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 12
    {
        'home_team': "Femarguín",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Femarguín"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2025, 12, 7),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 13
    {
        'home_team': "CFF Olympia", 
        'away_team': "Sport Extremadura",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Sport Extremadura"],
        'date': datetime(2025, 12, 14),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 14
    {
        'home_team': "Juan Grande",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Juan Grande"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 1, 11),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 15
    {
        'home_team': "CFF Olympia", 
        'away_team': "Córdoba CF",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Córdoba CF"],
        'date': datetime(2026, 1, 18),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 16
    {
        'home_team': "CFF Olympia", 
        'away_team': "Real Betis B",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Real Betis B"],
        'date': datetime(2026, 2, 1),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 17
    {
        'home_team': "Unión Viera",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Unión Viera"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 2, 8),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 18
    {
        'home_team': "CFF Olympia", 
        'away_team': "Granada B",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Granada B"],
        'date': datetime(2026, 2, 15),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 19
    {
        'home_team': "Getafe",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Getafe"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 2, 22),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 20
    {
        'home_team': "Málaga",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Málaga"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 3, 8),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 21
    {
        'home_team': "CFF Olympia", 
        'away_team': "Sporting de Huelva",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Sporting de Huelva"],
        'date': datetime(2026, 3, 15),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 22
    {
        'home_team': "Sport Extremadura",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Sport Extremadura"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 3, 22),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 23
    {
        'home_team': "CFF Olympia", 
        'away_team': "Pozuelo Alarcón",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Pozuelo Alarcón"],
        'date': datetime(2026, 3, 29),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 24
    {
        'home_team': "Cacereño II",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Cacereño II"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 4, 12),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
    
    # Jornada 25
    {
        'home_team': "CFF Olympia", 
        'away_team': "Femarguín",
        'home_team_logo': public_ids_correctos["CFF Olympia"],
        'away_team_logo': public_ids_correctos["Femarguín"],
        'date': datetime(2026, 4, 19),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': True
    },
    
    # Jornada 26
    {
        'home_team': "Guiniguada",
        'away_team': "CFF Olympia", 
        'home_team_logo': public_ids_correctos["Guiniguada"],
        'away_team_logo': public_ids_correctos["CFF Olympia"],
        'date': datetime(2026, 4, 26),
        'competition': "Segunda Federación FutFem",
        'is_olympia_home': False
    },
]

# Crear partidos
for partido_data in partidos:
    # Convertir datetime a timezone-aware si es necesario
    if partido_data['date'].tzinfo is None:
        partido_data['date'] = timezone.make_aware(partido_data['date'])
    
    match = Match.objects.create(**partido_data)
    print(f"✅ Creado: {match.home_team} vs {match.away_team} - {match.competition} ")

print("🎉 Todos los partidos creados correctamente")