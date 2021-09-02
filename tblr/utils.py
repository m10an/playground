from argparse import ArgumentParser
from typing import Type, get_type_hints, get_origin, Optional, Sequence, Any

__all__ = ['AnnotatedArgumentParser']


class AnnotatedArgumentParser(ArgumentParser):
    """
    >>> class AnnotatedNamespace: opt_string: str = "123"; string: str; number: int
    >>> parser = AnnotatedArgumentParser(namespace_class=AnnotatedNamespace)
    >>> parser.parse_args(['--string', 'abc', '--number', '123'])
    Namespace(opt_string='123', string='abc', number='123')
    """
    def __init__(self, namespace_class: Type, **kwargs):
        super().__init__(**kwargs)
        for flag, hint in get_type_hints(namespace_class).items():
            default_value = None
            if hasattr(namespace_class, flag):
                default_value = getattr(namespace_class, flag)
            self.add_argument(self.prefix_chars * 2 + flag,
                              type=get_origin(hint),
                              dest=flag,
                              default=default_value)

    def parse_args(self, args: Optional[Sequence[str]] = ...) -> Any:
        return super(AnnotatedArgumentParser, self).parse_args(args)
