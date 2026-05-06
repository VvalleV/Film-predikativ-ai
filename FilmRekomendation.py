media = [
    {"title":"Interstellar","genre":"sci fi","mood":"exciting","age":"13+", "runtime":"2:49"},
    {"title":"War Machine","genre":"action","mood":"funny","age":"16+","runtime":"1:49"},
    {"title":"The Equalizer","genre":"thriller","mood":"exciting","age":"15+","runtime": "2:12"},
    {"title":"The Conjuring","genre":"horror","mood":"scary","age":"15+","runtime":"1:52"},
    {"title":"Lord Of The Rings","genre":"adventure","mood":"epic","age":"11+","runtime":"2:58"},
    {"title":"The Mummy","genre":"adventure","mood":"exciting","age":"15+","runtime":"1:50"},
    {"title":"Jack Reacher","genre":"action","mood":"exciting","age":"15+","runtime":"2:10"},
    {"title":"2012","genre":"sci fi","mood":"exciting","age":"11+","runtime":"2:38"},
    {"title":"Bad Boys Ride Or Die","genre":"comedy","mood":"funny","age":"15+","runtime":"1:55"},
    {"title":"Terrifier","genre":"horror","mood":"scary","age":"18+","runtime":"1:25"}
]

while True:
    
    genre = input("What genre do you like? ").lower()
    mood = input("What mood do you want? ").lower()

    
    recommendations = 0

    print("We recommend:")

    
    for movie in media:
        score = 0

        
        if movie["genre"] == genre:
            score += 2

       
        if movie["mood"] == mood:
            score += 1

        
        if score >= 2:
            print(movie["title"])
            recommendations += 1

       
        if recommendations == 3:
            break

    if recommendations == 0:
        print("No good matches found.")

    
    answer = input("Do you need more recommendations? (yes/no): ").lower()

    if answer == "no":
        print("Goodbye!")
        break