"""
Utils services

Will contain general function and classes related to databases that will be used in whole project

"""
import importlib

from django.db.models import QuerySet


def get_model(module, model_name):
    imported_module = importlib.import_module(module)
    _class = getattr(imported_module, model_name)
    return _class


def get_one_db_object(module, model_name, _select_related=None, _prefetch_related=None, **fields):
    """
    This will fetch ONE db object from the given module and model_name

    Parameters
    ----------
    module: module where the Model exists: str
    model_name : model name: str
    _select_related: Comma separated fields to fetch which are directly defined int the model: str
    _prefetch_related: Comma separated fields to fetch which are NOT directly defined int the model: str
    fields: all fields which you want to use in where clause: dict

    Returns
    -------
    Db Object

    Examples
    --------
    >>> from sql_services import get_one_db_object
    >>> get_one_db_object('posts.models', 'Posts', **{'id': 1})
    <Posts: Posts object>

    OR

    >>> get_one_db_object('posts.models', 'Posts', _prefetch_related='authors, categories', **{'id': 1})
    <Posts: Posts object>

    """
    return get_model(module, model_name).objects.select_related(
        *(i.strip() for i in _select_related.split(",") if i) if _select_related else ()
    ).prefetch_related(
        *(i.strip() for i in _prefetch_related.split(",") if i) if _prefetch_related else ()
    ).get(**fields)


def get_many_db_object(module, model_name, _select_related=None, _prefetch_related=None, **fields):
    """
    This will fetch MANY db object from the given module and model_name

    Parameters
    ----------
    module: module where the Model exists: str
    model_name : model name: str
    _select_related: Comma separated fields to fetch which are directly defined int the model: str
    _prefetch_related: Comma separated fields to fetch which are NOT directly defined int the model: str
    fields: all fields which you want to use in where clause: dict

    Returns
    -------
    QuerySet

    Examples
    --------
    >>> from sql_services import get_one_db_object
    >>> get_one_db_object('posts.models', 'Posts', **{'id': 1})
    <QuerySet [<Posts: Posts object>]>
    OR

    >>> get_many_db_object('posts.models', 'Posts', _prefetch_related='authors, categories', **{'id': 1})
    <QuerySet [<Posts: Posts object>]>

    """
    return get_model(module, model_name).objects.select_related(
        *(i.strip() for i in _select_related.split(",") if i) if _select_related else ()
    ).prefetch_related(
        *(i.strip() for i in _prefetch_related.split(",") if i) if _prefetch_related else ()
    ).filter(**fields)


def set_one_db_object(instance, **fields):
    """
    This will save in db using djagno save() method

    Parameters
    ----------
    instance: Model instance
    fields: Fields to save: dict
    """
    for key, value in fields:
        setattr(instance, key, value)
    instance.save()


def set_many_db_object(instances, **fields):
    """
    This will save many db instance in db.

    Parameters
    ----------
    instances: QuerySet
    fields: Fields to save: dict
    """
    if isinstance(instances, QuerySet):
        instances.update(**fields)
    elif isinstance(instances, (list, tuple, set)):
        for instance in instances:
            set_one_db_object(instance, **fields)
