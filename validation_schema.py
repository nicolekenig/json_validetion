from enum import Enum


class Schema(Enum):
    people = {"type": "object",
              "properties": {
                  "name": {"type": "string"},
                  "suname": {"type": "string"},
                  "age": {"type": "number", "minimum":0},
                  "family_member": {"type": "string", "enum": ["kid", "parent"]},
              },
              }
    families = {"type": "object",
                "properties": {
                    "suname": {"type": "string"},
                    "has_kids": {"type": "boolean"},
                    "parents": {"type": "list"},
                    "kids": {"type": "list"},
                    "kids_num": {"type": "number", "minimum":0},
                },
                }
