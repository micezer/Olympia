# management/commands/update_player_images.py
from django.core.management.base import BaseCommand
from base.models import Player  # Ajusta según tu app
from cloudinary import uploader
import os

class Command(BaseCommand):
    help = 'Actualiza las imágenes de las jugadoras desde Cloudinary usando CloudinaryField'

    def handle(self, *args, **options):
        # Public_ids de Cloudinary para las jugadoras (sin la versión)
        public_ids_jugadoras = {
            # PORTERAS SENIOR A
            "Andrea": "andrea_rodriguez_jdxwky",
            
            # DEFENSAS SENIOR A
            "A. Totana": "a_totana_defensa",
            "Elisa": "elisa_defensa",
            "Gabi": "gabi_defensa",
            "Laura": "laura_defensa",
            
            # CENTROCAMPISTAS SENIOR A
            "Gema Prieto": "gema_prieto",
            "Marta Moreno": "marta_moreno",
            "Patri": "patri_centro",
            "Yoli": "yoli_centro",
            "Ana": "ana_centro",
            "Rosita": "rosita_centro",
            "Alfayate": "alfayate_centro",
            "S. Sánchez": "s_sanchez_centro",
            "María": "maria_centro",
            
            # DELANTERAS SENIOR A
            "Rocio Zafra": "rocio_zafra",
            "María": "maria_delantero",
            "Rincón": "rincon_delantero",
            "Belén": "belen_delantero",
            "Albita": "albita_delantero",
            "L. Viñas": "l_vinas_delantero",
            "Lucía.S": "lucia_s_delantero",
            
            # PORTERAS SENIOR B
            "Carmen": "carmen_porteria_b",
            "L. Martín": "l_martin_porteria_b",
            
            # DEFENSAS SENIOR B
            "Nuria": "nuria_defensa_b",
            "Lucía": "lucia_defensa_b",
            "Daniela": "daniela_defensa_b",
            "Andrea": "andrea_defensa_b",
            "Paola": "paola_defensa_b",
            "Mireya": "mireya_defensa_b",
            "Cristina": "cristina_defensa_b",
            "Gadea": "gadea_defensa_b",
            "Bea": "bea_defensa_b",
            "Teresa": "teresa_defensa_b",
            "Ana": "ana_defensa_b",
            
            # CENTROCAMPISTAS SENIOR B
            "L. Fernández": "l_fernandez_centro_b",
            "Raquel": "raquel_centro_b",
            "Marina": "marina_centro_b",
            "Aroa": "aroa_centro_b",
            "Iciar": "iciar_centro_b",
            "Lorena": "lorena_centro_b",
            "Susana": "susana_centro_b",
            "Mirem": "mirem_centro_b",
            
            # DELANTERAS SENIOR B
            "Alejandra": "alejandra_delantero_b",
            "Claudia": "claudia_delantero_b",
            "Lucía": "lucia_delantero_b",
            "Clara": "clara_delantero_b",
            "Victoria": "victoria_delantero_b",
            
            # CUERPO TÉCNICO
            "Fernando Zuazua Escalada": "fernando_entrenador",
            "Borja Carrera González": "borja_entrenador",
            "Rodrigo Colado": "rodrigo_preparador",
            "Maru Monte": "maru_fisio",
            "Alejandro Fernández": "alejandro_psicologo",
            "Sergio De Lucas Fernandez": "sergio_material",
            "Adrian Sanchez Lopez": "adrian_analista",
            "DELEGADO": "delegado",
            "Ana Belén De La Chica Cardenas": "ana_belen_entrenador_b",
            "Jose Pulido García": "jose_entrenador_b",
        }

        self.stdout.write("Iniciando actualización de imágenes de jugadoras...")
        
        # Actualizar todas las jugadoras
        all_players = Player.objects.all()
        self.stdout.write(f"Encontradas {all_players.count()} jugadoras en total")
        
        updated_count = 0
        for player in all_players:
            if player.name in public_ids_jugadoras:
                public_id = public_ids_jugadoras[player.name]
                
                # Construir la ruta completa con la carpeta 'jugadoras'
                full_public_id = f"jugadoras/{public_id}"
                
                try:
                    # Verificar si la imagen existe en Cloudinary
                    result = uploader.explicit(full_public_id, type="upload")
                    
                    # Actualizar el campo CloudinaryField con el public_id
                    player.image = full_public_id
                    player.save()
                    
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"✅ Imagen actualizada para {player.name}: {full_public_id}"
                        )
                    )
                    updated_count += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(
                            f"❌ Error al cargar imagen para {player.name}: {str(e)}"
                        )
                    )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"⚠️  No se encontró public_id para: {player.name}"
                    )
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Proceso completado. {updated_count} imágenes actualizadas correctamente"
            )
        )