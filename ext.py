class KeepType(type):
    def __new__(cls, class_name, class_bases, class_dict):
        class_count = len(class_bases)
        if class_count!=1:
            raise TypeError(f'`{cls.__name__}` should inherit exactly 1 type, got {class_count}: `{class_bases!r}`')
        klass = class_bases[0]
        if not issubclass(klass, object):
            raise TypeError(f'`{cls.__name__}` can inherit only types, got `{klass!r}`')
        for name, value in class_dict.items():
            setattr(klass,name,value)
        return klass
