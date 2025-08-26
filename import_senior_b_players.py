from base.models import Player  # Replace 'your_app' with your actual app name
from django.utils import timezone
from datetime import datetime

# Senior B player data
senior_b_players = [
    # ENTRENADOR
    {
        'name': 'Ana Belén De La Chica Cardenas',
        'full_name': 'Ana Belén De La Chica Cardenas',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Entrenador'
    },
    
    # PORTERAS
    {
        'name': 'Carmen',
        'full_name': 'Carmen',
        'number': 1,
        'position': 'portero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'L. Martín',
        'full_name': 'L. Martín',
        'number': 25,
        'position': 'portero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # DEFENSAS
    {
        'name': 'Nuria',
        'full_name': 'Nuria',
        'number': 28,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Lucía',
        'full_name': 'Lucía',
        'number': 3,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Daniela',
        'full_name': 'Daniela',
        'number': 7,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Andrea',
        'full_name': 'Andrea',
        'number': 2,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Paola',
        'full_name': 'Paola',
        'number': 22,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Mireya',
        'full_name': 'Mireya',
        'number': 4,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Cristina',
        'full_name': 'Cristina',
        'number': 14,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Gadea',
        'full_name': 'Gadea',
        'number': 31,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Bea',
        'full_name': 'Bea',
        'number': 33,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Teresa',
        'full_name': 'Teresa',
        'number': 32,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Ana',
        'full_name': 'Ana',
        'number': 51,
        'position': 'defensa',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # CENTROCAMPISTAS
    {
        'name': 'L. Fernández',
        'full_name': 'L. Fernández',
        'number': 7,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Raquel',
        'full_name': 'Raquel',
        'number': 10,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Marina',
        'full_name': 'Marina',
        'number': 23,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Aroa',
        'full_name': 'Aroa',
        'number': 18,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Iciar',
        'full_name': 'Iciar',
        'number': 20,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Lorena',
        'full_name': 'Lorena',
        'number': 6,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Susana',
        'full_name': 'Susana',
        'number': 26,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Mirem',
        'full_name': 'Mirem',
        'number': 88,
        'position': 'centrocampista',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # DELANTERAS
    {
        'name': 'Alejandra',
        'full_name': 'Alejandra',
        'number': 11,
        'position': 'delantero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Claudia',
        'full_name': 'Claudia',
        'number': 9,
        'position': 'delantero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Lucía',
        'full_name': 'Lucía',
        'number': 19,
        'position': 'delantero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Clara',
        'full_name': 'Clara',
        'number': 24,
        'position': 'delantero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    {
        'name': 'Victoria',
        'full_name': 'Victoria',
        'number': 29,
        'position': 'delantero',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': False,
        'role': ''
    },
    
    # CUERPO TÉCNICO
    {
        'name': 'Jose Pulido García',
        'full_name': 'Jose Pulido García',
        'number': 0,
        'position': 'tecnico',
        'team': 'senior_b',
        'birth_date': None,
        'nationality': 'Española',
        'is_staff': True,
        'role': 'Segundo Entrenador'
    },
]

# Create players
for player_data in senior_b_players:
    # Convert datetime to timezone-aware if needed
    if player_data['birth_date'] and player_data['birth_date'].tzinfo is None:
        player_data['birth_date'] = timezone.make_aware(player_data['birth_date'])
    
    player = Player.objects.create(**player_data)
    print(f"✅ Creado: {player.name} - {player.get_position_display()} - {player.get_team_display()}")

print("🎉 Todos los jugadores y cuerpo técnico del Senior B creados correctamente")