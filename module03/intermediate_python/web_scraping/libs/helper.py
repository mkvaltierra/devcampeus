import inflection


# Función para filtrar y formatear texto
def formating_text(tags_links):

    for tag_link in tags_links:
        title = tag_link.a.get('href')
        title = title[7:]
        title = title.replace('-', ' ')
        title = inflection.titleize(title)
        print('"' + title + '"')