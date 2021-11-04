story = {
    "title": "Het verhaal over een vluchteling",
    "story": {
        "1": {
            "title": "Hassan moet vluchten omdat het regime van Assad zijn vrijheid afneemt.",
            "options": [
                {
                    "text": "Vlucht met het vliegtuig naar Turkije",
                    "target": "2"
                },
                {
                    "text": "Vlucht te voet naar Libanon",
                    "target": "-"
                },
                {
                    "text": "Vlucht met de boot naar Cyprus",
                    "target": "-"
                }
            ]
        },
        "2": {
            "title": "Je hebt gekozen om naar Turkije te vluchten, je familie kan alleen niet mee in het vliegtuig, "
                     "laat je ze achter of kies je toch liever een andere optie?",
            "options": [
                {
                    "text": "Ik vlucht naar Turkije en ik laat mijn familie achter",
                    "target": "S1"
                },
                {
                    "text": "Ik kies liever een andere vlucht optie.",
                    "target": "1"
                }
            ],
            "substories": {
                "1": {
                    "title": "Je laat je familie achter en vertrekt met het vliegtuig naar Turkije, wanneer je bij "
                             "het vliegveld aankomt bied een mysterieuze man je een smokkelroute aan naar Rusland.",
                    "options": [
                        {
                            "text": "Ik loop door en doe alsof ik de man niet hoorde.",
                            "target": "-"
                        },
                        {
                            "text": "Ik accepteer de man zijn aanbod.",
                            "target": "-"
                        }
                    ]
                }
            }
        },
        "3": {
            "title": "Je hebt gekozen om te voet te vluchten naar Libanon, je oom Ali heeft plek in zijn busje maar "
                     "je hebt hem gespot met het regime en verdenkt hem van samenwerking met het regime, ga je met "
                     "hem mee?",
            "options": [
                {
                    "text": "Ja ik vertrouw hem wel volledig en ik ga mee in het busje.",
                    "target": "-"
                },
                {
                    "text": "Ik ga liever te voet.",
                    "target": "5"
                }
            ]
        },
        "4": {
            "title": "Je hebt gekozen om met de boot naar Cyprus te vluchten, alleen de man met de boot is na 3 uur "
                     "wachten nog steeds niet op de afgesproken plek.",
            "options": [
                {
                    "text": "Ik wacht nog even tot hij komt.",
                    "target": "-"
                },
                {
                    "text": "Ik kies liever een andere optie.",
                    "target": "1"
                }
            ]
        }
    }
}
