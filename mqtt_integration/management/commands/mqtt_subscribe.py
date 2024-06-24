# mqtt_integration/management/commands/mqtt_subscribe.py
from django.core.management.base import BaseCommand
from mqtt_integration.subscribe import main as subscribe_main

from mqtt_integration import subscribe
class Command(BaseCommand):
    help = 'Subscribe to MQTT messages'

    def handle(self, *args, **options):
        subscribe.main()
