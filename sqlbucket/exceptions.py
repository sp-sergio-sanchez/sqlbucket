class ProjectNotFound(Exception):
    pass


class ConnectionNotFound(Exception):
    pass


class GroupNotFound(KeyError):
    pass


class OrderNotInRightFormat(TypeError):
    pass