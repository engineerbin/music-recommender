import csv
import chardet
from django.core.management.base import BaseCommand
from recommend.models import Music

class Command(BaseCommand):
    help = 'Import data from a CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        # Detect the encoding of the CSV file
        with open(csv_file, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
        
        # Detect the delimiter and header
        with open(csv_file, 'r', encoding=encoding) as f:
            sample = f.read(1024)
            sniffer = csv.Sniffer()
            has_header = sniffer.has_header(sample)
            delimiter = sniffer.sniff(sample).delimiter
        
        def clean_int(value):
            return int(value.replace(',', '')) if value else 0

        def clean_float(value):
            return float(value.replace(',', '')) if value else 0.0

        # Read and import the CSV data
        with open(csv_file, newline='', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                next(reader)  # Skip the header row
            for row in reader:
                try:
                    print(f"Processing row: {row}")  # Print the current row for debugging
                    Music.objects.create(
                        track_name=row[0],
                        artists_name=row[1],
                        artist_count=clean_int(row[2]),
                        released_year=clean_int(row[3]),
                        released_month=clean_int(row[4]),
                        released_day=clean_int(row[5]),
                        in_spotify_playlists=clean_int(row[6]),
                        in_spotify_charts=clean_int(row[7]),
                        streams=clean_int(row[8]),
                        in_apple_playlists=clean_int(row[9]),
                        in_apple_charts=clean_int(row[10]),
                        in_deezer_playlists=clean_int(row[11]),
                        in_deezer_charts=clean_int(row[12]),
                        in_shazam_charts=clean_int(row[13]),
                        bpm=clean_int(row[14]),
                        key_name=row[15],  # Use key_name here
                        mode=row[16],
                        danceability=clean_float(row[17]),
                        valence=clean_float(row[18]),
                        energy=clean_float(row[19]),
                        acousticness=clean_float(row[20]),
                        instrumentalness=clean_float(row[21]),
                        liveness=clean_float(row[22]),
                        speechiness=clean_float(row[23]),
                    )
                except Exception as e:
                    print(f"Error processing row: {row}. Error: {e}")
        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
