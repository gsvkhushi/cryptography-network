cybersecurity_incidents=[
    "The Morris Worm disrupted computers in 988, one of the first computer worms distributed via the internet.", 
    "In 2007 , estonia suffered a massive DDos maatack that crippled the nation's  digital infrastruture.", 
    "In 2013, target experienced a major data breach where millions of credit card details were stolen.",
    "the Wannacry ransonware attack in 2017 affected thousands of computers globally, encrypting data and demanding ransom.",
    "A phishing attack in 2016 compromised the email accounts of several high-profile figures,leading to the release of sensitive information.",
    "The Mirai bothnet in 2016 launcheed DDos attacks using Iot devices , bringing down large parts of the internet."
]

categories = {"virus":[], "phishing":[] ,"DDos":[],
              "ransonware":[] ,"data breach":[]}

for incident in cybersecurity_incidents:
    for category in categories:
        if category in incident.lower():
            categories[category].append(incident)

for category , incidents in categories.items():
    print(f"\ncategory: {category.capitalize()}")
    print("\n".join(incidents) if incidents else "No incidents in this category.")
    
