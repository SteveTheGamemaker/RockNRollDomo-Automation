import cv2
import numpy as np
from mss import mss
import pydirectinput

# Define the region of the screen to capture for the game
monitor = {"left": 2535, "top": 1223, "width": 680, "height": 370}

# Define each lane's characteristics: pixel coordinates, expected color, and associated directional key
lanes = [
    {"pixel": (133, 285), "color": (243, 195, 0), "key": "left"},
    {"pixel": (344, 179), "color": (219, 97, 251), "key": "up"},
    {"pixel": (554, 286), "color": (130, 235, 40), "key": "right"}
]

# Set a threshold to identify color changes indicating incoming notes
color_change_threshold = 25
selected_lane = None  # Initialize the currently selected lane

# presstime: Delay after pressing 'A'. Crucial for game balance. Default value (0.032) is optimal for easy and hard tours. For faster BPM songs in the mixer, decrease this value. Beyond a certain BPM, songs are unwinnable regardless of this setting.
presstime = 0.032

def colors_are_similar(color1, color2):
    """Check if two colors are similar based on a set threshold."""
    return all(abs(color1[i] - color2[i]) < color_change_threshold for i in range(3))

def change_lane_and_hit(lane_index, img):
    """Change to the specified lane and simulate pressing the 'A' button."""
    global selected_lane
    lane_key = lanes[lane_index]["key"]
    
    # Switch lanes if the target lane is not currently selected.
    if selected_lane != lane_index:
        pydirectinput.PAUSE = 0  # Eliminate delay to allow instant note hitting post-lane switch
        pydirectinput.keyDown(lane_key)

    # Hit the note
    pydirectinput.PAUSE = presstime
    pydirectinput.press('a')
    print(f"Pressed 'a' for lane {lane_index}")

    # Release the lane key and update the currently selected lane
    if selected_lane != lane_index:
        pydirectinput.keyUp(lane_key)
        selected_lane = lane_index
        print(f"Switched to lane {selected_lane}")

with mss() as sct:
    while True:
        # Capture and process screen image
        img = np.array(sct.grab(monitor))
        img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Check each lane for note colors and respond accordingly
        for i, lane in enumerate(lanes):
            current_color = img_bgr[lane["pixel"][1], lane["pixel"][0]]
            if colors_are_similar(current_color, lane["color"]):
                change_lane_and_hit(i, img_bgr)

        # Display the captured image (for debugging purposes)
        cv2.imshow("Screen Capture", img_bgr)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
