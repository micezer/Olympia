from django.core.management.base import BaseCommand
from base.models import Match
from datetime import datetime

class Command(BaseCommand):
    help = 'Carga los partidos del CFF Olympia B en la base de datos'

    def handle(self, *args, **options):
        # Public_ids CORRECTOS de Cloudinary para Tercera Federación
        public_ids_tercera = {
            "A.D. SPORTING HORTALEZA \"A\"": "sportingpng_my84ht",
            "A.D. COLMENAR VIEJO \"A\"": "topheader_mxa18z",
            "JUVENTUD SANSE": "topheader_1_cfbzpc",
            "LAS ROZAS C.F. \"A\"": "Escudo-nuevos-Las-Rozas-640x640-2_j8t8ya",
            "A.D. VILLAVICIOSA DE ODON \"A\"": "AD_Villaviciosa_de_Odon_doavur",
            "C.D. GETAFE FEMENINO \"B\"": "escudo_t7p67t",
            "C.F. POZUELO DE ALARCON \"B\"": "Escudo-CF-Pozuelo_jjyhty",
            "MADRID C.F. FEMENINO \"C\"": "madrid_o5t75n",
            "S.A.D. FUNDACION RAYO VALLECANO \"B\"": "Rayo_Vallecano_logo.svg_uduedo",
            "C.D. MASRIVER \"A\"": "CD-Masriver_cf117j",
            "C.D. FUENLABRADA ATLANTIS": "ESC_C.D._FUENLABRADA_ATLANTIS_psyfao",
            "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"": "olympia-icon-512x512_rroiua",
        }



