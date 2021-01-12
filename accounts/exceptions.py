# from rest_framework.views import exception_handler


# def core_exception_handler(excep, context):

#     """ our core exception handler """

#     # first access the response of exception from drf
#     response = exception_handler(excep, context)

#     # all errors we'll be handling
#     handlers = {
#         'NotFound': _handle_not_found_error,
#         'ValidationError': _handle_generic_error,
#     }

#     # find the class of exception we got
#     exception_class = excep.__class__.__name__

#     if exception_class in handlers:

#         # if exception is one we're handling return response else let drf handle it
#         return handlers[exception_class](excep, context, response)

#     return response


# def _handle_generic_error(excep, context, response):
#     response.data = {
#         'errors': response.data
#     }
#     return response


# def _handle_not_found_error(excep, context, response):
#     view = context.get('view', None)

#     if view and hasattr(view, 'queryset') and view.queryset is not None:
#         error_key = view.queryset.model._meta.verbose_name

#         response.data = {
#             'errors': {
#                 error_key: response.data['detail']
#             }
#         }

#     else:
#         response = _handle_generic_error(excep, context, response)

#     return response
