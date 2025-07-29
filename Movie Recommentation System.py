#Movie recommendation system
class Movie():
    def __init__(self,title,genre,rating):
        self.title = title
        self.genre = genre
        self.rating = rating
    def __str__(self):
        print("-------------------------------------------------")
        return f"{self.title} ({self.genre}) --> ({self.rating})/10"
class User():
    def __init__(self,name,liked_genre):
        self.name = name
        self.liked_genre = liked_genre
    def __str__(self):
        print("============================================================")
        return f"User Name:{self.name} || Likes :{",".join(self.liked_genre)}"

class Recommender():
    def __init__(self,movies):
        self.movies = movies
    def recommendation(self,user):
        recom_movie = []
        for movie in self.movies:
            if movie.genre in user.liked_genre:
                recom_movie.append(movie)
        recom_movie.sort(key=lambda m:m.rating,reverse=True) # sort the list of movie from high to low
        return recom_movie[:5]
movie_list = [Movie("The Shawshank Redemption","Drama",9.3),
              Movie("Inception","Sci-Fi",8.8),
              Movie("The Dark Knight","Action",9.0),
              Movie("Forrest Gump","Romance",8.8),
              Movie("Interstellar","Sci-Fi",8.6),
              Movie("The Godfather","Crime",9.2),
              Movie("La La Land","Romance ",8.0),
              Movie("Spider-Man: No Way Home","Fantasy",8.2),
              Movie("Coco","Fantasy",8.4)]
user1 = User("parul",["Fantasy","Sci-Fi","Action"])
recommender = Recommender(movie_list)
top_movies = recommender.recommendation(user1)

print(user1)
print("-------------------------------------------------")
print(f"🎬Recommended Movies for {user1.name}:")
for movie in top_movies:
    print(f"⭐{movie}")

user2 = User("shyam",["Drama","Crime"])
recommender = Recommender(movie_list)
top_movies = recommender.recommendation(user2)

print(user2)
print("-------------------------------------------------")
print(f"🎬Recommended Movies for {user2.name}:")
for movie in top_movies:
    print(f"⭐{movie}")

















