dc1 = {
    "name": "india",
    "type": "country",
    "states": [{
        "Andhra": {
            "population": "2 millions",
            "districts": [{
                "EG": [{
                    "kkd": {
                        "smart_city": True,
                        "area": "200sqkms"
                    },
                    "rjy": {
                        "smart_city": False,
                        "area": "220sqkms"
                    },
                    "others":[
                        "samalkot",
                        "pithaputam"
                    ]}
                ],

                "WG": [
                    "bhimavaram",
                    "eluru"
                ]}
            ]
        },
        "Karnataka": {
            "population": "5 millions",
            "cities": [
                "bangalore",
                "mysore"
            ]
        }
    }]
}


print(dc1)

dc2 = {
    "name": "india",
    "type": "country",
    "states": [{
        "Andhra": {
            "population": "2 millions",
            "districts": [{
                "EG": [{
                    "kkd": {
                        "smart_city": True,
                        "area": "200sqkms"
                    },
                    "rjy": {
                        "smart_city": False,
                        "area": "220sqkms"
                    },
                    "others":[
                        "samalkot",
                        "pithaputam"
                    ]}
                ],

                "WG": [
                    "bhimavaram",
                    "eluru",
                    "ongole"
                ]}
            ]
        },
        "Karnataka": {
            "population": "5 millions",
            "cities": [
                "bangalore",
                "mysore"
            ]
        }
    }]
}
print(dc2)
print(dc1==dc2)