favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")


# Looping Through All Key-Value Pairs
favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping Through All the Keys in a Dictionary
favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
for name in favorite_languages.keys():  # same for name in favorite_languages
    print(name.title())

# linked with language favorite
friends = ["phil", "sarah"]
print("\n")
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# returns a list of all the keys
favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
if "erin" not in favorite_languages.keys():
    print("\nErin, please take our poll!")

# sorting Looping Through a Dictionary’s Keys in a Particular Order

favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.\n")

# Looping Through All Values in a Dictionary
favorite_languages = {"jen": "python", "sarah": "c", "edward": "ruby", "phil": "python"}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# cek duplikat dengan set
print("\n   The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


print("\n\n")
# list on dictionary
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")
