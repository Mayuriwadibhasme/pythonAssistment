import pandas as pd

df = pd.read_csv("books.csv")

print("Complete Report of Books:\n")
print(df.to_string(index=False))

author = input("\nEnter the author's name: ")
books_by_author = df[df['author'].str.lower() == author.lower()]
print(f"\nBooks by {author}:\n")
print(books_by_author[['title', 'edition', 'publication_year', 'publishing_house', 'price']].to_string(index=False))

publishing_house = input("\nEnter the publishing house: ")
books_by_house = df[df['publishing_house'].str.lower() == publishing_house.lower()]
print(f"\nBooks published by {publishing_house}:\n")
print(books_by_house[['title', 'author', 'edition', 'publication_year', 'price']].to_string(index=False))

cheapest_book = df.loc[df['price'].idxmin()]
costliest_book = df.loc[df['price'].idxmax()]
print(f"\nCheapest Book: {cheapest_book['title']} (Price: {cheapest_book['price']})")
print(f"Costliest Book: {costliest_book['title']} (Price: {costliest_book['price']})")

sorted_books = df.sort_values(by='publication_year')
print("\nBooks sorted by Year of Publication:\n")
print(sorted_books[['title', 'author', 'edition', 'publication_year', 'publishing_house', 'price']].to_string(index=False))
