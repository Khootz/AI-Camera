from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from kivy.clock import Clock
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions

class CameraDemoApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.img1 = Image()
        self.layout.add_widget(self.img1)
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0/30.0)
        take_picture_btn = Button(text="Take Picture", size_hint=(1, 0.1))
        take_picture_btn.bind(on_press=self.take_picture)
        self.layout.add_widget(take_picture_btn)
        self.model = MobileNetV2(weights='imagenet')
        return self.layout

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tostring()
            image_texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img1.texture = image_texture

    def take_picture(self, instance):
        ret, frame = self.capture.read()
        if ret:
            cv2.imwrite('captured_image.jpg', frame)
            img = self.preprocess_input(frame)
            predictions = self.model.predict(img)
            decoded_predictions = decode_predictions(predictions, top=1)[0]
            for _, class_name, confidence_score in decoded_predictions:
                self.show_payment_page(class_name, "$10.00")

    def preprocess_input(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))
        img = img.astype(np.float32)
        img = preprocess_input(img)
        img = np.expand_dims(img, axis=0)
        return img

    def show_payment_page(self, product_name, price):
        self.layout.clear_widgets()
        product_label = Button(text=f"Product: {product_name}\nPrice: {price}", size_hint=(1, 0.8))
        self.layout.add_widget(product_label)
        return_btn = Button(text="Return to Camera", size_hint=(1, 0.2))
        return_btn.bind(on_press=self.return_to_camera)
        self.layout.add_widget(return_btn)

    def return_to_camera(self, instance):
        self.layout.clear_widgets()
        self.layout.add_widget(self.img1)
        take_picture_btn = Button(text="Take Picture", size_hint=(1, 0.1))
        take_picture_btn.bind(on_press=self.take_picture)
        self.layout.add_widget(take_picture_btn)

if __name__ == '__main__':
    CameraDemoApp().run()