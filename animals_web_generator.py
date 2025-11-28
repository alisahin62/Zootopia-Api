import data_fetcher

def serialize_animal(animal):
    """Serialize a single animal dict into HTML card with name, diet, location and optional type."""
    output = ""
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    type = animal["characteristics"].get("type")
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{name}</div>\n'
    output += '<p class="card__text">'
    output += f"<strong>Diet:</strong> {diet}<br/>\n"
    output += f"<strong>Location:</strong> {location}<br/>\n"
    if type:
        output += f"<strong>Type:</strong> {type}<br/>\n"
    output += "\n"
    output += " </p>"
    output += '</li>'
    return output

animal_name = input("Enter a name of an animal: ")
animals_data = data_fetcher.fetch_data(animal_name)

with open("animals_template.html", "r") as file:
    html_page = file.read()

output = ""
for animal in animals_data:
    output += serialize_animal(animal)


new_html = html_page.replace("__REPLACE_ANIMALS_INFO__", output)

with open("animals.html", "w", encoding="utf-8") as f:
    f.write(new_html)