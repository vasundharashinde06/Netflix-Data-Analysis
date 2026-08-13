import pandas as pd
import matplotlib.pyplot as plt
import os

# Create images folder if it doesn't exist
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_csv("dataset/netflix_titles.csv")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())
# Question 1
# Which country produces the most content?
country = (
    df["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

country_count = country.value_counts().head(10)

print("\nTop 10 Countries:")
print(country_count)

plt.figure(figsize=(10,5))
country_count.plot(kind="bar")
plt.title("Top 10 Content Producing Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/country.png")
plt.show()
# Question 2
# Movie vs TV Show Distribution
type_count = df["type"].value_counts()

print("\nMovie vs TV Show:")
print(type_count)

plt.figure(figsize=(6,6))
type_count.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Movie vs TV Show Distribution")
plt.savefig("images/movie_tv.png")
plt.show()
# Question 3
# Most Common Genres
genres = (
    df["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

genre_count = genres.value_counts().head(10)

print("\nTop Genres:")
print(genre_count)

plt.figure(figsize=(8,5))
genre_count.plot(kind="barh")
plt.title("Top 10 Genres")
plt.tight_layout()
plt.savefig("images/genres.png")
plt.show()
# Question 4
# Content Added Over Years
yearly = df["year_added"].value_counts().sort_index()

print("\nContent Added Over Years:")
print(yearly)

plt.figure(figsize=(10,5))
yearly.plot(marker="o")
plt.title("Content Added Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True)
plt.tight_layout()
plt.savefig("images/yearly_addition.png")
plt.show()
# Question 5
# Ratings Distribution
rating_count = df["rating"].value_counts()

print("\nRatings Distribution:")
print(rating_count)

plt.figure(figsize=(10,5))
rating_count.plot(kind="bar")
plt.title("Ratings Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/ratings.png")
plt.show()

print("\nAnalysis Completed Successfully!")
