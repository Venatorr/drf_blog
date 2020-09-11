from rest_framework.routers import Route, SimpleRouter


class GetPostOnlyRouter(SimpleRouter):
    """
    Роутер, позволяющий выполнять только GET и POST
    """
    routes = [
        Route(
            url=r'^{prefix}{trailing_slash}$',
            mapping={
                'get': 'list',
                'post': 'create'
            },
            name='{basename}-list',
            detail=False,
            initkwargs={'suffix': 'List'}
        )
    ]
