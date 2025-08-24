from base.models import Match

# Diccionario con los public_id CORRECTOS de Cloudinary
public_ids_correctos = {
    "Córdoba CF": "sportingclubdehuelva-color-chico-2_a0r4co",
    "CFF Olympia": "olympia-icon-512x512_rroiua", 
    "Sporting de Huelva": "sportingclubdehuelva-color-chico-2_a0r4co",
    "Málaga": "malaga-football-seeklogo_qtv7ac",
    "Unión Viera": "CF_Uni%C3%B3n_Viera_uhlaue",
    "Juan Grande": "juan_ytmlbm",
    "Getafe": "getafe-cf-sad-seeklogo_rlois3",
}

print("=== CORRIGIENDO TODOS LOS ESCUDOS ===")

for match in Match.objects.all():
    updated = False
    
    # Corregir equipo local
    if match.home_team in public_ids_correctos:
        public_id_correcto = public_ids_correctos[match.home_team]
        if match.home_team_logo != public_id_correcto:
            print(f"Corrigiendo {match.home_team}: {match.home_team_logo} → {public_id_correcto}")
            match.home_team_logo = public_id_correcto
            updated = True
    
    # Corregir equipo visitante
    if match.away_team in public_ids_correctos:
        public_id_correcto = public_ids_correctos[match.away_team]
        if match.away_team_logo != public_id_correcto:
            print(f"Corrigiendo {match.away_team}: {match.away_team_logo} → {public_id_correcto}")
            match.away_team_logo = public_id_correcto
            updated = True
    
    if updated:
        match.save()

print("✅ Corrección completada")

# Verificar
print("\n=== VERIFICACIÓN FINAL ===")
for match in Match.objects.all():
    print(f"\n{match.home_team} vs {match.away_team}")
    print(f"Home: {match.home_team_logo} → {match.home_team_logo.url}")
    print(f"Away: {match.away_team_logo} → {match.away_team_logo.url}")