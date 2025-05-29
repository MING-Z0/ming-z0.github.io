import os
from PIL import Image


def convert_images_to_jpg(input_dir, output_dir=None, quality=85):
    """
    转换图片为 JPG 格式并压缩
    """
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    supported_formats = ('.png', '.bmp', '.tiff', '.jpeg', '.webp', '.heic',
                         '.heif', '.gif', '.jpg', '.JPG')

    output_files = []

    for root, _, files in os.walk(input_dir):
        for filename in files:
            if not filename.lower().endswith(supported_formats):
                continue

            file_path = os.path.join(root, filename)
            try:
                with Image.open(file_path) as img:
                    img = img.convert('RGB')

                    # 临时文件名（保持原名，之后再统一重命名）
                    new_filename = os.path.splitext(filename)[0] + '.jpg'
                    output_path = os.path.join(output_dir or root,
                                               new_filename)

                    img.save(output_path,
                             'JPEG',
                             quality=quality,
                             optimize=True)
                    output_files.append(output_path)

                    print(f"✅ 转换完成: {file_path} -> {output_path}")

            except Exception as e:
                print(f"⚠️ 无法处理文件 {file_path}: {e}")

    return output_files


def rename_images_sequentially(directory):
    """
    对目录中的 JPG 文件进行按数字顺序重命名：1.jpg, 2.jpg, ...
    """
    files = [f for f in os.listdir(directory) if f.lower().endswith('.jpg')]
    files.sort(key=lambda f: os.path.getmtime(os.path.join(directory, f))
               )  # 或用 lambda f: f.lower() 进行名称排序

    for idx, filename in enumerate(files, start=1):
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"{idx}.jpg")

        # 避免重名覆盖（如 old_path 与 new_path 相同）
        if old_path != new_path:
            os.rename(old_path, new_path)
            print(f"🔁 重命名: {filename} -> {idx}.jpg")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="将目录下图片转换为JPG格式、压缩并重命名排序")
    parser.add_argument("input_dir", help="图片所在的输入目录")
    parser.add_argument("-o",
                        "--output_dir",
                        help="输出目录（默认覆盖原图）",
                        default=None)
    parser.add_argument("-q",
                        "--quality",
                        type=int,
                        default=70,
                        help="压缩质量（1-95），默认80")

    args = parser.parse_args()

    # 1. 转换
    convert_images_to_jpg(args.input_dir, args.output_dir, args.quality)

    # 2. 重命名
    target_dir = args.output_dir or args.input_dir
    rename_images_sequentially(target_dir)
