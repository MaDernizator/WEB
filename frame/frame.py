from docx import Document
from task_generator import TaskGenerator

import os
import sys

sys.excepthook = lambda *a: sys.__excepthook__(*a)


class DocGenerator:
    def __init__(self, name, variant_count, patterns):
        self.name, self.variant_count, self.patterns = name, variant_count, patterns

    def generate_document(self):
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
