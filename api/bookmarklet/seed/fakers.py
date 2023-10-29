import json
from faker import Faker

fake = Faker()

root = ""
app = "bookmarklet"

filename_bookmark_groups = root + "faker-bookmark-groups.json"
filename_bookmark_tags = root + "faker-bookmark-tags.json"
filename_bookmarks = root + "faker-bookmarks.json"

len_bookmark_groups = 25
len_bookmark_tags = 40
len_bookmarks = 100



# Crear y guarda en un json los datos ficticios para grupos de marcadores
bookmark_groups = []
for _ in range(len_bookmark_groups): 
    group = {
        "model": app + ".bookmarkgroup",
        "pk": None,
        "fields": {
            "name": fake.word(),
            "icon": fake.word()
        }
    }
    bookmark_groups.append(group)

with open(filename_bookmark_groups, "w") as json_file:
    json.dump(bookmark_groups, json_file, indent=4)


#  Crear y guarda en un json los datos ficticios para etiquetas de marcadores 
bookmark_tags = []
for _ in range(len_bookmark_tags):  
    tag = {
        "model": app + ".bookmarktag",
        "pk": None,
        "fields": {
            "name": fake.word(),
            "icon": fake.word()
        }
    }
    bookmark_tags.append(tag)

with open(filename_bookmark_tags, "w") as json_file:
    json.dump(bookmark_tags, json_file, indent=4)


# Obtén IDs de grupos y etiquetas ficticias generadas anteriormente
group_ids = list(range(1, len(bookmark_groups) + 1))
tag_ids = list(range(1, len(bookmark_tags) + 1))

# Crear y guarda en un json los datos ficticios para marcadores relacionados con grupos y etiquetas
bookmarks = []
for _ in range(len_bookmarks):
    bookmark = {
        "model": app + ".bookmark",
        "pk": None,
        "fields": {
            "name": fake.catch_phrase(),
            "url": fake.url(),
            "description": fake.paragraph(),
            "group": fake.random_element(group_ids),
            "tag": fake.random_element(tag_ids)
        }
    }
    bookmarks.append(bookmark)

with open(filename_bookmarks, "w") as json_file:
    json.dump(bookmarks, json_file, indent=4)
