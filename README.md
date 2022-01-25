# address-parser

Simple REST API for address parsing.

Send POST request to http://\<host>\:5000/parse-address

Request body example:
```json
{
  "address" : "Fialova 17 Pardubice 53009",
  "probability" : true
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
        {
            "name": "StreetName",
            "value": "fialova",
            "probability": 1.0
        },
        {
            "name": "StreetNumber",
            "value": "17",
            "probability": 0.9995
        },
        {
            "name": "Municipality",
            "value": "pardubice",
            "probability": 0.9978
        },
        {
            "name": "PostalCode",
            "value": "53009",
            "probability": 0.9997
        }
    ]
}
```

Docker build:
```docker
docker build -t address-parser .

docker run -p 5000:5000 address-parser
```

