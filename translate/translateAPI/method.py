from translate.models import *


def translate(obj, language):
    tran_obj = TranslateField.objects.filter(status=True, tran_field_pk__trans_language=language).values(
        'trans_field',
        'tran_field_pk__trans_value',
    )
    field_to_value = {}
    for tran in tran_obj:
        field_to_value[tran['trans_field']] = tran['tran_field_pk__trans_value']
    for key, value in obj.items():
        obj[key] = field_to_value[key]
    return obj

