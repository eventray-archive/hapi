from pyramid.config         import Configurator
#from pyramid.authentication import AuthTktAuthenticationPolicy
#from pyramid.authorization  import ACLAuthorizationPolicy

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(
        settings = settings
    )

    config.include('hapi.routes')

    config.scan()

    return config.make_wsgi_app()

