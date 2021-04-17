from docx import Document
from frame.task_generator import TaskGenerator
from frame.task_generator import Pattern


import os
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class DocGenerator:
    def __init__(self, data):
        self.name = data['name']
        self.variant_count = int(data['variant_count'])
        self.patterns = []
        for pattern_id in data:
            if pattern_id.isdigit():
                pattern = data[pattern_id]
                if pattern != '0':
                    print(pattern_id, int(pattern))
                    self.patterns.append(Pattern(pattern_id, int(pattern)))



    def generate_document(self):
        print('генирируем')
        def generate_variant(variant):
            tasks = Document()
            tasks.add_heading(self.name + f' Вариант-{variant}', 0)
            number = 1
            for pattern in self.patterns:
                for _ in range(pattern.get_count()):
                    task_gen = TaskGenerator(pattern.get_pattern())
                    p = tasks.add_paragraph(f'№{number} ' + task_gen.get_text()[0])
                    p.alignment = 3
                    par.add_run(f'\n№{number} - ' + str(task_gen.get_text()[1]))
                    number += 1
            tasks.save('generated_documents/' + self.name + f'_вариант-{variant}.docx')
            # tasks.save(directory + '/' + self.name_edit.text() + f'_вариант-{variant}.docx')

        answers = Document()
        for variant in range(1, int(self.variant_count) + 1):
            answers.add_heading(f'Вариант-{variant}', 0)
            par = answers.add_paragraph()
            generate_variant(variant)
        answers.save('generated_documents/' + self.name + '_ответы.docx')
