import sys
import json
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QLabel, QFormLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from io import BytesIO

flower_data = {
  "flowers": [
    {
      "name": "Rose",
      "color": ["Red", "Pink", "White", "Yellow", "Orange"],
      "pollinators": ["Bees", "Butterflies", "Hummingbirds"],
      "geographicRegions": ["Worldwide", "North America", "Europe", "Asia"],
      "physicalFeatures": {
        "height": "1-2 meters",
        "flowerSize": "5-10 cm",
        "leafShape": "Compound",
        "stem": "Thorny"
      }
    },
    {
      "name": "Tulip",
      "color": ["Red", "Pink", "Yellow", "Purple", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia"],
      "physicalFeatures": {
        "height": "10-60 cm",
        "flowerSize": "5-7 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Lily",
      "color": ["White", "Pink", "Red", "Orange", "Yellow"],
      "pollinators": ["Bees", "Butterflies", "Hummingbirds"],
      "geographicRegions": ["North America", "Europe", "Asia"],
      "physicalFeatures": {
        "height": "60-180 cm",
        "flowerSize": "10-20 cm",
        "leafShape": "Lance-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Anemone",
      "color": ["Red", "Pink", "White", "Blue", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "15-60 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Palmate",
        "stem": "Smooth"
      }
    },
    {
      "name": "Amaryllis",
      "color": ["Red", "Pink", "White", "Orange"],
      "pollinators": ["Bees"],
      "geographicRegions": ["South America", "Africa"],
      "physicalFeatures": {
        "height": "45-60 cm",
        "flowerSize": "10-15 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Aster",
      "color": ["Purple", "Pink", "Blue", "White", "Red"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "30-90 cm",
        "flowerSize": "2-4 cm",
        "leafShape": "Lance-shaped",
        "stem": "Hairy"
      }
    },
    {
      "name": "Azalea",
      "color": ["Red", "Pink", "White", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Asia", "North America"],
      "physicalFeatures": {
        "height": "1-3 meters",
        "flowerSize": "5-8 cm",
        "leafShape": "Elliptical",
        "stem": "Woody"
      }
    },
    {
      "name": "Baby's Breath",
      "color": ["White", "Pink"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "1-2 cm",
        "leafShape": "Linear",
        "stem": "Branching"
      }
    },
    {
      "name": "Begonia",
      "color": ["Red", "Pink", "White", "Orange"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["South America", "Africa", "Asia"],
      "physicalFeatures": {
        "height": "15-45 cm",
        "flowerSize": "3-5 cm",
        "leafShape": "Round or Heart-shaped",
        "stem": "Fleshy"
      }
    },
    {
      "name": "Bellflower",
      "color": ["Blue", "Purple", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "North America"],
      "physicalFeatures": {
        "height": "30-90 cm",
        "flowerSize": "2-4 cm",
        "leafShape": "Oval",
        "stem": "Smooth"
      }
    },
    {
      "name": "Bergamot",
      "color": ["Purple", "Pink", "Red"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "60-90 cm",
        "flowerSize": "2-3 cm",
        "leafShape": "Ovate",
        "stem": "Square"
      }
    },
    {
      "name": "Bird of Paradise",
      "color": ["Orange", "Blue", "Green"],
      "pollinators": ["Birds"],
      "geographicRegions": ["South Africa"],
      "physicalFeatures": {
        "height": "1.5-2 meters",
        "flowerSize": "20-30 cm",
        "leafShape": "Large, Banana-like",
        "stem": "Thick and sturdy"
      }
    },
    {
      "name": "Bluebell",
      "color": ["Blue", "Purple"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe"],
      "physicalFeatures": {
        "height": "15-30 cm",
        "flowerSize": "1-2 cm",
        "leafShape": "Linear",
        "stem": "Hairy"
      }
    },
    {
      "name": "Bottlebrush",
      "color": ["Red", "Pink"],
      "pollinators": ["Bees", "Birds"],
      "geographicRegions": ["Australia"],
      "physicalFeatures": {
        "height": "1-3 meters",
        "flowerSize": "10-15 cm",
        "leafShape": "Linear",
        "stem": "Woody"
      }
    },
    {
      "name": "Buttercup",
      "color": ["Yellow", "White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "10-30 cm",
        "flowerSize": "2-5 cm",
        "leafShape": "Heart-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Camellia",
      "color": ["Red", "Pink", "White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Asia"],
      "physicalFeatures": {
        "height": "1-3 meters",
        "flowerSize": "5-10 cm",
        "leafShape": "Oval",
        "stem": "Woody"
      }
    },
    {
      "name": "Carnation",
      "color": ["Red", "Pink", "White", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "4-6 cm",
        "leafShape": "Lance-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Chrysanthemum",
      "color": ["Yellow", "Red", "White", "Purple", "Pink"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Asia", "Europe", "North America"],
      "physicalFeatures": {
        "height": "30-90 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Lobed",
        "stem": "Smooth"
      }
    },
    {
      "name": "Columbine",
      "color": ["Blue", "Purple", "Red", "White"],
      "pollinators": ["Bees", "Hummingbirds"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "3-5 cm",
        "leafShape": "Palmate",
        "stem": "Smooth"
      }
    },
    {
      "name": "Clover",
      "color": ["Red", "White", "Pink"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Worldwide"],
      "physicalFeatures": {
        "height": "10-30 cm",
        "flowerSize": "1-2 cm",
        "leafShape": "Trifoliate",
        "stem": "Hairy"
      }
    },
    {
      "name": "Crocus",
      "color": ["Purple", "Yellow", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia"],
      "physicalFeatures": {
        "height": "10-15 cm",
        "flowerSize": "3-5 cm",
        "leafShape": "Linear",
        "stem": "No stem (grows from corm)"
      }
    },
    {
      "name": "Daisy",
      "color": ["White", "Yellow", "Pink"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Worldwide"],
      "physicalFeatures": {
        "height": "10-30 cm",
        "flowerSize": "3-5 cm",
        "leafShape": "Lance-shaped",
        "stem": "Hairy"
      }
    },
    {
      "name": "Dahlia",
      "color": ["Red", "Pink", "Yellow", "Purple", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Central America", "Mexico"],
      "physicalFeatures": {
        "height": "60-180 cm",
        "flowerSize": "10-20 cm",
        "leafShape": "Lobed",
        "stem": "Smooth"
      }
    },
    {
      "name": "Daffodil",
      "color": ["Yellow", "White", "Orange"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe", "North America"],
      "physicalFeatures": {
        "height": "30-45 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Delphinium",
      "color": ["Blue", "Purple", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "90-180 cm",
        "flowerSize": "2-5 cm",
        "leafShape": "Lobed",
        "stem": "Smooth"
      }
    },
    {
      "name": "Edelweiss",
      "color": ["White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Alps", "Carpathians"],
      "physicalFeatures": {
        "height": "10-30 cm",
        "flowerSize": "2-4 cm",
        "leafShape": "Woolly",
        "stem": "Hairy"
      }
    },
    {
      "name": "Freesia",
      "color": ["Yellow", "White", "Pink", "Purple", "Red"],
      "pollinators": ["Bees"],
      "geographicRegions": ["South Africa"],
      "physicalFeatures": {
        "height": "30-45 cm",
        "flowerSize": "4-6 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Gardenia",
      "color": ["White", "Cream"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Asia", "Africa"],
      "physicalFeatures": {
        "height": "1-2 meters",
        "flowerSize": "5-10 cm",
        "leafShape": "Oval",
        "stem": "Woody"
      }
    },
    {
      "name": "Geranium",
      "color": ["Red", "Pink", "White", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["South Africa", "Europe"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "2-4 cm",
        "leafShape": "Rounded",
        "stem": "Hairy"
      }
    },
    {
      "name": "Gerbera Daisy",
      "color": ["Red", "Pink", "Yellow", "White", "Orange"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["South Africa"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "7-12 cm",
        "leafShape": "Lance-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Gladiolus",
      "color": ["Red", "Pink", "Yellow", "White", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Africa", "Europe"],
      "physicalFeatures": {
        "height": "60-180 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Sword-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Gloxinia",
      "color": ["Red", "Pink", "Purple", "White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["South America"],
      "physicalFeatures": {
        "height": "15-30 cm",
        "flowerSize": "5-8 cm",
        "leafShape": "Rounded",
        "stem": "Fleshy"
      }
    },
    {
      "name": "Hibiscus",
      "color": ["Red", "Pink", "White", "Yellow", "Orange"],
      "pollinators": ["Bees", "Hummingbirds"],
      "geographicRegions": ["Tropical regions worldwide"],
      "physicalFeatures": {
        "height": "1-3 meters",
        "flowerSize": "10-15 cm",
        "leafShape": "Oval",
        "stem": "Woody"
      }
    },
    {
      "name": "Hollyhock",
      "color": ["Red", "Pink", "White", "Purple", "Yellow"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia"],
      "physicalFeatures": {
        "height": "90-180 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Heart-shaped",
        "stem": "Hairy"
      }
    },
    {
      "name": "Hyacinth",
      "color": ["Purple", "Pink", "Blue", "White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe", "Asia"],
      "physicalFeatures": {
        "height": "15-30 cm",
        "flowerSize": "2-5 cm",
        "leafShape": "Linear",
        "stem": "No stem (grows from bulb)"
      }
    },
    {
      "name": "Hydrangea",
      "color": ["Blue", "Pink", "White", "Purple"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Asia", "North America"],
      "physicalFeatures": {
        "height": "1-2 meters",
        "flowerSize": "10-20 cm",
        "leafShape": "Oval",
        "stem": "Woody"
      }
    },
    {
      "name": "Iris",
      "color": ["Purple", "Blue", "White", "Yellow"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "30-90 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Sword-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Jasmine",
      "color": ["White", "Yellow"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Asia", "Europe", "North America"],
      "physicalFeatures": {
        "height": "1-4 meters",
        "flowerSize": "1-2 cm",
        "leafShape": "Oval",
        "stem": "Woody"
      }
    },
    {
      "name": "Lady's Slipper",
      "color": ["Pink", "White", "Yellow"],
      "pollinators": ["Bees"],
      "geographicRegions": ["North America", "Europe"],
      "physicalFeatures": {
        "height": "20-30 cm",
        "flowerSize": "4-6 cm",
        "leafShape": "Oval",
        "stem": "Hairy"
      }
    },
    {
      "name": "Lavender",
      "color": ["Purple", "Blue"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Mediterranean", "North America"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "1-2 cm",
        "leafShape": "Linear",
        "stem": "Woody"
      }
    },
    {
      "name": "Lilac",
      "color": ["Purple", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "North America"],
      "physicalFeatures": {
        "height": "2-5 meters",
        "flowerSize": "5-10 cm",
        "leafShape": "Heart-shaped",
        "stem": "Woody"
      }
    },
    {
      "name": "Lily",
      "color": ["White", "Yellow", "Pink", "Red", "Orange"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "60-120 cm",
        "flowerSize": "5-15 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Lotus",
      "color": ["White", "Pink", "Red"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Asia"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "10-20 cm",
        "leafShape": "Round",
        "stem": "No stem (grows from rhizome)"
      }
    },
    {
      "name": "Marigold",
      "color": ["Orange", "Yellow", "Red"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["North America", "South America", "Europe"],
      "physicalFeatures": {
        "height": "30-60 cm",
        "flowerSize": "3-5 cm",
        "leafShape": "Lobed",
        "stem": "Hairy"
      }
    },
    {
      "name": "Orchid",
      "color": ["White", "Purple", "Pink", "Yellow"],
      "pollinators": ["Bees", "Butterflies", "Hummingbirds"],
      "geographicRegions": ["Tropical and subtropical regions worldwide"],
      "physicalFeatures": {
        "height": "15-90 cm",
        "flowerSize": "2-5 cm",
        "leafShape": "Oval",
        "stem": "Fleshy"
      }
    },
    {
      "name": "Pansy",
      "color": ["Purple", "Yellow", "White", "Red"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe", "North America"],
      "physicalFeatures": {
        "height": "15-30 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Heart-shaped",
        "stem": "Smooth"
      }
    },
    {
      "name": "Peony",
      "color": ["Red", "Pink", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "60-90 cm",
        "flowerSize": "10-20 cm",
        "leafShape": "Lobed",
        "stem": "Hairy"
      }
    },
    {
      "name": "Petunia",
      "color": ["Purple", "Pink", "White", "Red"],
      "pollinators": ["Bees"],
      "geographicRegions": ["South America"],
      "physicalFeatures": {
        "height": "15-30 cm",
        "flowerSize": "5-8 cm",
        "leafShape": "Oval",
        "stem": "Smooth"
      }
    },
    {
      "name": "Rose",
      "color": ["Red", "Pink", "White", "Yellow", "Orange"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["Worldwide"],
      "physicalFeatures": {
        "height": "30 cm - 3 meters",
        "flowerSize": "5-15 cm",
        "leafShape": "Oval",
        "stem": "Thorny"
      }
    },
    {
      "name": "Sunflower",
      "color": ["Yellow", "Orange"],
      "pollinators": ["Bees", "Birds"],
      "geographicRegions": ["North America", "South America"],
      "physicalFeatures": {
        "height": "1-3 meters",
        "flowerSize": "15-30 cm",
        "leafShape": "Heart-shaped",
        "stem": "Hairy"
      }
    },
    {
      "name": "Tulip",
      "color": ["Red", "Yellow", "Pink", "White"],
      "pollinators": ["Bees"],
      "geographicRegions": ["Europe", "Asia", "North America"],
      "physicalFeatures": {
        "height": "10-60 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Linear",
        "stem": "Smooth"
      }
    },
    {
      "name": "Zinnia",
      "color": ["Red", "Pink", "Orange", "Yellow", "White"],
      "pollinators": ["Bees", "Butterflies"],
      "geographicRegions": ["North America", "South America"],
      "physicalFeatures": {
        "height": "30-90 cm",
        "flowerSize": "5-10 cm",
        "leafShape": "Lance-shaped",
        "stem": "Smooth"
      }
    }
  ]
}


def find_matching_flowers(flower_data, selected_colors, selected_pollinators, selected_geographic_regions):
    matches = []
    for flower in flower_data["flowers"]:
        match = True
        if not any(color in flower["color"] for color in selected_colors):
            match = False
        if not any(pollinator in flower["pollinators"] for pollinator in selected_pollinators):
            match = False
        if not any(region in flower["geographicRegions"] for region in selected_geographic_regions):
            match = False
        
        if match:
            matches.append(flower)

    return matches[:5]  #top 5 matches

class FlowerFinderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Flower Finder')
        self.setGeometry(200, 200, 800, 600)  #initial window size

        layout = QVBoxLayout()

        #custom window control buttons
        window_control_layout = QHBoxLayout()

        minimize_button = QPushButton('_')
        minimize_button.clicked.connect(self.minimize_window)
        maximize_button = QPushButton('□')
        maximize_button.clicked.connect(self.maximize_window)
        close_button = QPushButton('X')
        close_button.clicked.connect(self.close_window)

        #window buttons
        window_control_layout.addWidget(minimize_button)
        window_control_layout.addWidget(maximize_button)
        window_control_layout.addWidget(close_button)

        spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        window_control_layout.addSpacerItem(spacer)

        layout.addLayout(window_control_layout)

        self.color_checkboxes = [QCheckBox(color) for color in ["White", "Yellow", "Pink", "Red", "Blue"]]
        self.pollinator_checkboxes = [QCheckBox(pollinator) for pollinator in ["Bees", "Butterflies", "Hummingbirds"]]
        self.region_checkboxes = [QCheckBox(region) for region in ["Worldwide", "North America", "South America", "Europe", "Asia"]]

        form_layout = QFormLayout()
        
        for checkbox in self.color_checkboxes:
            form_layout.addRow(checkbox)
        form_layout.addRow(QLabel('Colors'))

        for checkbox in self.pollinator_checkboxes:
            form_layout.addRow(checkbox)
        form_layout.addRow(QLabel('Pollinators'))

        for checkbox in self.region_checkboxes:
            form_layout.addRow(checkbox)
        form_layout.addRow(QLabel('Geographic Regions'))

        self.button = QPushButton('Find Flowers')
        self.button.clicked.connect(self.on_click)

        self.result_label = QLabel('Matching flowers will appear here.')

        layout.addLayout(form_layout)
        layout.addWidget(self.button)
        layout.addWidget(self.result_label)

        self.image_layout = QVBoxLayout()
        layout.addLayout(self.image_layout)

        self.setLayout(layout)

    def on_click(self):
        selected_colors = [checkbox.text() for checkbox in self.color_checkboxes if checkbox.isChecked()]
        selected_pollinators = [checkbox.text() for checkbox in self.pollinator_checkboxes if checkbox.isChecked()]
        selected_geographic_regions = [checkbox.text() for checkbox in self.region_checkboxes if checkbox.isChecked()]

        matches = find_matching_flowers(flower_data, selected_colors, selected_pollinators, selected_geographic_regions)

        for i in reversed(range(self.image_layout.count())): 
            widget = self.image_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)

        if matches:
            for flower in matches:
                self.display_flower(flower)
        else:
            self.result_label.setText('No matching flowers found.')

    def display_flower(self, flower):
        #horz
        hbox = QHBoxLayout()

        #img
        image_label = QLabel(self)
        image_url = flower.get("image_url")
        if image_url:
            try:
                response = requests.get(image_url)
                image_data = BytesIO(response.content)
                pixmap = QPixmap()
                pixmap.loadFromData(image_data.read())
                image_label.setPixmap(pixmap.scaled(100, 100, Qt.KeepAspectRatio))
            except:
                image_label.setText('Image not available')

        name_label = QLabel(flower["name"], self)
        name_label.setAlignment(Qt.AlignCenter)

        hbox.addWidget(image_label)
        hbox.addWidget(name_label)

        self.image_layout.addLayout(hbox)

    def minimize_window(self):
        self.showMinimized()

    def maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def close_window(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlowerFinderApp()
    ex.show()
    sys.exit(app.exec_())
