from base.models import Player  # Replace 'your_app' with your actual app name
from django.utils import timezone
from datetime import datetime

# Player data
players_data = [
    # PORTERAS
    {
        'name': 'Andrea',
        'full_name': 'Andrea Rodriguez Castellano',
        'number': 1,
        'position': 'portero',
        'team': 'senior_a',
        'birth_date': datetime(2003, 9, 2),
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # DEFENSAS
    {
        'name': 'A. Totana',
        'full_name': 'A. Totana',
        'number': 18,
        'position': 'defensa',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Elisa',
        'full_name': 'Elisa',
        'number': 19,
        'position': 'defensa',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Gabi',
        'full_name': 'Gabi',
        'number': 12,
        'position': 'defensa',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Laura',
        'full_name': 'Laura',
        'number': 24,
        'position': 'defensa',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # CENTROCAMPISTAS
    {
        'name': 'Gema Prieto',
        'full_name': 'Gema Prieto',
        'number': 6,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Marta Moreno',
        'full_name': 'Marta Moreno',
        'number': 8,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Patri',
        'full_name': 'Patri',
        'number': 7,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Yoli',
        'full_name': 'Yoli',
        'number': 20,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Ana',
        'full_name': 'Ana',
        'number': 0,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Rosita',
        'full_name': 'Rosita',
        'number': 10,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Alfayate',
        'full_name': 'Alfayate',
        'number': 30,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'S. Sánchez',
        'full_name': 'S. Sánchez',
        'number': 17,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'María',
        'full_name': 'María',
        'number': 16,
        'position': 'centrocampista',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # DELANTERAS
    {
        'name': 'Rocio Zafra',
        'full_name': 'Rocio Zafra',
        'number': 9,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'María',
        'full_name': 'María',
        'number': 23,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Rincón',
        'full_name': 'Rincón',
        'number': 0,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Belén',
        'full_name': 'Belén',
        'number': 5,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Albita',
        'full_name': 'Albita',
        'number': 22,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'L. Viñas',
        'full_name': 'L. Viñas',
        'number': 0,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Lucía.S',
        'full_name': 'Lucía.S',
        'number': 24,
        'position': 'delantero',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # CUERPO TÉCNICO
    {
        'name': 'Fernando Zuazua Escalada',
        'full_name': 'Fernando Zuazua Escalada',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Entrenador'
    },
    {
        'name': 'Borja Carrera González',
        'full_name': 'Borja Carrera González',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Segundo Entrenador'
    },
    {
        'name': 'Rodrigo Colado',
        'full_name': 'Rodrigo Colado',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Preparador Físico'
    },
    {
        'name': 'Maru Monte',
        'full_name': 'Maru Monte',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Fisioterapeuta'
    },
    {
        'name': 'Alejandro Fernández',
        'full_name': 'Alejandro Fernández',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Psicólogo'
    },
    {
        'name': 'Sergio De Lucas Fernandez',
        'full_name': 'Sergio De Lucas Fernandez',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Encargado de Material'
    },
    {
        'name': 'Adrian Sanchez Lopez',
        'full_name': 'Adrian Sanchez Lopez',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Analista'
    },
    {
        'name': 'DELEGADO',
        'full_name': 'DELEGADO',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_a',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Delegado'
    },
]

# Create players
for player_data in players_data:
    # Convert datetime to timezone-aware if needed
    if player_data['birth_date'] and player_data['birth_date'].tzinfo is None:
        player_data['birth_date'] = timezone.make_aware(player_data['birth_date'])
    
    player = Player.objects.create(**player_data)
    print(f"✅ Creado: {player.name} - {player.get_position_display()} - {player.get_team_display()}")

print("🎉 Todos los jugadores y cuerpo técnico creados correctamente")