# Project Arch

Project Arch is a high-level ML-based real-time scouting system in progress. It uses advanced computer vision and machine learning techniques to analyze Twitch live streams for scouting purposes. The system identifies robots, game pieces, and predicts whether a game piece has been scored.

## Features
- Connects to Twitch live streams using the Twitch API.
- Processes video in real-time using YOLOv5 vision models.
- Tracks robots and game pieces on the field.
- Predicts scoring events using custom asset packages and matching algorithms.

## Folder Structure
- `src/`: Contains source code.
- `data/`: Stores data files.
- `models/`: Stores AI models.
- `docs/`: Contains project documentation.

## Technical Stack
- **Twitch API**: For live stream integration.
- **YOLOv5 Vision Model**: Trained with a custom asset package to locate robots and game pieces.
- **Python**: For backend processing and logic.
- **OpenCV**: For video processing and frame analysis.
https://www.ultralytics.com/
## Getting Started
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the project using `python src/main.py`.

## Requirements
- Python 3.8+
- OpenCV
- Twitch API integration
- YOLOv5

## License
This project is licensed under the MIT License.
