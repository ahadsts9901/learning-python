# random joke
import pyjokes
joke = pyjokes.get_joke()
print(joke)

# Fetch and print a single joke from a specific category
category_joke = pyjokes.get_joke(language='en', category='neutral')
print("Category joke :",category_joke)
print(f"category joke : {category_joke}")

# Fetch and print multiple jokes
multiple_jokes = pyjokes.get_jokes()
print("multiple_jokes")

for _joke in multiple_jokes:
    print(_joke)