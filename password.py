import sys
import subprocess
import random
import os

def install_packages(packages):
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Установка пакета {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Пакет {package} успешно установлен.")

required_packages = []

install_packages(required_packages)

header = """
██████╗░░█████╗░░██████╗░██████╗░██╗░░░░░░░██╗░█████╗░██████╗░██████╗░
██╔══██╗██╔══██╗██╔════╝██╔════╝░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗
██████╔╝███████║╚█████╗░╚█████╗░░╚██╗████╗██╔╝██║░░██║██████╔╝██║░░██║
██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗░░████╔═████║░██║░░██║██╔══██╗██║░░██║
██║░░░░░██║░░██║██████╔╝██████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝██║░░██║██████╔╝
╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝░░░╚════╝░╚═╝░░╚═╝╚═════╝░

░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
"""

def show_menu():
    print(header)
    print("Выберите действие:")
    print("1. Генерировать пароли")
    print("2. Очистить файл password.csv")
    print("0. Выход")
    choice = input("Ваш выбор: ")
    return choice

def generate_unique_passwords(num_passwords=10000, max_attempts=10_000_000, progress_interval=10000):
    bases = [
        "qwerty", "asdfgh", "zxcvbn", "123456", "1qaz2wsx", 
        "qazwsx", "password", "admin", "welcome", "login",
        "sunshine", "football", "monkey", "dragon", "baseball",
        "letmein", "superman", "mustang", "shadow", "master",
        "hello", "freedom", "whatever", "trustno1", "starwars",
        "iloveyou", "princess", "rockyou", "solo", "fuckyou",
        "jordan", "harley", "hunter", "buster", "soccer",
        "batman", "test", "killer", "hockey", "george",
        "charlie", "andrew", "michelle", "love", "jennifer",
        "thomas", "matrix", "computer", "internet", "access",
        
        "michael", "christopher", "joshua", "matthew", "daniel",
        "david", "john", "james", "robert", "ryan",
        "jason", "justin", "brandon", "william", "nick",
        "anthony", "kevin", "steven", "timothy", "richard",
        "joseph", "jeremy", "brian", "charles", "aaron",
        "adam", "mark", "paul", "jose", "kenneth",
        "jonathan", "stephen", "patrick", "scott", "gregory",
        "benjamin", "samuel", "raymond", "jack", "alexander",
        "angel", "dennis", "jerry", "henry", "douglas",
        "peter", "tyler", "austin", "jesse", "albert",
        "arthur", "jimmy", "shawn", "victor", "ralph",
        "billy", "bruce", "joe", "bobby", "philip",
        "johnny", "randy", "howard", "craig", "juan",
        "louis", "russell", "eugene", "wayne", "fred",
        "gary", "oscar", "alan", "jim", "ronald",
        "roy", "vincent", "danny", "timmy", "carl",
        
        "dragon", "monkey", "tiger", "lion", "leopard",
        "panther", "cheetah", "wolf", "fox", "eagle",
        "shark", "whale", "dolphin", "snake", "python",
        "falcon", "hawk", "raptor", "bear", "bull",
        "horse", "pony", "unicorn", "kitten", "puppy",
        "bird", "fish", "rabbit", "hamster", "spider",
        "scorpion", "gorilla", "rhino", "zebra", "giraffe",
        "kangaroo", "crocodile", "alligator", "raccoon", "panda",
        
        "soccer", "football", "baseball", "basketball", "hockey",
        "tennis", "golf", "boxing", "racing", "surfing",
        "skiing", "snowboard", "volleyball", "cricket", "rugby",
        "wrestling", "karate", "judo", "archery", "fencing",
        "cycling", "running", "swimming", "diving", "gymnastics",
        
        "starwars", "matrix", "terminator", "predator", "alien",
        "avengers", "superman", "batman", "spiderman", "ironman",
        "hulk", "thor", "captain", "wolverine", "deadpool",
        "supergirl", "flash", "aquaman", "joker", "harley",
        "gotham", "skywalker", "vader", "yoda", "chewbacca",
        "hobbit", "gandalf", "potter", "hermione", "voldemort",
        "skyrim", "witcher", "dragonage", "mass", "halo",
        "doom", "quake", "wolfenstein", "fallout", "resident",
        
        "metallica", "slayer", "megadeth", "anthrax", "ironmaiden",
        "sabbath", "pantera", "motorhead", "judas", "acdc",
        "gunsnroses", "aerosmith", "vanhalen", "kiss", "queen",
        "beatles", "rollingstones", "ledzeppelin", "pinkfloyd", "doors",
        "nirvana", "pearljam", "soundgarden", "aliceinchains", "stone",
        "radiohead", "oasis", "blur", "coldplay", "u2",
        "greenday", "offspring", "ramones", "sexpistols", "clash",
        
        "newyork", "london", "paris", "berlin", "tokyo",
        "moscow", "rome", "madrid", "barcelona", "amsterdam",
        "dublin", "vienna", "prague", "budapest", "warsaw",
        "lisbon", "athens", "istanbul", "dubai", "mumbai",
        "shanghai", "beijing", "seoul", "sydney", "melbourne",
        "toronto", "vancouver", "montreal", "chicago", "losangeles",
        "sanfrancisco", "lasvegas", "miami", "houston", "boston",
        "philadelphia", "phoenix", "seattle", "denver", "dallas",
        
        "apple", "orange", "banana", "peach", "grape",
        "strawberry", "blueberry", "watermelon", "pineapple", "mango",
        "cherry", "lemon", "lime", "coconut", "kiwi",
        "pear", "apricot", "avocado", "blackberry", "cantaloupe",
        "fig", "grapefruit", "guava", "honeydew", "melon",
        "nectarine", "olive", "papaya", "passionfruit", "plum",
        "pomegranate", "raspberry", "tangerine", "tomato", "cucumber",
        "carrot", "potato", "onion", "garlic", "pepper",
        "broccoli", "cauliflower", "cabbage", "lettuce", "spinach",
        "celery", "asparagus", "eggplant", "zucchini", "pumpkin",
        "radish", "beet", "corn", "pea", "bean",
        "lentil", "chickpea", "soybean", "alfalfa", "clover",
        "sunflower", "daisy", "rose", "tulip", "lily",
        "daffodil", "dandelion", "marigold", "petunia", "violet",
        "iris", "orchid", "peony", "hydrangea", "lavender",
        "jasmine", "lilac", "magnolia", "poppy", "snapdragon",
        "dahlia", "begonia", "geranium", "zinnia", "cosmos",
        "aster", "carnation", "chrysanthemum", "forgetmenot", "gladiolus",
        "hibiscus", "hollyhock", "hyacinth", "impatiens", "lobelia",
        "nasturtium", "pansy", "phlox", "primrose", "ranunculus",
        "rhododendron", "salvia", "scabiosa", "stock", "sweetpea",
        "verbena", "wallflower", "weigela", "wisteria", "yucca",
        "agave", "aloe", "bamboo", "cactus", "fern",
        "ivy", "moss", "palm", "reed", "sage",
        "thyme", "basil", "chive", "cilantro", "dill",
        "fennel", "marjoram", "oregano", "parsley", "rosemary",
        "savory", "tarragon", "vanilla", "wasabi", "ginger",
        "turmeric", "cinnamon", "nutmeg", "clove", "allspice",
        "cardamom", "coriander", "cumin", "mustard", "paprika",
        "pepper", "saffron", "sumac", "tamarind", "vinegar",
        "yeast", "baking", "soda", "powder", "flour",
        "sugar", "honey", "syrup", "molasses", "jam",
        "jelly", "marmalade", "butter", "cheese", "yogurt",
        "cream", "milk", "sourcream", "mayo", "ketchup",
        "mustard", "relish", "salsa", "guacamole", "hummus",
        "pesto", "tahini", "soysauce", "teriyaki", "worcestershire",
        "vinegar", "oil", "oliveoil", "canola", "vegetable",
        "coconut", "peanut", "almond", "walnut", "pecan",
        "cashew", "pistachio", "hazelnut", "macadamia", "chestnut",
        "sunflower", "pumpkin", "sesame", "flax", "chia",
        "quinoa", "rice", "brownrice", "basmati", "jasmine",
        "wildrice", "barley", "oats", "wheat", "rye",
        "corn", "millet", "sorghum", "bulgur", "couscous",
        "farro", "freekeh", "spelt", "teff", "amaranth",
        "buckwheat", "kamut", "muesli", "granola", "cereal",
        "pasta", "spaghetti", "penne", "fettuccine", "linguine",
        "macaroni", "fusilli", "rotini", "orzo", "lasagna",
        "ravioli", "tortellini", "gnocchi", "udon", "soba",
        "ramen", "vermicelli", "noodles", "rice", "risotto",
        "polenta", "grits", "mashed", "baked", "fried",
        "roasted", "grilled", "steamed", "boiled", "sauteed",
        "stirfried", "braised", "poached", "seared", "smoked",
        "cured", "pickled", "fermented", "raw", "juiced",
        "blended", "pureed", "whipped", "frosted", "glazed",
        "iced", "drizzled", "sprinkled", "topped", "stuffed",
        "wrapped", "rolled", "folded", "layered", "stacked",
        "shredded", "sliced", "diced", "chopped", "minced",
        "crushed", "mashed", "pureed", "grated", "zested",
        "juiced", "squeezed", "pressed", "extracted", "brewed",
        "steeped", "infused", "marinated", "brined", "cured",
        "smoked", "dried", "dehydrated", "freezedried", "candied",
        "glazed", "caramelized", "charred", "blackened", "seared",
        "browned", "toasted", "roasted", "grilled", "broiled",
        "baked", "fried", "deepfried", "panfried", "stirfried",
        "sauteed", "simmered", "braised", "stewed", "poached",
        "steamed", "boiled", "blanched", "parboiled", "scalded",
        "melted", "clarified", "whipped", "churned", "cultured",
        "fermented", "leavened", "proofed", "kneaded", "rolled",
        "cut", "shaped", "molded", "formed", "scored",
        "glazed", "iced", "frosted", "filled", "stuffed",
        "layered", "stacked", "assembled", "plated", "garnished",
        "decorated", "presented", "served", "enjoyed", "consumed",
        "devoured", "savored", "relished", "appreciated", "loved",
        "adored", "cherished", "treasured", "valued", "prized",
        "esteemed", "respected", "admired", "revered", "worshipped",
        "idolized", "lionized", "celebrated", "commemorated", "remembered",
        "honored", "respected", "venerated", "exalted", "glorified",
        "magnified", "aggrandized", "dignified", "ennobled", "elevated",
        "uplifted", "enhanced", "embellished", "enriched", "improved",
        "refined", "perfected", "polished", "honed", "sharpened",
        "strengthened", "fortified", "reinforced", "buttressed", "supported",
        "sustained", "maintained", "preserved", "conserved", "protected",
        "defended", "guarded", "shielded", "sheltered", "secured",
        "anchored", "moored", "fastened", "tethered", "hitched",
        "harnessed", "yoked", "bridled", "reined", "curbed",
        "checked", "restrained", "constrained", "restricted", "limited",
        "bounded", "circumscribed", "delimited", "defined", "determined",
        "fixed", "established", "settled", "resolved", "decided",
        "concluded", "finalized", "completed", "finished", "ended",
        "terminated", "ceased", "stopped", "halted", "paused",
        "suspended", "interrupted", "discontinued", "abandoned", "forsaken",
        "deserted", "relinquished", "surrendered", "yielded", "ceded",
        "conceded", "admitted", "acknowledged", "confessed", "avowed",
        "declared", "proclaimed", "announced", "published", "broadcast",
        "disseminated", "circulated", "propagated", "spread", "diffused",
        "dispersed", "scattered", "distributed", "allocated", "apportioned",
        "assigned", "designated", "specified", "stipulated", "prescribed",
        "ordained", "decreed", "commanded", "ordered", "directed",
        "instructed", "guided", "led", "conducted", "managed",
        "administered", "supervised", "oversaw", "governed", "ruled",
        "controlled", "regulated", "moderated", "mediated", "arbitrated",
        "adjudicated", "judged", "sentenced", "condemned", "convicted",
        "acquitted", "exonerated", "absolved", "pardoned", "forgiven",
        "excused", "justified", "vindicated", "validated", "verified",
        "confirmed", "substantiated", "corroborated", "authenticated", "certified",
        "accredited", "licensed", "authorized", "sanctioned", "approved",
        "endorsed", "ratified", "validated", "legitimized", "legalized",
        "institutionalized", "formalized", "standardized", "normalized", "regularized",
        "systematized", "organized", "arranged", "ordered", "classified",
        "categorized", "sorted", "grouped", "clustered", "bunched",
        "bundled", "packaged", "wrapped", "boxed", "crated",
        "contained", "encased", "enclosed", "surrounded", "enveloped",
        "swathed", "shrouded", "veiled", "masked", "cloaked",
        "disguised", "camouflaged", "concealed", "hidden", "obscured",
        "covered", "blanketed", "overlaid", "coated", "painted",
        "varnished", "lacquered", "glazed", "polished", "burnished",
        "buffered", "rubbed", "smoothed", "leveled", "flattened",
        "evened", "balanced", "equalized", "stabilized", "steadyed",
        "calmed", "soothed", "pacified", "placated", "appeased",
        "mollified", "conciliated", "reconciled", "harmonized", "integrated",
        "unified", "consolidated", "merged", "amalgamated", "fused",
        "blended", "mixed", "combined", "joined", "connected",
        "linked", "attached", "affixed", "fastened", "secured",
        "anchored", "moored", "tethered", "hitched", "harnessed",
        "yoked", "bridled", "reined", "curbed", "checked",
        "restrained", "constrained", "restricted", "limited", "bounded",
        "circumscribed", "delimited", "defined", "determined", "fixed",
        "established", "settled", "resolved", "decided", "concluded",
        "finalized", "completed", "finished", "ended", "terminated",
        "ceased", "stopped", "halted", "paused", "suspended",
        "interrupted", "discontinued", "abandoned", "forsaken", "deserted",
        "relinquished", "surrendered", "yielded", "ceded", "conceded",
        "admitted", "acknowledged", "confessed", "avowed", "declared",
        "proclaimed", "announced", "published", "broadcast", "disseminated",
        "circulated", "propagated", "spread", "diffused", "dispersed",
        "scattered", "distributed", "allocated", "apportioned", "assigned",
        "designated", "specified", "stipulated", "prescribed", "ordained",
        "decreed", "commanded", "ordered", "directed", "instructed",
        "guided", "led", "conducted", "managed", "administered",
        "supervised", "oversaw", "governed", "ruled", "controlled",
        "regulated", "moderated", "mediated", "arbitrated", "adjudicated",
        "judged", "sentenced", "condemned", "convicted", "acquitted",
        "exonerated", "absolved", "pardoned", "forgiven", "excused",
        "justified", "vindicated", "validated", "verified", "confirmed",
        "substantiated", "corroborated", "authenticated", "certified", "accredited",
        "licensed", "authorized", "sanctioned", "approved", "endorsed",
        "ratified", "validated", "legitimized", "legalized", "institutionalized",
        "formalized", "standardized", "normalized", "regularized", "systematized",
        "organized", "arranged", "ordered", "classified", "categorized",
        "sorted", "grouped", "clustered", "bunched", "bundled",
        "packaged", "wrapped", "boxed", "crated", "contained",
        "encased", "enclosed", "surrounded", "enveloped", "swathed",
        "shrouded", "veiled", "masked", "cloaked", "disguised",
        "camouflaged", "concealed", "hidden", "obscured", "covered",
        "blanketed", "overlaid", "coated", "painted", "varnished",
        "lacquered", "glazed", "polished", "burnished", "buffered",
        "rubbed", "smoothed", "leveled", "flattened", "evened",
        "balanced", "equalized", "stabilized", "steadyed", "calmed",
        "soothed", "pacified", "placated", "appeased", "mollified",
        "conciliated", "reconciled", "harmonized", "integrated", "unified",
        "consolidated", "merged", "amalgamated", "fused", "blended",
        "mixed", "combined", "joined", "connected", "linked",
        "attached", "affixed", "fastened", "secured", "anchored",
        "moored", "tethered", "hitched", "harnessed", "yoked",
        "bridled", "reined", "curbed", "checked", "restrained",
        "constrained", "restricted", "limited", "bounded", "circumscribed",
        "delimited", "defined", "determined", "fixed", "established",
        "settled", "resolved", "decided", "concluded", "finalized",
        "completed", "finished", "ended", "terminated", "ceased",
        "stopped", "halted", "paused", "suspended", "interrupted",
        "discontinued", "abandoned", "forsaken", "deserted", "relinquished",
        "surrendered", "yielded", "ceded", "conceded", "admitted",
        "acknowledged", "confessed", "avowed", "declared", "proclaimed",
        "announced", "published", "broadcast", "disseminated", "circulated",
        "propagated", "spread", "diffused", "dispersed", "scattered",
        "distributed", "allocated", "apportioned", "assigned", "designated",
        "specified", "stipulated", "prescribed", "ordained", "decreed",
        "commanded", "ordered", "directed", "instructed", "guided",
        "led", "conducted", "managed", "administered", "supervised",
        "oversaw", "governed", "ruled", "controlled", "regulated",
        "moderated", "mediated", "arbitrated", "adjudicated", "judged",
        "sentenced", "condemned", "convicted", "acquitted", "exonerated",
        "absolved", "pardoned", "forgiven", "excused", "justified",
        "vindicated", "validated", "verified", "confirmed", "substantiated",
        "corroborated", "authenticated", "certified", "accredited", "licensed",
        "authorized", "sanctioned", "approved", "endorsed", "ratified",
        "validated", "legitimized", "legalized", "institutionalized", "formalized",
        "standardized", "normalized", "regularized", "systematized", "organized",
        "arranged", "ordered", "classified", "categorized", "sorted",
        "grouped", "clustered", "bunched", "bundled", "packaged",
        "wrapped", "boxed", "crated", "contained", "encased",
        "enclosed", "surrounded", "enveloped", "swathed", "shrouded",
        "veiled", "masked", "cloaked", "disguised", "camouflaged",
        "concealed", "hidden", "obscured", "covered", "blanketed",
        "overlaid", "coated", "painted", "varnished", "lacquered",
        "glazed", "polished", "burnished", "buffered", "rubbed",
        "smoothed", "leveled", "flattened", "evened", "balanced",
        "equalized", "stabilized", "steadyed", "calmed", "soothed",
        "pacified", "placated", "appeased", "mollified", "conciliated",
        "reconciled", "harmonized", "integrated", "unified", "consolidated",
        "merged", "amalgamated", "fused", "blended", "mixed",
        "combined", "joined", "connected", "linked", "attached",
        "affixed", "fastened", "secured", "anchored", "moored",
        "tethered", "hitched", "harnessed", "yoked", "bridled",
        "reined", "curbed", "checked", "restrained", "constrained",
        "restricted", "limited", "bounded", "circumscribed", "delimited",
        "defined", "determined", "fixed", "established", "settled",
        "resolved", "decided", "concluded", "finalized", "completed",
        "finished", "ended", "terminated", "ceased", "stopped",
        "halted", "paused", "suspended", "interrupted", "discontinued",
        "abandoned", "forsaken", "deserted", "relinquished", "surrendered",
        "yielded", "ceded", "conceded", "admitted", "acknowledged",
        "confessed", "avowed", "declared", "proclaimed", "announced",
        "published", "broadcast", "disseminated", "circulated", "propagated",
        "spread", "diffused", "dispersed", "scattered", "distributed",
        "allocated", "apportioned", "assigned", "designated", "specified",
        "stipulated", "prescribed", "ordained", "decreed", "commanded",
        "ordered", "directed", "instructed", "guided", "led",
        "conducted", "managed", "administered", "supervised", "oversaw",
        "governed", "ruled", "controlled", "regulated", "moderated",
        "mediated", "arbitrated", "adjudicated", "judged", "sentenced",
        "condemned", "convicted", "acquitted", "exonerated", "absolved",
        "pardoned", "forgiven", "excused", "justified", "vindicated",
        "validated", "verified", "confirmed", "substantiated", "corroborated",
        "authenticated", "certified", "accredited", "licensed", "authorized",
        "sanctioned", "approved", "endorsed", "ratified", "validated",
        "legitimized", "legalized", "institutionalized", "formalized", "standardized",
        "normalized", "regularized", "systematized", "organized", "arranged",
        "ordered", "classified", "categorized", "sorted", "grouped",
        "clustered", "bunched", "bundled", "packaged", "wrapped",
        "boxed", "crated", "contained", "encased", "enclosed",
        "surrounded", "enveloped", "swathed", "shrouded", "veiled",
        "masked", "cloaked", "disguised", "camouflaged", "concealed",
        "hidden", "obscured", "covered", "blanketed", "overlaid",
        "coated", "painted", "varnished", "lacquered", "glazed",
        "polished", "burnished", "buffered", "rubbed", "smoothed",
        "leveled", "flattened", "evened", "balanced", "equalized",
        "stabilized", "steadyed", "calmed", "soothed", "pacified",
        "placated", "appeased", "mollified", "conciliated", "reconciled",
        "harmonized", "integrated", "unified", "consolidated", "merged",
        "amalgamated", "fused", "blended", "mixed", "combined",
        "joined", "connected", "linked", "attached", "affixed",
        "fastened", "secured", "anchored", "moored", "tethered",
        "hitched", "harnessed", "yoked", "bridled", "reined",
        "curbed", "checked", "restrained", "constrained", "restricted",
        "limited", "bounded", "circumscribed", "delimited", "defined",
        "determined", "fixed", "established", "settled", "resolved",
        "decided", "concluded", "finalized", "completed", "finished",
        "ended", "terminated", "ceased", "stopped", "halted",
        "paused", "suspended", "interrupted", "discontinued", "abandoned",
        "forsaken", "deserted", "relinquished", "surrendered", "yielded",
        "ceded", "conceded", "admitted", "acknowledged", "confessed",
        "avowed", "declared", "proclaimed", "announced", "published",
        "broadcast", "disseminated", "circulated", "propagated", "spread",
        "diffused", "dispersed", "scattered", "distributed", "allocated",
        "apportioned", "assigned", "designated", "specified", "stipulated",
        "prescribed", "ordained", "decreed", "commanded", "ordered",
        "directed", "instructed", "guided", "led", "conducted",
        "managed", "administered", "supervised", "oversaw", "governed",
        "ruled", "controlled", "regulated", "moderated", "mediated",
        "arbitrated", "adjudicated", "judged", "sentenced", "condemned",
        "convicted", "acquitted", "exonerated", "absolved", "pardoned",
        "forgiven", "excused", "justified", "vindicated", "validated",
        "verified", "confirmed", "substantiated", "corroborated", "authenticated",
        "certified", "accredited", "licensed", "authorized", "sanctioned",
        "approved", "endorsed", "ratified", "validated", "legitimized",
        "legalized", "institutionalized", "formalized", "standardized", "normalized",
        "regularized", "systematized", "organized", "arranged", "ordered",
        "classified", "categorized", "sorted", "grouped", "clustered",
        "bunched", "bundled", "packaged", "wrapped", "boxed",
        "crated", "contained", "encased", "enclosed", "surrounded",
        "enveloped", "swathed", "shrouded", "veiled", "masked",
        "cloaked", "disguised", "camouflaged", "concealed", "hidden",
        "obscured", "covered", "blanketed", "overlaid", "coated",
        "painted", "varnished", "lacquered", "glazed", "polished",
        "burnished", "buffered", "rubbed", "smoothed", "leveled",
        "flattened", "evened", "balanced", "equalized", "stabilized",
        "steadyed", "calmed", "soothed", "pacified", "placated",
        "appeased", "mollified", "conciliated", "reconciled", "harmonized",
        "integrated", "unified", "consolidated", "merged", "amalgamated",
        "fused", "blended", "mixed", "combined", "joined",
        "connected", "linked", "attached", "affixed", "fastened",
        "secured", "anchored", "moored", "tethered", "hitched",
        "harnessed", "yoked", "bridled", "reined", "curbed",
        "checked", "restrained", "constrained", "restricted", "limited",
        "bounded", "circumscribed", "delimited", "defined", "determined",
        "fixed", "established", "settled", "resolved", "decided",
        "concluded", "finalized", "completed", "finished", "ended",
        "terminated", "ceased", "stopped", "halted", "paused",
        "suspended", "interrupted", "discontinued", "abandoned", "forsaken",
        "deserted", "relinquished", "surrendered", "yielded", "ceded",
        "conceded", "admitted", "acknowledged", "confessed", "avowed",
        "declared", "proclaimed", "announced", "published", "broadcast",
        "disseminated", "circulated", "propagated", "spread", "diffused",
        "dispersed", "scattered", "distributed", "allocated", "apportioned",
        "assigned", "designated", "specified", "stipulated", "prescribed",
        "ordained", "decreed", "commanded", "ordered", "directed",
        "instructed", "guided", "led", "conducted", "managed",
        "administered", "supervised", "oversaw", "governed", "ruled",
        "controlled", "regulated", "moderated", "mediated", "arbitrated",
        "adjudicated", "judged", "sentenced", "condemned", "convicted",
        "acquitted", "exonerated", "absolved", "pardoned", "forgiven",
        "excused", "justified", "vindicated", "validated", "verified",
        "confirmed", "substantiated", "corroborated", "authenticated", "certified",
        "accredited", "licensed", "authorized", "sanctioned", "approved",
        "endorsed", "ratified", "validated", "legitimized", "legalized",
        "institutionalized", "formalized", "standardized", "normalized", "regularized",
        "systematized", "organized", "arranged", "ordered", "classified",
        "categorized", "sorted", "grouped", "clustered", "bunched",
        "bundled", "packaged", "wrapped", "boxed", "crated",
        "contained", "encased" 
]

    passwords = set()
    attempts = 0
    generated = 0
    while generated < num_passwords and attempts < max_attempts:
        base_word = random.choice(bases)
        variation_type = random.randint(0, 2)
        if variation_type == 0:
            pwd = base_word
        elif variation_type == 1:
            number = random.randint(0, 999999)
            pwd = f"{base_word}{number}"
        else:
            if random.choice([True, False]):
                pwd = base_word.upper()
            else:
                pwd = base_word.lower()

        if pwd not in passwords:
            passwords.add(pwd)
            generated += 1

        attempts += 1
        if attempts % progress_interval == 0:
            print(f"Попыток: {attempts}, сгенерировано уникальных паролей: {generated}/{num_passwords}")

        if attempts >= max_attempts:
            print("Достигнут лимит попыток для генерации уникальных паролей.")
            break

    if generated < num_passwords:
        print(f"Не удалось сгенерировать запрошенное количество уникальных паролей. Получено: {generated}.")
    return list(passwords)

def clear_password_file():
    with open("password.csv", "w", encoding="utf-8") as f:
        pass
    print("Файл password.csv очищен.")

while True:
    choice = show_menu()
    if choice == '0':
        print("Выход из программы.")
        break
    elif choice == '1':
        try:
            total_input = input("Введите количество паролей для генерации (до 10 000 000): ")
            total = int(total_input)
            if total <= 0 or total > 10000000:
                print("Пожалуйста, введите число от 1 до 10 000 000.")
                continue
        except ValueError:
            print("Некорректный ввод.")
            continue
        print(f"Генерация {total} уникальных паролей...")
        passwords = generate_unique_passwords(total, progress_interval=max(10000, total // 10))
        with open("password.csv", "w", encoding="utf-8") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print("Пароли успешно сохранены в файл password.csv.")
        input("Нажмите Enter для возврата в меню...")
    elif choice == '2':
        clear_password_file()
        input("Нажмите Enter для возврата в меню...")
    else:
        print("Некорректный выбор. Попробуйте снова.")

# Discord : killmeyoudamnschoolboy
# Telegram : killmeyoudamnschoolboy