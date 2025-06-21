import os
import json
from django.core.management.base import BaseCommand, CommandError
from quiz.models import Quiz, Section, Question

class Command(BaseCommand):
    help = 'Import questions from a JSON file. Usage: python manage.py import_questions <json_file>'

    def add_arguments(self, parser):
        parser.add_argument('json_file', nargs='?', type=str, help='Path to the questions JSON file.')

    def handle(self, *args, **options):
        json_file = options['json_file']

        if not json_file:
            self.stdout.write(self.style.ERROR(
                'Usage: python manage.py import_questions <json_file>\n'
                'You must provide the path to the questions JSON file.'
            ))
            return

        if not os.path.isfile(json_file):
            self.stdout.write(self.style.ERROR(f"File not found: {json_file}"))
            return

        with open(json_file, encoding='utf-8') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                raise CommandError(f"Invalid JSON: {e}")

        quiz, _ = Quiz.objects.get_or_create(title="Internet Quiz", description="A self-assessment on digital life.")
        sections = {}

        for q in data:
            section_name = q.get('section', 'Default')
            if section_name not in sections:
                section, _ = Section.objects.get_or_create(quiz=quiz, name=section_name)
                sections[section_name] = section
            Question.objects.create(section=sections[section_name], text=q['text'])

        self.stdout.write(self.style.SUCCESS("Questions imported!"))
