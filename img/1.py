import os
import requests

# 设置基本URL和本地存储路径
base_url = "http://0blog.test.upcdn.net/"
output_folder = "./"

# 确保本地存储路径存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 读取name.txt中的文件名
with open("name.txt", "r") as file:
    filenames = file.readlines()

# 遍历每个文件名，拼接URL并下载图片
for filename in filenames:
    filename = filename.strip()  # 去除行末尾的换行符
    if filename:  # 确保不处理空行
        url = base_url + filename
        output_path = os.path.join(output_folder, filename)
        
        # 下载图片
        response = requests.get(url)
        
        if response.status_code == 200:
            with open(output_path, "wb") as img_file:
                img_file.write(response.content)
            print(f"Downloaded {filename} to {output_path}")
        else:
            print(f"Failed to download {filename} from {url}")

print("All downloads completed.")
