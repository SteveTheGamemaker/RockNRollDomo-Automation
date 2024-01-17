
# RockNRollDomo-Automation

Automated player for 'Rock-n-Roll Domo,' a rhythm game from the Nintendo DSi's DSiware shop. This project leverages Python, OpenCV, PyDirectInput, and MSS for screen capture to simulate gameplay.

## Introduction

In 'Rock-n-Roll Domo,' the character Domo and his band are displayed on screen, surrounded by speakers emitting colored music notes. These notes travel towards the center of the screen, aligning with three circles. 
The player's objective is to tap these notes as they align with the circles. This automation project replicates player interactions using computer vision and keyboard input simulation, adapted for use with a DS emulator.

## Technical Challenges and Solutions

- **Emulator Limitation**: The DS emulator used didn't recognize click inputs simulated by any Python library. The solution involved using the directional keys for selecting a circle and the 'A' button for hitting the notes.
- **PyDirectInput Library**: A key challenge was managing the built-in pause function of PyDirectInput, the only library recognized by the emulator for key presses. Adjusting this pause was crucial to avoid being flagged for rapid inputs, which the game considers cheating.

## Emulator Setup and Configuration

To begin, ensure you have a DS emulator with DSi mode enabled. For this project, melonDS was used, but any emulator compatible with PyDirectInput key presses will work. Make sure you have the necessary firmware or NAND files for the DSi.

### Screen Capture Setup

You need to define the area on the screen where the in-game circles are located. This can be changed in the 'monitor' definition at the beginning of the code. 
You'll also need to set the pixel coordinates for the centers of each music note. This is where the program will detect color changes indicating incoming notes. You can set these in the 'pixel' attribute of the 'lanes' list, also at the beginning of the code. 
Please note that the pixel coordinates are relative to the top left of the box you have set up in the 'monitor' definition.

An easy way to get the coordinates and size is by using MS Paint. You can use the 'prt sc' button on your keyboard to save a screenshot of your display to the clipboard, which you can then paste into MS paint using CTRL+V. 
The bottom of the window will show you the X and Y coordinates of the position the mouse is currently hovering over. If you use the select tool to select a region, it will also show you the size of the selected region. You can use this to get the position and size of a box containing the three circles, as well as the position of the middle of the circles where the code will check for incoming notes.


## Project Workflow

1. **Screen Capture**: The program captures specific areas of the screen, focusing on the centers of each circle where notes appear.
2. **Note Detection**: Utilizing color detection, the program identifies when a note is present in a lane.
3. **Lane Switching and Note Hitting**: The program dynamically selects the appropriate lane using directional keys and hits the note using the 'A' button.

## Getting Started

### Prerequisites

- Python 3.x
- OpenCV
- PyDirectInput
- MSS (for screen capture)

### Installation

1. Clone the repository:

   git clone https://github.com/[YourUsername]/RockNRollDomo-Automation.git

2. Install the required packages:

   pip install opencv-python pydirectinput mss


### Usage

Start your emulator. Start the game. 

Run the script in the cloned directory:

python rock_n_roll_domo.py

Make sure to click back on the emulator window as it has to be in focus for the key presses to register.


## Contributing

Contributions are encouraged and appreciated. Follow the standard fork, branch, and pull request workflow.

## Contact

Steve - [jmgg_1998@hotmail.com](mailto:jmgg_1998@hotmail.com)

Project Link: [https://github.com/SteveTheGamer/RockNRollDomo-Automation](https://github.com/SteveTheGamer/RockNRollDomo-Automation)

## Acknowledgements

- [Nintendo DSi](https://www.nintendo.com/)
- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [PyDirectInput](https://github.com/learncodebygaming/pydirectinput)
- [MSS](https://python-mss.readthedocs.io/)
