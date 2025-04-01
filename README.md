# DriveCopier

DriveCopier is a Docker-based tool that helps you scan Google Drive folders for images containing specific faces. It combines Google Drive batch downloading with facial recognition to identify and sort images containing a specific person.

## Features

- Download images from any shared Google Drive folder
- Perform facial recognition using DeepFace's Facenet512 model
- Automatically identify images that match a reference face
- Save matching images to a separate directory
- All packaged in a convenient Docker container

## Prerequisites

- Docker installed on your system
- A Google Drive folder link containing images
- A reference image of the person you want to find

## Quick Start

### Option 1: Pull from Docker Hub

```bash
# Docker image will be available at: 
# [DOCKER_HUB_LINK_PLACEHOLDER]
```

### Option 2: Build Locally

1. Clone this repository
   ```bash
   git clone https://github.com/yourusername/DriveCopier.git
   cd DriveCopier
   ```

2. Build the Docker image
   ```bash
   docker build -t drivecopier:latest .
   ```

3. Run the container using the provided script
   ```bash
   chmod +x run_container.sh
   ./run_container.sh
   ```

## Usage

1. Place your reference image(s) in the `~/DriveCopier_input` directory
2. Run the container script
3. When prompted, enter the Google Drive folder URL you want to scan
4. The tool will analyze all available images and identify matches
5. All downloaded images will be saved to `~/DriveCopier_output`
6. Matched images will be copied to `~/DriveCopier_verified`

## How It Works

1. The tool connects to Google Drive using the provided folder link
2. It identifies all image files in the drive and downloads them
3. You select a reference image from your input directory
4. The tool performs facial recognition on all downloaded images
5. Images containing the same person as the reference are copied to the verified directory

## Important Notes

- This tool uses DeepFace for facial recognition, which provides high accuracy but may have some false positives/negatives
- Large Google Drive folders may take significant time to download
- All processing is done locally - no data is sent to external services

## Directory Structure

- `~/DriveCopier_input`: Place your reference images here
- `~/DriveCopier_output`: All downloaded images will be stored here
- `~/DriveCopier_verified`: Images matching your reference will be copied here

## Technical Details

DriveCopier uses:
- Python 3.10
- DeepFace library for facial recognition
- gdown library for Google Drive interactions
- Docker for containerization and easy deployment

## License

This is a personal project so fully opensourced and freely editable

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.