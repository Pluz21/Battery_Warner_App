# Low Battery Warner App

Low Battery Warner is a simple Python application that alerts users when their battery level falls below a specified threshold. It provides a graphical user interface (GUI) to display the current battery level and issues a warning when the battery level is low.

## Executable

You can find an executable version readily available right here : https://pluz21.itch.io/battery-checker

## Features

- Monitors the battery level of the system.
- Displays the current battery level in the GUI.
- Allows users to set a lower threshold for battery level.
- Issues a warning when the battery level falls below the specified threshold.
- Icon blinks when the battery level reaches the threshold.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Required Python packages: `tkinter`, `psutil`, `winsound` (for Windows).

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/your-username/low-battery-warner.git
```

2. Navigate to the project directory:

```
cd low-battery-warner
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

### Usage

1. Run the application by executing the Python script:

```
python LowBatteryWarnerApp.py
```

2. Set the lower threshold for the battery level in the GUI.
3. The application will monitor the battery level and issue a warning when it falls below the specified threshold. The icon will blink when the battery level reaches the threshold.

### Building Executable

- To build the Windows executable, run the following command:

```bash
pyinstaller --onefile --noconsole LowBatteryWarnerApp.py
```

### Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new pull request.


## Acknowledgements

- Special thanks to [psutil](https://github.com/giampaolo/psutil) and [tkinter](https://docs.python.org/3/library/tkinter.html) for their excellent libraries.
