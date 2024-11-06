from PIL import Image, ImageChops
import numpy as np
import os
import allure


def compare_images(actual_path, expected_path, diff_dir, threshold=11, max_diff_percentage=11):
    img1 = Image.open(actual_path).convert("RGB")
    img2 = Image.open(expected_path).convert("RGB")
    if img1.size != img2.size:
        raise ValueError("Images must be of the same size")
    img1_np = np.array(img1)
    img2_np = np.array(img2)
    diff = np.abs(img1_np - img2_np)
    if threshold > 0:
        diff = np.where(diff > threshold, 255, 0)
    diff_mask = np.zeros_like(img1_np)
    diff_mask[:, :, 0] = diff.max(axis=2)
    diff_mask_image = Image.fromarray(diff_mask)
    diff_highlighted = Image.blend(img1, diff_mask_image, alpha=0.5)
    if not os.path.exists(diff_dir):
        os.makedirs(diff_dir)
    diff_path = os.path.join(diff_dir, "difference.png")
    diff_highlighted.save(diff_path)
    diff_percentage = np.mean(diff) / 255 * 100

    with allure.step("Images difference check"):
        allure.attach.file(actual_path, name="Actual Image", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(expected_path, name="Expected Image", attachment_type=allure.attachment_type.PNG)
        allure.attach.file(diff_path, name="Difference Image", attachment_type=allure.attachment_type.PNG)

        assert diff_percentage <= max_diff_percentage, f"Difference percentage is {diff_percentage:.2f}%"

    return diff_path, diff_percentage
