from pyramid.view               import view_config
from pyramid.httpexceptions     import HTTPFound
from oauth2_provider.provider   import AuthorizationProvider

class AuthServer(AuthorizationProvider):
    should_force_ssl = False

    def verify_client_id(self, client_id):
        return True

    def verify_redirect_uri(self, client_id, redirect_uri):
        return True

    def verify_scope(self, scope):
        return True

    def authenticate_user(self):
        return True

    def save_auth_code(self, client_id, code, scope, redirect_uri):
        return True

    def save_auth_token(self, access_token, refresh_token):
        return True

    def verify_auth_code(self, code):
        return True

@view_config(
    route_name='hapi_callback'
    , request_method='POST'
    , renderer='json'
#    , permission = 'hapi_view_authorize'
)
def callback(request):
    prov = AuthServer()
    results = prov.redeem_code_for_token(dict(request.POST))

    return results

@view_config(
    route_name='hapi_authorize'
    , renderer='hapi:templates/authorize.mako'
#    , permission = 'hapi_view_authorize'
)
def authorize(request):
    prov = AuthServer()
    if request.method == 'GET':
        results = prov.verify_auth_request(request.url)

        if 'error' in results:
            return results
        else:
            return {}

    elif request.method == 'POST':
        results = prov.verify_auth_request(request.POST['url'])

        return HTTPFound(location=results['redirect_uri'])
