class MyMixin(object):
    mixin_properties = ''

    def get_properties(self):
        return self.mixin_properties.upper()

    @staticmethod
    def get_upper(s):
        if isinstance(s, str):
            return s.upper()
        else:
            return s.title.upper()
