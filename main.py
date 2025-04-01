import gdown
from concurrent.futures import ThreadPoolExecutor
from deepface import DeepFace
import os
import shutil

def download_file_names(file_id: str):
    image_file_count = 0
    files = gdown.download_folder(url=file_id, skip_download=True,resume=True,quiet=True)
    with open("images.txt", "w") as image_files:
        for file_obj in files:
            if file_obj.path.lower().endswith(( '.jpg', '.jpeg')):
                image_file_count += 1
                image_files.write(f"{file_obj.id} -- {file_obj.path}\n")
    return image_file_count

def download_file_using_file_id(file_id: str):
    print(f"Downloading image with id : {file_id}")
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output="all_images/")

def map_and_download_images_from_images_txt():
    with ThreadPoolExecutor(max_workers=3) as executor:
        with open("images.txt", "r") as image_files:
            file = image_files.readline()        
            while file:
                file_id = file.split(" -- ")[0]
                executor.submit(download_file_using_file_id, file_id)
                file = image_files.readline()
            

if __name__ == "__main__":
    print("DriveCopier - Face Matching Tool")
    print("--------------------------------")
    print("Downloaded images will be saved to the mounted volume.")
    print("Matched images will be moved to the verified_images directory.")
    print("")
    
    # Make sure directories exist
    os.makedirs("all_images", exist_ok=True)
    os.makedirs("verified_images", exist_ok=True)
    
    drive_link = input("Enter the drive link to be scanned: ")
    no_of_images = download_file_names(drive_link)

    print(f"There are {no_of_images} images in the drive\n")

    confirm_to_proceed = input("Do you proceed to download all images (y or n): ")
    if confirm_to_proceed.lower() in ("y", "yes"):
        map_and_download_images_from_images_txt()
        print(f"All {no_of_images} images have been downloaded")
    else:
        exit()

    # List available reference images
    input_dir = "input"
    print("\nAvailable reference images:")
    ref_images = [f for f in os.listdir(input_dir) 
                 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
    
    if not ref_images:
        print("No reference images found in input directory.")
        exit(1)
        
    for i, img in enumerate(ref_images):
        print(f"{i+1}. {img}")
    
    selection = int(input("\nSelect reference image number: ")) - 1
    if 0 <= selection < len(ref_images):
        image_path_of_face_to_find = os.path.join(input_dir, ref_images[selection])
    else:
        print("Invalid selection")
        exit(1)
        
    print(f"Using reference image: {image_path_of_face_to_find}")
    
    embedding_of_face_to_find = DeepFace.represent(image_path_of_face_to_find, model_name="Facenet512")[0]['embedding']
    image_dir = "all_images"
    
    image_files = [f for f in os.listdir(image_dir) 
                 if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]

    matches = 0
    for img_to_verify in image_files:
        img2_path = os.path.join(image_dir, img_to_verify)
        try:
            result = DeepFace.verify(embedding_of_face_to_find, img2_path, model_name="Facenet512")["verified"]
            if result:
                matches += 1
                print(f"✅ Match found: {img_to_verify}")
                os.makedirs("verified_images", exist_ok=True)
                src_path = os.path.join("all_images", img_to_verify) 
                dest_path = os.path.join("verified_images", img_to_verify)
                shutil.copy(src=src_path, dst=dest_path)  # Using copy instead of move to keep originals
            else:
                print(f"❌ No match: {img_to_verify}")
        except Exception as e:
            print(f"Error processing {img_to_verify}: {str(e)}")
    
    print(f"\nFound {matches} matching images out of {len(image_files)} total images")
    print(f"Matched images saved to verified_images directory")

