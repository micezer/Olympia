from base.models import Match

logos = {
    "CFF Olympia": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040406/olympia-icon-512x512_rroiua.png",
    "Sporting de Huelva": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040406/sportingclubdehuelva-color-chico-2_a0r4co.png",
    "Málaga": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040405/malaga-football-seeklogo_qtv7ac.png",
    "Córdoba CF": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040399/cordoba-c-f-escudo-actual-desde-marzo-seeklogo_ytjurr.png",
    "Unión Viera": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040399/CF_Uni%C3%BAn_Viera_uhlaue.png",
    "Juan Grande": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040404/juan_ytmlbm.png",
    "Getafe": "https://res.cloudinary.com/do0mj4z8k/image/upload/v1756040402/getafe-cf-sad-seeklogo_rlois3.png",
}

for match in Match.objects.all():
    updated = False

    if match.home_team in logos:
        match.home_team_logo = logos[match.home_team]
        updated = True

    if match.away_team in logos:
        match.away_team_logo = logos[match.away_team]
        updated = True

    if updated:
        match.save()
        print(f"✅ Actualizado: {match.home_team} vs {match.away_team}")

print("🎉 Todos los partidos procesados")
