def valid_data_from_test():
    return {
        "text": "New meme",
        "url": "https://img.rl0.ru/afisha/400x-/"
               "daily.afisha.ru/uploads/images/c/"
               "cf/ccf7a86d37854b4e911c67a6d10c024b.jpg",
        "tags": ["food", "restaurant"],
        "info": {
            "creator": "Andrey",
            "observer": "Eugene"
        }
    }


def data_from_mest_with_messing_field(field):
    data = valid_data_from_test()
    for field in data:
        del data[field]
        return data


def valid_data_for_put(mem_id):
    return {
        "id": mem_id,
        "text": "Update Meme",
        "url": "https://img-webcalypt.ru/uploads/admin/"
               "images/meme-templates/6rsHhdZv06ylAzFW6aMdlhWu45olnaUQ.jpg",
        "tags": ["New", "Cat"],
        "info": {
            "creator": "Andrey",
            "observer": "Eugene"
        }
    }
