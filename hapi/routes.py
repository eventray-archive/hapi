def includeme(config):
    config.add_route('hapi_authorize', '/authorize')
    config.add_route('hapi_callback', '/token')
