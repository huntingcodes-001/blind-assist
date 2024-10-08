This project involves complex hardware integration and requires intermediate-level programming skills in Python, along with familiarity with Linux, Raspberry Pi, and basic hardware concepts. Before starting, ensure you meet these prerequisites for a smooth experience.

For Software Assistance:
Contact Muhammad Sheikh: GitHub | Phone: +91 88508 78997

For Hardware Assistance:
Contact Amir Zakaria: GitHub | Phone: +91 98929 77581

Software Setup Instructions:
1. Install Dependencies:
Install all required packages listed in the requirements.txt file.

2. Create a Virtual Environment:
Set up a virtual environment to isolate your project dependencies.

3. Edit Configuration in main.py:
Modify lines 19-23 in main.py to reflect the correct paths to the virtual environment's Python interpreter and the app-related files.

4. Generate API Keys:
Obtain and configure API keys for the following services:
     AI Assistant: Generate a key from OpenAI.
     OCR & Object Detection: Enable and obtain keys for the Cloud Vision API on Google Cloud Platform.

5. Set Up Cron Jobs:
After completing the hardware setup, configure cron jobs as specified in cronjobs.txt to run the code on system boot.


Hardware Setup Instructions:

1. Gather Materials:
Purchase all the components listed in the HardwareRequirements document.

2. Prepare the SD Card:
Flash the SD card with the latest 64-bit version of Raspberry Pi OS.

3. Connect Push Buttons:
Follow the provided schematic to connect the push buttons correctly.

4. Test Button Connections:
Run the testButtons.py script to ensure all buttons are functioning and properly connected.

5. Final Testing:
After successful button testing, restart the system and verify button functionality using main.py.