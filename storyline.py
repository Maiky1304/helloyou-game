story = {
    "story": {
        "1": {
            "title": "Er is oorlog in Syrië en je bent genoodzaakt te vertrekken. Wat doe je?",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Je kiest ervoor om te vluchten naar een ander land.",
                    "target": "2"
                },
                {
                    "text": "Je kiest ervoor om thuis te blijven en niks te doen.",
                    "target": "3"
                },
                {
                    "text": "Je sluit je aan bij het verzet.",
                    "target": "4"
                }
            ]
        },
        "2": {
            "title": "Je wordt gezocht en je moet een goede keuze maken, wat doe je?",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Je geeft je over.",
                    "target": "4"
                },
                {
                    "text": "Je vlucht",
                    "target": "5"
                }
            ]
        },
        "3": {
            "title": "Je spreekt je mening uit over wat je hier allemaal van vind en wordt gezocht hiervoor, "
                     "wat doe je?",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Je geeft je over.",
                    "target": "4"
                },
                {
                    "text": "Je vlucht",
                    "target": "5"
                }
            ]
        },
        "4": {
            "title": "Je bent dood gegaan!",
            "type": "STORY",
            "close_app": True
        },
        "5": {
            "title": "Je hebt verschillende opties om te vluchten welke keuze maak je?",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Vlucht met het vliegtuig naar Turkije",
                    "target": "6"
                },
                {
                    "text": "Vlucht te voet naar Libanon",
                    "target": "S1"
                },
                {
                    "text": "Vlucht met de boot naar Cyprus",
                    "target": "S2"
                }
            ],
            "substories": {
                "1": {
                    "title": "Op de weg naar Libanon wordt je opgepakt en dood gemaakt.",
                    "type": "STORY",
                    "close_app": True
                },
                "2": {
                    "title": "Je bent veilig aangekomen op Cyprus",
                    "type": "STORY",
                    "target": "7"
                }
            }
        },
        "6": {
            "title": "Op het vliegveld wordt heftig gecontroleerd ga je toch liever voor een andere optie? Of durf je "
                     "het te proberen?",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Ik durf het te proberen",
                    "target": "S1"
                },
                {
                    "text": "Ik ga toch liever op een andere manier vluchten",
                    "target": "5"
                }
            ],
            "substories": {
                "1": {
                    "title": "Je komt aan op het vliegveld in Turkije...",
                    "type": "STORY",
                    "target": "7"
                }
            }
        },
        "7": {
            "title": "Je krijgt de mogelijkheid om naar Nederland te vliegen zonder paspoort of papieren.",
            "type": "STORY",
            "target": "S1",
            "substories": {
                "1": {
                    "title": "Je komt velig aan in Nederland je verteld de maraschaussee dat je illegaal naar "
                             "Nederland bent gekomen en ze helpen jou met het bellen voor iemand die je kan helpen "
                             "met asiel.",
                    "type": "STORY",
                    "target": "8"
                }
            }
        },
        "8": {
            "title": "Je hebt asiel gekregen en moet nu gaan solliciteren voor een baan.",
            "type": "QUESTION",
            "options": [
                {
                    "text": "Postbezorger",
                    "target": "S1"
                },
                {
                    "text": "Kassamedewerker bij de Albert Heijn",
                    "target": "S1"
                },
                {
                    "text": "Hoge pief/chef van een fabriek",
                    "target": "S1"
                }
            ],
            "substories": {
                "1": {
                    "title": "Je woont heel veilig en samen met je familie.",
                    "type": "STORY",
                    "close_app": True
                }
            }
        },
    }
}
