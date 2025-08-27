# management/commands/update_player_images.py
from django.core.management.base import BaseCommand
from base.models import Player
from cloudinary import uploader


class Command(BaseCommand):
    help = 'Asigna imágenes de Cloudinary a las jugadoras'

    def handle(self, *args, **options):
        # Mapeo de nombres de jugadoras a public_ids de Cloudinary
        player_public_ids = {
            # PORTERAS SENIOR A
            "Andrea Rodriguez": "andrea_rodriguez_nucjaq",
            "Laura Zaballos": "laurazaballos_gqv9be",

            # DEFENSAS SENIOR A
            "Andrea Totana": "andra_totana_qyihmn",
            "Elisa Puerta": "elisa_puerta_qxgppy",
            "Laura González": "laura_gonzalez_pmustm",

            # CENTROCAMPISTAS SENIOR A
            "Gema Prieto": "gema_prieto_nermsd",
            "Yolanda Albalat": "yoanda_albalat_hrosej",
            "Ana Hortelano": "ana_hortelano_t4tkxq",
            "Ainara Mauri": "ainara_mauri_dorczd",
            "Manuela Alfayate": "manuela_alfayete_siqbfj",
            "Sara Sánchez": "sara_sanchez_lnpxqg",
            "Maria Herrero": "mariaherrero_hewosr",

            # DELANTERAS SENIOR A
            "Rocio Zafra": "rociozafra_cnqvvw",
            "María Bravo": "maria_bravo_d97cza",
            "Cristina Rincón": "cristina_rincon_wprer9",
            "Belén Peralta": "belen_peralta_jpi0sq",
            "Alba Masa": "alba_masa_dyzdbp",
            "Laura Viñas": "lauravinas_njlphi",
            "Lucía Sanchez": "lucia_sanchez_vb0vxm",

            # PORTERAS SENIOR B
            "Carmen": "carmen_porteria_senior_b",
            "L. Martín": "l_martin_porteria_senior_b",
            
            # DEFENSAS SENIOR B
            "Nuria": "nuria_defensa_senior_b",
            "Lucía": "lucia_defensa_senior_b",
            "Daniela": "daniela_defensa_senior_b",
            "Andrea": "andrea_rodriguez_nucjaq",
            "Paola": "paola_defensa_senior_b",
            "Mireya": "mireya_defensa_senior_b",
            "Cristina": "cristina_defensa_senior_b",
            "Gadea": "gadea_defensa_senior_b",
            "Bea": "bea_defensa_senior_b",
            "Teresa": "teresa_defensa_senior_b",
            "Ana": "ana_defensa_senior_b",
            
            # CENTROCAMPISTAS SENIOR B
            "L. Fernández": "l_fernandez_centro_senior_b",
            "Raquel": "raquel_centro_senior_b",
            "Marina": "marina_centro_senior_b",
            "Aroa": "aroa_centro_senior_b",
            "Iciar": "iciar_centro_senior_b",
            "Lorena": "lorena_centro_senior_b",
            "Susana": "susana_centro_senior_b",
            "Mirem": "mirem_centro_senior_b",
            
            # DELANTERAS SENIOR B
            "Alejandra": "alejandra_delantero_senior_b",
            "Claudia": "claudia_delantero_senior_b",
            "Lucía": "lucia_delantero_senior_b",
            "Clara": "clara_delantero_senior_b",
            "Victoria": "victoria_delantero_senior_b",
            
            # CUERPO TÉCNICO
            "Fernando Zuazua Escalada": "fernando_entrenador_senior_a",
            "Borja Carrera González": "borja_entrenador_senior_a",
            "Rodrigo Colado": "rodrigo_preparador_senior_a",
            "Maru Monte": "maru_fisio_senior_a",
            "Alejandro Fernández": "alejandro_psicologo_senior_a",
            "Sergio De Lucas Fernandez": "sergio_material_senior_a",
            "Adrian Sanchez Lopez": "adrian_analista_senior_a",
            "DELEGADO": "delegado_senior_a",
            "Ana Belén De La Chica Cardenas": "ana_belen_entrenador_senior_b",
            "Jose Pulido García": "jose_entrenador_senior_b",
        }

        self.stdout.write("Iniciando asignación de imágenes de jugadoras...")
        
        updated_count = 0
        missing_count = 0
        
        for player_name, public_id in player_public_ids.items():
            try:
                # Buscar jugadora por nombre
                players = Player.objects.filter(name=player_name)
                
                if not players.exists():
                    self.stdout.write(
                        self.style.WARNING(f"⚠️  Jugadora no encontrada: {player_name}")
                    )
                    missing_count += 1
                    continue
                
                # Verificar si la imagen existe en Cloudinary
                try:
                    result = uploader.explicit(public_id, type="upload")
                    
                    # Actualizar todas las jugadoras con ese nombre
                    for player in players:
                        player.image = public_id  # CloudinaryField usa el public_id directamente
                        player.save()
                    
                    self.stdout.write(
                        self.style.SUCCESS(f"✅ Imagen asignada: {player_name} -> {public_id}")
                    )
                    updated_count += 1
                    
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f"❌ Imagen no encontrada en Cloudinary: {public_id} - {str(e)}")
                    )
                    missing_count += 1
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"❌ Error procesando {player_name}: {str(e)}")
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f"🎉 Proceso completado. {updated_count} imágenes asignadas, {missing_count} no encontradas"
            )
        )