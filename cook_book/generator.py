import random

# Seznam názvů jídel
dish_names = [
    "Kuřecí směs s brokolicí",
    "Zeleninový ragú s rýží",
    "Losos na grilu se špenátem",
    "Těstoviny s krémovou omáčkou",
    "Květáková polévka s hříbky",
    "Rajčatový salát s mozzarellou",
    "Hovězí burger s cibulí",
    "Tropický smoothie s kokosem",
    "Bruschetta s avokádem",
    "Pizza s šunkou a žampiony",
    "Rýžový nákyp s jahodami",
    "Kuřecí kari s rýží",
    "Grilovaná zelenina s bylinkovým olejem",
    "Veganský quinoa salát",
    "Lazanje se špenátem a ricottou",
    "Hovězí steak s pepřovou omáčkou",
    "Křupavý kuřecí salát",
    "Ryba na medu s citronem",
    "Cizrna s indickými kořením",
    "Mexické tacos s fazolem",
    "Tunak s avokádem a sezamem",
    "Hovězí guláš s knedlíky",
    "Čočková polévka s kari",
    "Ovocný jogurtový pohár",
    "Těstoviny aglio e olio",
    "Karamelizovaný banán s povidly",
    "Lilek plněný sýrem",
    "Pečené brambory s rozmarýnem",
    "Květákové karbanátky",
    "Klasická vepřová pečeně s knedlíkem"
]

# Seznam ingrediencí
ingredients = [
    ["kuřecí maso", "brokolice", "cibule", "česnek"],
    ["zelenina", "rajčatová omáčka", "rýže"],
    ["losos", "špenát", "citron", "olivový olej"],
    ["těstoviny", "smetana", "sýr"],
    ["květák", "hříbky", "cibule", "vývar"],
    ["rajčata", "mozzarella", "bazalka", "olivový olej"],
    ["hovězí maso", "cibule", "rajčata", "chleba"],
    ["banán", "ananas", "kokosové mléko"],
    ["chleba", "avokádo", "rajčata", "česnek"],
    ["těsto", "šunka", "žampiony", "sýr"],
    ["rýže", "mléko", "jahody"],
    ["kuřecí maso", "kari koření", "kokosové mléko"],
    ["zelenina", "bylinky", "olivový olej"],
    ["quinoa", "zelenina", "citronová omáčka"],
    ["lazanje těsto", "špenát", "ricotta", "sýr"],
    ["hovězí steak", "černý pepř", "smetana"],
    ["kuřecí maso", "zelenina", "krutony", "dresing"],
    ["ryba", "med", "citron", "sojová omáčka"],
    ["cizrna", "rajčatová omáčka", "kari koření"],
    ["taco plátek", "fazole", "sýr", "zelenina"],
    ["tuňák", "avokádo", "sezamová semínka"],
    ["hovězí maso", "cibule", "paprika", "česnek"],
    ["červená čočka", "mrkev", "cibule", "kari koření"],
    ["jogurt", "jahody", "banán", "med"],
    ["těstoviny", "česnek", "olivový olej", "pepř"],
    ["banán", "cukr", "povidla"],
    ["lilek", "sýr", "bylinky"],
    ["brambory", "rozmarýn", "olivový olej", "sůl"],
    ["květák", "sýr", "vejce", "strouhanka"],
    ["vepřová pečeně", "houskový knedlík", "zelí"]
]

# Generování náhodných receptů
def generate_recipes():
    recipes = []
    for dish_name, ingredient_list in zip(dish_names, ingredients):
        recipe = {"name": dish_name, "ingredients": ingredient_list}
        recipes.append(recipe)
    return recipes

# Vytvoření seznamu receptů
recipes = generate_recipes()

# Výpis náhodně generovaných receptů
for recipe in recipes:
    print(recipe["name"])
    print(", ".join(recipe["ingredients"]))
    print("=" * 40)
