# AI Camera for Object Detection

This project is an AI-powered camera application that uses TensorFlow’s MobileNetV2 model to perform object detection in real time. The app allows users to take pictures of objects and receive publicly available data, such as product names and prices. 

This prototype was used as part of the BOCHK Business Competition 2024, where it won 2nd place and a HKD100,000 prize. A similar version was adapted for the HKGCC Business Competition, where it was used to identify building materials and achieved Top 5.

## Features
- **Real-time object detection:** Uses a webcam to capture real-time video and detect objects.
- **TensorFlow integration:** Utilizes the MobileNetV2 model to recognize objects from the ImageNet dataset.
- **User interaction:** Provides a simple user interface (UI) that allows users to take a picture and get predictions for the object.
- **Integration flexibility:** Can be integrated into an app to provide product data or identification of various objects, such as building materials.

## Code Overview

The core of this application is the `CameraDemoApp` class, which is based on Kivy for the user interface. The app uses OpenCV to capture video from the webcam and displays it in a window. When a user takes a picture, the app processes the image with a pre-trained MobileNetV2 model to make predictions on the object.

### Main Components:
- **Kivy UI**: The app’s UI is created using Kivy, and includes a camera display and a button for taking pictures.
- **OpenCV**: Used for capturing frames from the webcam and converting them into a format suitable for processing.
- **TensorFlow (MobileNetV2)**: The pre-trained MobileNetV2 model is used to classify the captured image and make predictions.
- **Prediction Display**: After taking a picture, the app decodes the predictions from the MobileNetV2 model and displays the result to the user.

### Key Functions:
- **build()**: Initializes the layout, camera feed, and "Take Picture" button.
- **update()**: Captures frames from the webcam and displays them in real-time.
- **take_picture()**: Captures a frame from the webcam, processes it, and predicts the object class using MobileNetV2.
- **preprocess_input()**: Prepares the image for model input by resizing and normalizing it.
- **show_payment_page()**: Displays the predicted product name and price after a picture is taken.
- **return_to_camera()**: Returns to the camera feed after showing the prediction.

## Achievements

This project was recognized in the following competitions:
- **BOCHK Business Competition 2024**: Won 2nd place and HKD100,000 prize.
- **HKGCC Business Competition**: Finalist in Top 5 for identifying building materials.

## Future Enhancements
- **Expanded object database**: Integrate with more product datasets to provide richer information.
- **Mobile app integration**: Build a mobile version of the app for broader consumer access.
- **Real-time improvements**: Optimize the model for faster predictions and enhanced real-time performance.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
