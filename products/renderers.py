# from rest_framework.renderers import JSONRenderer
# from rest_framework.utils.serializer_helpers import ReturnList
# import json


# class FinderJSONRenderer(JSONRenderer):
#     """ base renderer"""
#     charset = 'utf-8'
#     object_label = 'object'
#     object_name_plural = 'objects'

#     def render(self, data, media_type=None, renderer_context=None):
#         if isinstance(data, ReturnList):
#             _data = json.loads(
#                 super(FinderJSONRenderer, self).render(data).decode('utf-8'))
#             return json.dumps({self.object_label_plural: _data})
#         else:
#             errors = data.get('errors', None)

#         if errors is not None:
#             return super(FinderJSONRenderer, self).render(data)

#         return json.dumps({
#             self.object_label: data
#         })
