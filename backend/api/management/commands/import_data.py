import csv, os

from django.core.management.base import BaseCommand
from api.models import Pokemon

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def handle(self, *args, **options):
        # Specify the path to your CSV file
        script_path = os.path.abspath(__file__)
        backend_directory = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(script_path))))
        csv_file = os.path.join(backend_directory, 'csv_data', 'pokemon.csv')

        # Clear all data from the table
        Pokemon.objects.all().delete()

        # Import data from the CSV
        self.import_data_from_csv(csv_file)

        self.stdout.write(self.style.SUCCESS('Data import completed.'))

    @staticmethod
    def import_data_from_csv(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            csv_data = csv.DictReader(file)
            for row in csv_data:

                # Replace empty fields with None to avoid detecting them as empty string ''
                for key, value in row.items():
                    if not value:
                        row[key] = None

                try:
                    Pokemon.objects.create(
                        attack=row['attack'],
                        classification=row['classification'],
                        defense=row['defense'],
                        height_m=row['height_m'],
                        hp=row['hp'],
                        japanese_name=row['japanese_name'],
                        name=row['name'],
                        pokedex_number=row['pokedex_number'],
                        sp_attack=row['sp_attack'],
                        sp_defense=row['sp_defense'],
                        speed=row['speed'],
                        type1=row['type1'],
                        type2=row['type2'],
                        weight_kg=row['weight_kg'],
                        generation=row['generation'],
                        is_legendary=row['is_legendary'],
                    )
                except Exception as e:
                    print(f"An error occurred: {str(e)}")
