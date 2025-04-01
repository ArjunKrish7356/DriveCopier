#!/bin/bash

# Check if input directory exists, if not create it
INPUT_DIR="$HOME/DriveCopier_input"
OUTPUT_DIR="$HOME/DriveCopier_output"
VERIFIED_DIR="$HOME/DriveCopier_verified"

mkdir -p "$INPUT_DIR"
mkdir -p "$OUTPUT_DIR"
mkdir -p "$VERIFIED_DIR"

echo "Place your reference image in: $INPUT_DIR"
echo "Downloaded images will be stored in: $OUTPUT_DIR"
echo "Matched images will be stored in: $VERIFIED_DIR"
echo ""
echo "Press Enter when ready..."
read

# Run the container with mounted volumes
docker run -it --rm \
  -v "$INPUT_DIR:/app/input" \
  -v "$OUTPUT_DIR:/app/all_images" \
  -v "$VERIFIED_DIR:/app/verified_images" \
  drivecopier:latest