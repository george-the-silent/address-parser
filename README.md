# address-parser

Simple REST API for address parsing.

Send POST request to http://\<host>\:5000/parse-address

Request body example:
```json
{
  "address" : "Fialova 17 Pardubice 53009"
}
```

Response body example:
```json
{
    "raw_address": "Fialova 17 Pardubice 53009",
    "parsed_address": {
        "StreetNumber": "17",
        "StreetName": "fialova",
        "Unit": null,
        "Municipality": "pardubice",
        "Province": null,
        "PostalCode": "53009",
        "Orientation": null,
        "GeneralDelivery": null,
        "EOS": null
    },
    "parsed_address_components": [
        [
            "fialova",
            [
                "StreetName",
                1.0
            ]
        ],
        [
            "17",
            [
                "StreetNumber",
                0.9995
            ]
        ],
        [
            "pardubice",
            [
                "Municipality",
                0.9978
            ]
        ],
        [
            "53009",
            [
                "PostalCode",
                0.9997
            ]
        ]
    ]
}
```

Docker build:
```docker
docker build -t address-parser .

docker run -p 5000:5000 address-parser
```

