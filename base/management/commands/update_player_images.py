# management/commands/update_player_images.py
from django.core.management.base import BaseCommand
from base.models import Player

class Command(BaseCommand):
    help = 'Actualiza las imágenes de las jugadoras desde Cloudinary'

    def handle(self, *args, **options):
        # Copia aquí el contenido de la función update_player_images()
        # del script anterior, pero sin la parte del if __name__
        
        print("Iniciando actualización de imágenes de jugadoras...")
        
        # Public_ids de Cloudinary (copia el diccionario aquí)
        public_ids_jugadoras = {
    # PORTERAS
    "Andrea": "andrea_rodriguez_jdxwky",
    "Carmen": "carmen_porteria_senior_b",
    "L. Martín": "l_martin_porteria_senior_b",
    
    # DEFENSAS SENIOR A
    "A. Totana": "a_totana_defensa_senior_a",
    "Elisa": "elisa_defensa_senior_a",
    "Gabi": "gabi_defensa_senior_a",
    "Laura": "laura_defensa_senior_a",
    
    # DEFENSAS SENIOR B
    "Nuria": "nuria_defensa_senior_b",
    "Lucía": "lucia_defensa_senior_b",
    "Daniela": "daniela_defensa_senior_b",
    "Andrea": "andrea_defensa_senior_b",
    "Paola": "paola_defensa_senior_b",
    "Mireya": "mireya_defensa_senior_b",
    "Cristina": "cristina_defensa_senior_b",
    "Gadea": "gadea_defensa_senior_b",
    "Bea": "bea_defensa_senior_b",
    "Teresa": "teresa_defensa_senior_b",
    "Ana": "ana_defensa_senior_b",
    
    # CENTROCAMPISTAS SENIOR A
    "Gema Prieto": "gema_prieto_centro_senior_a",
    "Marta Moreno": "marta_moreno_centro_senior_a",
    "Patri": "patri_centro_senior_a",
    "Yoli": "yoli_centro_senior_a",
    "Ana": "ana_centro_senior_a",
    "Rosita": "rosita_centro_senior_a",
    "Alfayate": "alfayate_centro_senior_a",
    "S. Sánchez": "s_sanchez_centro_senior_a",
    "María": "maria_centro_senior_a",
    
    # CENTROCAMPISTAS SENIOR B
    "L. Fernández": "l_fernandez_centro_senior_b",
    "Raquel": "raquel_centro_senior_b",
    "Marina": "marina_centro_senior_b",
    "Aroa": "aroa_centro_senior_b",
    "Iciar": "iciar_centro_senior_b",
    "Lorena": "lorena_centro_senior_b",
    "Susana": "susana_centro_senior_b",
    "Mirem": "mirem_centro_senior_b",
    
    # DELANTERAS SENIOR A
    "Rocio Zafra": "rocio_zafra_delantero_senior_a",
    "María": "maria_delantero_senior_a",
    "Rincón": "rincon_delantero_senior_a",
    "Belén": "belen_delantero_senior_a",
    "Albita": "albita_delantero_senior_a",
    "L. Viñas": "l_vinas_delantero_senior_a",
    "Lucía.S": "lucia_s_delantero_senior_a",
    
    # DELANTERAS SENIOR B
    "Alejandra": "alejandra_delantero_senior_b",
    "Claudia": "claudia_delantero_senior_b",
    "Lucía": "lucia_delantero_senior_b",
    "Clara": "clara_delantero_senior_b",
    "Victoria": "victoria_delantero_senior_b",
    
    # CUERPO TÉCNICO SENIOR A
    "Fernando Zuazua Escalada": "fernando_zuazua_tecnico_senior_a",
    "Borja Carrera González": "borja_carrera_tecnico_senior_a",
    "Rodrigo Colado": "rodrigo_colado_tecnico_senior_a",
    "Maru Monte": "maru_monte_tecnico_senior_a",
    "Alejandro Fernández": "alejandro_fernandez_tecnico_senior_a",
    "Sergio De Lucas Fernandez": "sergio_de_lucas_tecnico_senior_a",
    "Adrian Sanchez Lopez": "adrian_sanchez_tecnico_senior_a",
    "DELEGADO": "delegado_tecnico_senior_a",
    
    # CUERPO TÉCNICO SENIOR B
    "Ana Belén De La Chica Cardenas": "ana_belen_tecnico_senior_b",
    "Jose Pulido García": "jose_pulido_tecnico_senior_b",
}
        
        # Función para construir URL
        def build_cloudinary_url(public_id):
            return f"https://res.cloudinary.com/tu_cloud_name/image/upload/{public_id}.jpg"
        
        # Resto del código de actualización...
        # Primero, actualizar jugadoras del Senior A
        senior_a_players = Player.objects.filter(team='senior_a')
        print(f"Encontradas {senior_a_players.count()} jugadoras en Senior A")
        
        for player in senior_a_players:
            if player.name in public_ids_jugadoras:
                public_id = public_ids_jugadoras[player.name]
                player.image = build_cloudinary_url(public_id)
                player.save()
                print(f"✅ Imagen actualizada para {player.name} ({player.get_position_display()}) - Senior A")
            else:
                print(f"⚠️  No se encontró public_id para {player.name} en Senior A")
        
        # Luego, actualizar jugadoras del Senior B
        senior_b_players = Player.objects.filter(team='senior_b')
        print(f"Encontradas {senior_b_players.count()} jugadoras en Senior B")
        
        for player in senior_b_players:
            if player.name in public_ids_jugadoras:
                public_id = public_ids_jugadoras[player.name]
                player.image = build_cloudinary_url(public_id)
                player.save()
                print(f"✅ Imagen actualizada para {player.name} ({player.get_position_display()}) - Senior B")
            else:
                print(f"⚠️  No se encontró public_id para {player.name} en Senior B")
        
        print("🎉 Proceso de actualización de imágenes completado")