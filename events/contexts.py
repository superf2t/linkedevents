"""
Most of the types and properties used are found from schema.org
but customized properties and types should be defined in @context
to add semantic spice in JSONs.
"""
from events.serializers import utils

LINKED_EVENTS_SCHEMA_URL = "http://example.com/le/"


def create_context(klass):
    klass.jsonld_context = {
        "@vocab": "http://schema.org/",
        "linkedEvents": LINKED_EVENTS_SCHEMA_URL
    }
    for name in klass._meta.get_all_field_names():
        name = utils.convert_to_camelcase(name)
        if name in CONTEXTS:
            klass.jsonld_context[name] = CONTEXTS[name]

CONTEXTS = {
    "id": {
        "@id": "linkedEvents:id",
        "@type": "Integer"
    },
    "name": {
        "@id": "name",
        "@container": "@language"
    },
    "description": {
        "@id": "description",
        "@container": "@language"
    },
    "originId": {
        "@id": "linkedEvents:originId",
        "@type": "Text"
    },
    "targetGroup": {
        "@id": "linkedEvents:targetGroup",
        "@type": "Text"
    },
    "slug": {
        "@id": "linkedEvents:slug",
        "@type": "Text"
    },
    "customFields": {
        "@id": "linkedEvents:customFields",
        "@container": "@index"
    }
}