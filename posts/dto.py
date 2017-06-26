class PostDTO(object):
    def __init__(self, post_obj):
        # Setting attribute for each field
        for key, value in post_obj.__dict__.items():
            if not key.startswith("__"):
                setattr(self, key, value)

        # Now setting attribute for foreign, one to one, and/or m2m fields
        for key, value in self.__dict__.get("_prefetched_objects_cache").items():
            if not key.startswith("__") or not key.startswith("_"):
                setattr(self, key, value)

        # Set url
        setattr(self, 'url', post_obj.get_absolute_url())


class PostsDTO(object):
    pass
