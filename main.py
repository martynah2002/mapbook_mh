users:list[dict] = [
    {'name': 'Martyna', 'location': 'Zamość', 'posts': 500, },
    {'name': 'Kinga', 'location': 'Kozienice', 'posts': 470, },
    {'name': 'Wiktoria', 'location': 'Radzyń', 'posts': 150, }
]

for user in users:
    print(f'Twój znajomy: {user["name"]} z miejscowości: {user["location"]} opublikował: {user["posts"]} postów.')
