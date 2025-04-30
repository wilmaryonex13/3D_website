import os
import shutil

source_dir = 'C:/Users/lukee/OneDrive/Desktop/Projects/3D_Website/frames/drone-to-laser'
target_dir = 'C:/Users/lukee/OneDrive/Desktop/Projects/3D_Website/frames/laser-to-drone'

# Make sure the target folder exists
os.makedirs(target_dir, exist_ok=True)

# Get all frame files sorted by name
frames = sorted([f for f in os.listdir(source_dir) if f.endswith('.webp')])

# Reverse the frame list
reversed_frames = frames[::-1]

# Rename and copy
total = len(reversed_frames)
for i, filename in enumerate(reversed_frames, start=1):
    new_name = f"frame{i:03d}.webp"
    src_path = os.path.join(source_dir, filename)
    dst_path = os.path.join(target_dir, new_name)
    shutil.copyfile(src_path, dst_path)

print(f"✅ Reversed {total} frames from '{source_dir}' to '{target_dir}'")
