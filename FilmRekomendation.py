media = [
    {"title":"Interstellar","genre":"sci fi","mood":"exciting"},
    {"title":"War Machine","genre":"action","mood":"funny"},
    {"title":"The Equalizer","genre":"thriller","mood":"exciting"},
    {"title":"The Conjuring","genre":"horror","mood":"scary"},
    {"title":"Lord Of The Rings","genre":"adventure","mood":"epic"},
    {"title":"The Mummy","genre":"adventure","mood":"exciting"},
    {"title":"Jack Reacher","genre":"action","mood":"exciting"},
    {"title":"2012","genre":"sci fi","mood":"exciting"},
    {"title":"Bad Boys Ride Or Die","genre":"comedy","mood":"funny"},
    {"title":"Terrifier","genre":"horror","mood":"scary"}
]
   #while loop som får att programmet fortsätta att köra tills användaren väljer att avsluta. Den frågar användaren om deras favoritgenre och stämning, och ger sedan rekommendationer baserat på dessa preferenser. Om inga matchningar hittas, informeras användaren om det. Efter att ha gett rekommendationer, frågar programmet om användaren vill ha fler rekommendationer eller avsluta programmet.
while True:
    genre = input("What genre do you like? ").lower() #frågar användaren om deras favoritgenre och konverterar svaret till små bokstäver.
    mood = input("What mood do you want? ").lower()   #frågar användaren om vilken stämning de vill ha och konverterar svaret till små bokstäver.

    recommendations = 0 #räknar antalet rekommendationer som ges till användaren. Den börjar på 0 och ökar varje gång en matchning hittas.

    print("We recommend:") #rubrik till rekomendationerna 

    for movie in media: #loopar igenom alla filmer i listan
        score = 0 #varje film börjar med en poäng på 0, och poängen ökar baserat på hur väl filmen matchar användarens preferenser. Om genren matchar, ökar poängen med 2, och om stämningen matchar, ökar poängen med 1.

        if movie["genre"] == genre:
            score += 2

        if movie["mood"] == mood:
            score += 1

        if score >= 2:
            recommendations += 1
            print(str(recommendations) + ".", movie["title"])

        if recommendations == 3:
            break
     
    if recommendations == 0:
        print("No good matches found.")

    answer = input("Do you need more recommendations? (yes/no): ").lower()

    if answer == "no":
        print("Goodbye!")
        break   