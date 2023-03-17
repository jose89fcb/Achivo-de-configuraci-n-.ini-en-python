import configparser

config = configparser.ConfigParser()
config.read("canales.ini")

yo = config.get("Twitter_jose89fcb","Twitter")
fn = config.get("Twitter_fortnite", "Twitter")
hb = config.get("Twitter_eshabbo", "twitter")

print(f"Mi twitter: {yo}")
print(f"Twitter de fortnite: {fn}")
print(f"Twitter de habbo: {hb}")


#Esto es sólo un ejemplo
