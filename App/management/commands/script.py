import json
import csv
from django.core.management.base import BaseCommand
# Replace `your_app` with the actual name of your Django app and `YourModel` with the name of your model
from App.models import Restaurant, Item
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    help = 'Import data from CSV into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', help='The path to the CSV file')

    def handle(self, *args, **options):
        print('Deleting Previous Records Started')
        Restaurant.objects.all().delete()
        Item.objects.all().delete()
        print('Deleting Previous Records Done')
        csv_file = options['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists

            count_details = dict()

            for row in reader:

                print('Started saving row')

                full_deatails = json.loads(row[5]) if row[5] else dict()

                obj = dict()
                obj['name'] = row[1]
                obj['location'] = row[2]
                obj['lat'], obj['long'] = row[4].split(',')
                obj['cuisines'] = full_deatails.get('cuisines')
                obj['currency'] = full_deatails.get('currency')
                obj['price_range'] = full_deatails.get('price_range')
                obj['has_table_booking'] = full_deatails.get('has_table_booking')
                obj['is_delevering_now'] = full_deatails.get('is_delevering_now')
                obj['opentable_support'] = full_deatails.get('opentable_support')
                obj['has_online_delivery'] = full_deatails.get('has_online_delivery')
                obj['include_bogo_offer'] = full_deatails.get('include_bogo_offers')
                obj['average_cost_for_two'] = full_deatails.get('average_cost_for_two')
                obj['switch_to_order_menu'] = full_deatails.get('switch_to_order_menu')
                obj['is_book_form_web_view'] = full_deatails.get('is_book_form_web_view')
                obj['bookform_webview_url'] = full_deatails.get('book_form_web_view_url')
                obj['istable_reservation_supported'] = full_deatails.get('is_table_reservation_supported')
                
                try: 
                    dbEntry = Restaurant(**obj)
                    dbEntry.save()

                    items = json.loads(row[3])
                    for name, price in items.items():
                        try: 
                            itemEntry = Item(restaurant=dbEntry,item_name=name,item_price=float(price.strip()))
                            itemEntry.save()
                        except ValueError:
                            try:
                                itemEntry = Item(restaurant=dbEntry,item_name=name,item_price=float(price.strip().split(' ')[0]))
                                itemEntry.save()
                            except ValueError:
                                print('Error in item', dict({ 'name': name, 'price': price}))
                
                except ValidationError:
                    print('Error while loading row', row)
                print('Done saving row')                 
