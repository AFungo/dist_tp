# Add airline directory to sys.path
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent) + "/networking/airline")
sys.path.insert(0, str(Path(__file__).parent) + "/networking/ticket_service")

from classes.config_loader import ConfigLoader

# python3 run_airline_server.py -i resources/latam_airlines.json
def main():
    config_loader = ConfigLoader()
    config_loader.load_config_file()
    airline, server = config_loader.create_airline_server()
    server.start()
    
if __name__ == "__main__":
    main()    