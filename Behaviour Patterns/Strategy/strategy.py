from enum import Enum, auto
from abc import ABC

class OutputFormat(Enum):
    MARKDOWN    = auto()
    HTML        = auto()

class ListStrategy(ABC):
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        pass

class MarkdownListStrategy(ListStrategy):
    def add_list_item(self, buffer, item):
        buffer.append(f' * {item}\n')

class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append('<ul>\n')

    def end(self, buffer):
        buffer.append('</ul>\n')
    
    def add_list_item(self, buffer, item):
        buffer.append(f'  <li>{item}</li>\n')

class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.buffer         = []
        self.list_strategy  = list_strategy
    
    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()
    
    def clear(self):
        self.buffer.clear()
    
    def __str__(self):
        return ''.join(self.buffer)

def break_line():
    print('------------------------------------------')
    

if __name__ == '__main__':
    items = ['foo', 'bar', 'baz']
    break_line()

    tp = TextProcessor()
    tp.set_output_format(OutputFormat.MARKDOWN)
    tp.append_list(items)
    print(tp)
    break_line()

    tp.clear()
    tp.set_output_format(OutputFormat.HTML)
    tp.append_list(items)
    print(tp)
    break_line()
