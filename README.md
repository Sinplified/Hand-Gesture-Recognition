# Hand-Gesture-Recognition
Sign language is one of the oldest and most natural forms of language for communication, but since most people do not know sign language and interpreters are very difficult to come by we have come up with a real-time method using neural networks for fingerspelling based on American sign language. The focus of this work is to create a vision-based system to identify sign language gestures from the video sequences. The reason for choosing a system based on vision relates to the fact that it provides a simpler and more intuitive way of communication between a human and a computer. We can deploy the trained model on popular cloud services and predict the output of the gesture made. In our method, the hand image is first passed through a filter, and after the filter has been applied the frame is passed through a classifier that predicts the class of the hand gestures. Methodology -

* Dataset Formation - OpenCV
* Classification - CNN
* Web App - FLask
* Sending webcam frames to server side - SocketIO
* Sending predicted class to client side - SocketIO
