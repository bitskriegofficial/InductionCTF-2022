import json
import os

continents = json.load(open("continent.json","r"))
countries = json.load(open("names.json", "r"))
continent_codes = {
    "AS":"Asia",
    "AF":"Africa",
    "OC":"Oceania",
    "EU":"Europe",
    "SA":"South America",
    "NA":"North America",
    "AN":"Antartica"
}

song = """There once was a ship that put to sea
The name of the ship was the Billy of Tea
The winds blew up, her bow dipped down
Oh blow, my bully boys, blow (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
She'd not been two weeks from shore
When down on her a right whale bore
The captain called all hands and swore
He'd take that whale in tow (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
Da-da-da-da-da
Da-da-da-da-da-da-da
Da-da-da-da-da-da-da-da-da-da-da
Before the boat had hit the water
The whale's tail came up and caught her
All hands to the side, harpooned and fought her
When she dived down low (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
No line was cut, no whale was freed
The captain's mind was not of greed
And he belonged to the Whaleman's creed
She took that ship in tow (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
Da-da-da-da-da
Da-da-da-da-da-da-da
Da-da-da-da-da-da-da-da-da-da-da
For forty days or even more
The line went slack then tight once more
All boats were lost, there were only four
But still that whale did go (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
As far as I've heard, the fight's still on
The line's not cut, and the whale's not gone
The Wellerman makes his regular call
To encourage the captain, crew and all (huh)
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
Soon may the Wellerman come
To bring us sugar and tea and rum
One day, when the tonguing is done
We'll take our leave and go
"""
parent = os.path.join(os.curdir,"World")

for country_code in countries.keys():
    continent = continents[country_code]
    os.makedirs(os.path.join(parent, continent_codes[continent], countries[country_code]), exist_ok=True)
    with open(os.path.join(parent, continent_codes[continent], countries[country_code],"flag.txt"),"w") as f:
        f.write(song)
