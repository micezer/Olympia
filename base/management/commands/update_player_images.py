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
            "Andrea Rodriguez": "andrea_rodriguez_r6g6ew",
            "Laura Zaballos": "laura_zaballos_jynhsk",

            # DEFENSAS SENIOR A
            "Andrea Totana": "andrea_totana_h2mrkp",
            "Elisa Puerta": "elisa_puerta_wlwlgr",
            "Laura González": "laura_gonzalez_gv0zdu",
            "Tamara Álvarez": "tamara_alvarez_sq0pfo",

            # CENTROCAMPISTAS SENIOR A
            "Gema Prieto": "gema_prieto_lwivsj",
            "Yolanda Albalat": "yolanda_albalat_tarbys",
            "Ana Hortelano": "ana_hortelano_q7l88x",
            "Ainara Mauri": "ainara_mauri_t6mael",
            "Manuela Alfayate": "manuela_alfayate_yipcnf",
            "Sara Sánchez": "",
            "Maria Herrero": "maria_herrero_mpn4qv",

            # DELANTERAS SENIOR A
            "Rocio Zafra": "rocio_zafra_rtxkdl",
            "María Bravo": "maria_bravo_dzhgy9",
            "Cristina Rincón": "cristina_rincon_sp0nnp",
            "Belén Peralta": "belen_peralta_m4dghu",
            "Alba Masa": "alba_masa_ecjnwj",
            "Laura Viñas": "laura_vinas_tlo8ph",
            "Lucía Sanchez": "lucia_sanchez_zu9047",


            # PORTERAS SENIOR B
            "Carmen Sánchez": "carmen_sanchez-Photoroom_claoo4",
            "Lucía Martín": "lucia_martin-Photoroom_pzaip0",

            # DEFENSAS SENIOR B
            "Nuria Díaz": "nuria_diaz-Photoroom_vn6yso",
            "Lucía Adán": "lucia_adan-Photoroom_vvkdhs",
            "Andrea Ovejero": "andrea_ovejero-Photoroom_nbzu8x",
            "Lorena Fernández": "lorena_fernandez-Photoroom_km7nbr",
            "Paola González": "paola_gonzalez-Photoroom_ypisxt",
            "Mireya Nieto": "mireya_nieto-Photoroom_an7pkg",
            "Cristina Tejada": "cristina_tejada-Photoroom_ugefg7",
            "Marina Valmorisco": "marina_valmorisco-Photoroom_wnfskv",
            "Teresa Brandau": "",
            "Sarah Yagüe": "sarahyague-Photoroom_jda5pv",


            # CENTROCAMPISTAS SENIOR B
            "Lucía Fernández": "lucia_fernandez-Photoroom_lhi5uc",
            "Raquel Guardado": "raquel_guardado-Photoroom_zfdbqb",
            "Aroa González": "aroa_gonzalez-Photoroom_ydxm07",
            "Iciar Cofrades": "iciar_cofrades-Photoroom_a2ehsx",
            "Clara Gómez": "clara_gomez-Photoroom_xr0ass",
            "Vicky Pérez": "vicky_perez-Photoroom_xtnb1z",
            "Bea Asenjo": "bea_asenjo-Photoroom_fz9txe",
            
            # DELANTERAS SENIOR B
            "Daniela Sanchís": "daniela__sanchis-Photoroom_sbzrvg",
            "Claudia Hernando": "claudia_hernando-Photoroom_c01hya",
            "Lucía Nuñez": "lucia_nunez-Photoroom_awwnfh",
            "Clara Fajardo": "clara_fajardo-Photoroom_dqjd7e",
            "Iratxe Rodríguez": "iratxe_rodriguez-Photoroom_vss7xx",
            
            # CUERPO TÉCNICO
            "Abiel Ojeda": "abiel_ojeda-Photoroom_wykhl3",
            "Alba Mateos": "alba_mateos-Photoroom_clcz6p",
            "Arantxa De La Chica": "arantxa_de_la_chica-Photoroom_bwf2ru",
            "Emanuel Inga": "emanuel_inga_vbazk5",
            "Lucía Sánchez": "lucia_sanchez-Photoroom_w9e9si",
        }



        self.stdout.write("Iniciando asignación de imágenFes de jugadoras...")
        
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



