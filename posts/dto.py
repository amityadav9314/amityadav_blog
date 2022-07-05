class PostDTO(object):
    """
    This class acts as setter and getter. Here it is controlled what to pass to network
    and what not to pass
    """
    def __init__(self, post_obj, exclude=None):
        # Setting attribute for each field
        if exclude is None:
            exclude = []
        for key, value in post_obj.__dict__.items():
            if not key.startswith("__") and (key is not None and key not in exclude):
                setattr(self, key, value)

        # Now setting attribute for foreign, one to one, and/or m2m fields
        for key, value in self.__dict__.get("_prefetched_objects_cache").items():
            if not key.startswith("__") or not key.startswith("_") and (key is not None and key not in exclude):
                setattr(self, key, value)

        # Set url
        setattr(self, 'url', post_obj.get_absolute_url())
