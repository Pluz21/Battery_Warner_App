import tkinter as tk
import winsound
import psutil
import os

class LowBatteryWarnerApp:
    def __init__(self, master):
        self.master = master
        master.title("Low Battery Warner")

        self.label = tk.Label(master, text="Battery Checker Running")
        self.label.pack()

        self.lower_threshold_label = tk.Label(master, text="Enter Lower Threshold:")
        self.lower_threshold_label.pack()

        self.lower_threshold_entry = tk.Entry(master)
        self.lower_threshold_entry.pack()

        self.battery_label = tk.Label(master, text="")
        self.battery_label.pack()

        self.warning_label = tk.Label(master, text="")
        self.warning_label.pack()

        # Get the path to the directory containing the script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.images_dir = os.path.join(self.script_dir, "Images")

        # Load PNG images
        self.empty_battery_image = tk.PhotoImage(file=os.path.join(self.images_dir, "empty_battery_icon.png"))
        self.full_battery_image = tk.PhotoImage(file=os.path.join(self.images_dir, "full_battery_icon.png"))

        self.check_battery()  

    def check_battery(self):
        current_battery_percent = psutil.sensors_battery().percent

        lower_threshold_text = self.lower_threshold_entry.get()
        if lower_threshold_text.strip() == '' or not lower_threshold_text.strip().isdigit():
            self.warning_label.config(text="Please enter a valid integer for lower threshold.")
            self.master.after(6000, self.check_battery)  # Check battery every 6 seconds
            return
        
        lower_threshold = int(lower_threshold_text)

        if current_battery_percent <= lower_threshold:
            self.warning_label.config(text="Low battery warning! Please connect your charger.")
            self.blink_icon()  # Start blinking icon
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
        else:
            self.warning_label.config(text="Battery level is normal.")
            self.master.iconphoto(False, self.full_battery_image)  # Set icon to full battery

        self.battery_label.config(text=UpdateBatteryLevelMessage())  
        self.master.after(6000, self.check_battery)  # Check battery every 1 minute

    def blink_icon(self):
        self.master.iconphoto(False, self.empty_battery_image)  # Set icon to empty battery
        self.master.after(500, self.reset_icon)  # After 500 milliseconds, reset icon

    def reset_icon(self):
        self.master.iconphoto(False, self.full_battery_image)  # Set icon to full battery
        self.master.after(500, self.blink_icon)  # After 500 milliseconds, blink icon again

def UpdateBatteryLevelMessage() -> str:
    lowBatteryString = "Your battery is LOW"
    mediumBatteryString = "Your battery is MEDIUM"
    highBatteryString = "Your battery is HIGH"

    battery_percent = psutil.sensors_battery().percent

    if battery_percent >= 88:
        return highBatteryString + " ->  " + str(battery_percent) + "%"
    elif 30 <= battery_percent < 88:
        return mediumBatteryString + " ->  " + str(battery_percent) + "%"
    else:
        return lowBatteryString + " ->  " + str(battery_percent) + "%"

def main():
    root = tk.Tk()
    app = LowBatteryWarnerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
