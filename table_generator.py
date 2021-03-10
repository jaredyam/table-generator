import sublime
import sublime_plugin

from .csv_converter import csv2plaintext, csv2markdown, csv2latex


class TableGenerator(sublime_plugin.TextCommand):

    def run(self, edit, alignment, converter):
        assert len(self.view.sel()) == 1, sublime.error_message(
            'expected only one selection')

        selection = self.view.sel()[0]
        selection = (selection if self.view.substr(selection)
                     else sublime.Region(0, self.view.size()))

        rawdata = self.view.substr(selection)
        output = converter(
            rawdata, alignment=alignment if alignment else None) + '\n'
        self.view.replace(edit, selection, output)

    def input(self, args):
        if 'alignment' not in args:
            return AlignmentInputHandler()

    def input_description(self):
        return "Alignment Specifiers of Columns"


class PlainTableGeneratorCommand(TableGenerator):

    def run(self, edit, alignment):
        super(PlainTableGeneratorCommand, self).run(edit, alignment,
                                                    converter=csv2plaintext)


class MarkdownTableGeneratorCommand(TableGenerator):

    def run(self, edit, alignment):
        super(MarkdownTableGeneratorCommand, self).run(edit, alignment,
                                                       converter=csv2markdown)


class LatexTableGeneratorCommand(TableGenerator):

    def run(self, edit, alignment):
        super(LatexTableGeneratorCommand, self).run(edit, alignment,
                                                    converter=csv2latex)


class AlignmentInputHandler(sublime_plugin.TextInputHandler):

    def placeholder(self):
        return "'clr': render the 3-column table with 'center-left-right' alignment"

    def validate(self, alignment):
        return len(alignment) == 0 or (len(alignment) > 0 and set(alignment).issubset({'c', 'l', 'r'}))