# Datos de todos los partidos del Olympia B
        partidos_olympia_b = [
    # Jornada 1
    {
        'home_team': "C.D. GETAFE FEMENINO \"B\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["C.D. GETAFE FEMENINO \"B\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 9, 21),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 1,
        'location_name': "GETAFE - ALHONDIGA SECTOR III 1",
        'location_address': "Getafe, Madrid"
    },
    
    # Jornada 2
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "A.D. VILLAVICIOSA DE ODON \"A\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["A.D. VILLAVICIOSA DE ODON \"A\""],
        'date': datetime(2025, 9, 28),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 2,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 3
    {
        'home_team': "JUVENTUD SANSE",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["JUVENTUD SANSE"],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 10, 5),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 3,
        'location_name': "S.S. REYES - GABRIEL PEDREGAL 1",
        'location_address': "San Sebastián de los Reyes, Madrid"
    },
    
    # Jornada 4
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "A.D. COLMENAR VIEJO \"A\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["A.D. COLMENAR VIEJO \"A\""],
        'date': datetime(2025, 10, 12),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 4,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 5
    {
        'home_team': "A.D. SPORTING HORTALEZA \"A\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["A.D. SPORTING HORTALEZA \"A\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 10, 19),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 5,
        'location_name': "PVO. MPAL. SPORTING HORTALEZA",
        'location_address': "Hortaleza, Madrid"
    },
    
    # Jornada 6
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "S.A.D. FUNDACION RAYO VALLECANO \"B\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["S.A.D. FUNDACION RAYO VALLECANO \"B\""],
        'date': datetime(2025, 11, 2),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 6,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 7
    {
        'home_team': "C.D. MASRIVER \"A\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["C.D. MASRIVER \"A\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 11, 9),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 7,
        'location_name': "C.D.M. VICENTE DEL BOSQUE",
        'location_address': "Madrid"
    },
    
    # Jornada 8
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "LAS ROZAS C.F. \"A\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["LAS ROZAS C.F. \"A\""],
        'date': datetime(2025, 11, 16),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 8,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 9
    {
        'home_team': "C.D. FUENLABRADA ATLANTIS",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["C.D. FUENLABRADA ATLANTIS"],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 11, 23),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 9,
        'location_name': "FUENLABRADA (Por determinar)",
        'location_address': "Fuenlabrada, Madrid"
    },
    
    # Jornada 10
    {
        'home_team': "C.F. POZUELO DE ALARCON \"B\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["C.F. POZUELO DE ALARCON \"B\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2025, 12, 7),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 10,
        'location_name': "POZUELO - VALLE DE LAS CAÑAS 1",
        'location_address': "Pozuelo de Alarcón, Madrid"
    },
    
    # Jornada 11
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "MADRID C.F. FEMENINO \"C\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["MADRID C.F. FEMENINO \"C\""],
        'date': datetime(2025, 12, 14),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 11,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 12
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "C.D. GETAFE FEMENINO \"B\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["C.D. GETAFE FEMENINO \"B\""],
        'date': datetime(2025, 12, 21),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 12,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 13
    {
        'home_team': "A.D. VILLAVICIOSA DE ODON \"A\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["A.D. VILLAVICIOSA DE ODON \"A\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2026, 1, 11),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 13,
        'location_name': "VILLAVICIOSA DE ODÓN 1",
        'location_address': "Villaviciosa de Odón, Madrid"
    },
    
    # Jornada 14
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "JUVENTUD SANSE",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["JUVENTUD SANSE"],
        'date': datetime(2026, 1, 18),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 14,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 15
    {
        'home_team': "A.D. COLMENAR VIEJO \"A\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["A.D. COLMENAR VIEJO \"A\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2026, 2, 1),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 15,
        'location_name': "COLMENAR VIEJO - ALBERTO RUIZ",
        'location_address': "Colmenar Viejo, Madrid"
    },
    
    # Jornada 16
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "A.D. SPORTING HORTALEZA \"A\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["A.D. SPORTING HORTALEZA \"A\""],
        'date': datetime(2026, 2, 8),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 16,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 17
    {
        'home_team': "S.A.D. FUNDACION RAYO VALLECANO \"B\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["S.A.D. FUNDACION RAYO VALLECANO \"B\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2026, 2, 22),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 17,
        'location_name': "CIUDAD DPTVA. FUND. RAYO VALLECANO 3",
        'location_address': "Madrid"
    },
    
    # Jornada 18
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "C.D. MASRIVER \"A\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["C.D. MASRIVER \"A\""],
        'date': datetime(2026, 3, 8),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 18,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 19
    {
        'home_team': "LAS ROZAS C.F. \"A\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["LAS ROZAS C.F. \"A\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2026, 3, 22),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 19,
        'location_name': "LAS ROZAS - PVO. DEHESA DE NAVALCARBON 1",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 20
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "C.D. FUENLABRADA ATLANTIS",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["C.D. FUENLABRADA ATLANTIS"],
        'date': datetime(2026, 4, 12),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 20,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 21
    {
        'home_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'away_team': "C.F. POZUELO DE ALARCON \"B\"",
        'home_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'away_team_logo': public_ids_tercera["C.F. POZUELO DE ALARCON \"B\""],
        'date': datetime(2026, 4, 19),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': True,
        'team_category': 'senior_b',
        'matchday': 21,
        'location_name': "LAS ROZAS - RECINTO FERIAL",
        'location_address': "Las Rozas, Madrid"
    },
    
    # Jornada 22
    {
        'home_team': "MADRID C.F. FEMENINO \"C\"",
        'away_team': "CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\"",
        'home_team_logo': public_ids_tercera["MADRID C.F. FEMENINO \"C\""],
        'away_team_logo': public_ids_tercera["CDB FUTBOL FEMENINO OLYMPIA LAS ROZAS \"B\""],
        'date': datetime(2026, 4, 26),
        'competition': "Tercera Federación Fútbol Femenino - Grupo 7",
        'is_olympia_home': False,
        'team_category': 'senior_b',
        'matchday': 22,
        'location_name': "CANODROMO",
        'location_address': "Madrid"
    },
]

  # Crear los partidos
        for partido_data in partidos_olympia_b:
            if not Match.objects.filter(
                home_team=partido_data['home_team'],
                away_team=partido_data['away_team'],
                date=partido_data['date']
            ).exists():
                
                match = Match(**partido_data)
                match.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Partido creado: {partido_data['home_team']} vs {partido_data['away_team']} - Jornada {partido_data['matchday']}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Partido ya existe: {partido_data['home_team']} vs {partido_data['away_team']}"
                    )
                )

        self.stdout.write(self.style.SUCCESS('Proceso completado'))