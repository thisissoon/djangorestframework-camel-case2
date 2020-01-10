# -*- coding: utf-8 -*-
from djangorestframework_camel_case2.settings import api_settings
from djangorestframework_camel_case2.util import camelize


class CamelCaseJSONRenderer(api_settings.RENDERER_CLASS):
    json_camelize = api_settings.JSON_CAMELIZE

    def render(self, data, *args, **kwargs):
        camelized = camelize(data, **self.json_camelize)
        return super(CamelCaseJSONRenderer, self).render(camelized, *args, **kwargs)
