import sys
import pathlib
import csv
import jinja2

class CsvToJinja2:
    
    def main(self, template_str, src, delimiter = ','):
        template = self.load_template(template_str)
        src_rows = self.load_src(src, delimiter)
        rendered = self.render(template, src_rows)
        print(rendered)
    
    def load_template(self, template_str):
        template_path = pathlib.Path(template_str)
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader(
            template_path.parent, encoding="utf8"))
        return environment.get_template(template_path.name)

    def render(self, template, src_rows):
        return template.render(rows=src_rows)

    def load_src(self, src, delimiter):
        with open(src, encoding="utf8") as csvsrc:
            rows = csv.reader(csvsrc, delimiter=delimiter)
            return [row for row in rows]

if __name__ == '__main__':
    CsvToJinja2().main(sys.argv[1], sys.argv[2])
