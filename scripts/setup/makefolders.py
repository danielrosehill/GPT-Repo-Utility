import os

year = input("Enter the two-digit year (e.g., 24 for 2024): ")

parent_folder = "Module"

if not os.path.exists(parent_folder):
    print(f"Parent folder '{parent_folder}' does not exist.")
    exit()

for subfolder in os.listdir(parent_folder):
    subfolder_path = os.path.join(parent_folder, subfolder)
    
    if os.path.isdir(subfolder_path):
        for i in range(1, 13):
            month_folder = os.path.join(subfolder_path, f"{year}-{i:02}")
            os.makedirs(month_folder, exist_ok=True)
            print(f"Created folder: {month_folder}")

print("Subfolders created successfully.")
