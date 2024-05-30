from paddleocr import PaddleOCR
from PIL import Image, ImageEnhance
import numpy as np
import logging

# Set log level to warning
logging.getLogger('ppocr').setLevel(logging.WARNING)

class OCRProcessor:

    def __init__(self, use_gpu=True, lang="japan", det_limit_side_len=960):
        self.ocr = PaddleOCR(
            use_gpu=use_gpu,
            lang=lang,
            det_limit_side_len=det_limit_side_len,
        )

    def preprocess_image(self, img_array):
        im = Image.fromarray(img_array).convert('L')
        enhancer = ImageEnhance.Contrast(im)
        # Increase contrast
        im_con = enhancer.enhance(2.0)
        np_img = np.asarray(im_con)
        return np_img

    def run_ocr(self, img_array):
        np_img = self.preprocess_image(img_array)

        # Run PaddleOCR
        result = self.ocr.ocr(img=np_img, det=True, rec=True, cls=False)

        # OCR result
        detected_texts = []
        if result and isinstance(result, list) and len(result) > 0 and isinstance(result[0], list):
            for detection in result[0]:
                confidence_score = detection[1][1]
                # Set threshold
                if confidence_score > 0.85:
                    ocr_text = detection[1][0]
                    detected_texts.append(ocr_text)
        
        return detected_texts