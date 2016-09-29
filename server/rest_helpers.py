from flask_restful.reqparse import RequestParser


class ApiReqParser(RequestParser):
    """
    Subclass of RequestParser to set some defaults, DRY up usages.
    """

    def __init__(self, **kwargs):
        # Enable trim
        super(ApiReqParser, self).__init__(
            bundle_errors=True, trim=True, **kwargs)

    def add_argument(self, *args, **kwargs):
        # Default some arguments
        if 'case_sensitive' not in kwargs:
            kwargs['case_sensitive'] = False
        if 'nullable' not in kwargs:
            kwargs['nullable'] = False
        if 'required' not in kwargs:
            kwargs['required'] = True
        return super(ApiReqParser, self).add_argument(*args, **kwargs)

    def parse_args(self, req=None, strict=True):
        return super(ApiReqParser, self).parse_args(req, strict)
