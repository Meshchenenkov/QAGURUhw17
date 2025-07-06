#схемагенератор https://www.liquid-technologies.com/online-json-to-schema-converter
post_users = { #изУрока
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "createdAt",
        "job",
        "name"
    ]
}


post_register_unsuccessful = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "error": {
      "type": "string"
    }
  },
  "required": [
    "error"
  ]
}


post_create = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "id",
    "createdAt"
  ]
}


get_single_user_not_found = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object"
}
