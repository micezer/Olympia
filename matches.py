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
    "Getafe": "escudo_t7p67t",
    "Real Betis B": "beetiss_npkhm7",
    "Granada B": "granada_nb0vaf",
    "Cacereño II": "cpc-pantalla-presentacion-128x128_scyrtt",
    "Pozuelo Alarcón": "Escudo-CF-Pozuelo_jjyhty",
    "Guiniguada": "guiniguada_glymuh",
    "Femarguín": "CD-Fermaguin-128x128_mci1f9",
    "Sport Extremadura": "escudo-12698_hkpzrc",
}

# Actualizar logos de los partidos existentes
for match in Match.objects.all():
    # Actualizar logo del equipo local si existe en el diccionario
    if match.home_team in public_ids_correctos:
        match.home_team_logo = public_ids_correctos[match.home_team]
    
    # Actualizar logo del equipo visitante si existe en el diccionario
    if match.away_team in public_ids_correctos:
        match.away_team_logo = public_ids_correctos[match.away_team]
    
    # Guardar los cambios
    match.save()
    print(f"✅ Actualizado: {match.home_team} vs {match.away_team} - Logos actualizados")

print("🎉 Todos los logos de partidos actualizados correctamente")