# What is this?
Current Project Description:
We were unable to complete our original idea in the time frame allotted, so we pivoted to a different idea, which is a game that uses CV to detect a real-life rectangle, creates a virtual rectangle based on these properties, and has a vitual circle chase it. You lose if the circle is able to catch up to and collide with the rectangle, so you have to move your real-life rectangle quickly and with dexterity in order to not lose.

***In the near future, we hope to complete our original idea. We have described this idea below so that you can see where we are heading.***

Original Idea:
Our project is a game that combines CV and AR into the gameplay. The human player is able to add obstacles to the game environment by placing them in front of a separate game display screen, OpenCV detects the obstacles, and these obstacles are generated through pygame as a component that other features in the game can interact with. This idea is based off of [Puppet.io](https://devpost.com/software/puppet-io), a project we were impressed by at MakeHarvard 2020.
![Game Diagram](https://i.imgur.com/4PQ7gKF.jpg)



# Important Disclosure
This game captures video using your computer webcam. This video feed is near-live capture, and it is not saved locally or to the web. The video is only used to allow for the game to be played. By playing this game, you consent to having video taken, which may involve yourself or other people.



# Instructions
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

To get started, clone this respository onto your device.

## Prerequisites
To be able to run this game, you must have OpenCV installed. 
- For Ubuntu, use the command `$ pip install opencv-python` or click [here](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html) for instructions
- For any Linux distro, click [here](https://docs.opencv.org/master/d7/d9f/tutorial_linux_install.html)
- For Windows, click [here](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html) for instructions
- For MacOS, click [here](https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html)

You must also have pygame installed.
- Generally speaking, you can use the command `python3 -m pip install -U pygame --user` to install pygame and use the command `python3 -m pygame.examples.aliens` to test that the installation was successful.
- If the installation did not occur successfully, or if you would like more details, click [here](https://www.pygame.org/wiki/GettingStarted) 

If you have ROS installed on your computer, OpenCV may not run properly. To resolve this, try uncommenting out the two sys.path lines toward the top of the *FinalProject_Model.py* file. Click [here](https://stackoverflow.com/questions/43019951/after-install-ros-kinetic-cannot-import-opencv) for more details.

## How to Run Our Game
The necessary files are *FinalProject_Model.py*, *FinalProject_View.py*, *FinalProject_Controller.py*, and *OpenCV_Pygame. py*, all located within the */src* folder of our GitHub repository. To run our game, first download these files. 

Before calibrating or running the game, make sure that your webcam is not being used by any other application.

General Calibration:
- Run *OpenCV_Pygame. py*. Four windows should appear. 
- View the taskbar, mask, and frame windows simulataneously.
- Hold a rectangle up within the frame of the webcam.
- Adjust the trackbars so that, in the mask window, the rectangle appears white while everything else appears black. Try to get rid of any white pixels in the parts of the mask that should be black or any black pixels within the rectangle, even if they only flash on the screen temporarily, as these can reduce the accuracy of the rectangle detection algorithm. Ideally, in the frame window, the rectangle should constantly be outlined and display the word rectangle next to it. We recommend taking your time to get the calibration right because this can have a huge impact on how well the game works.

Projector Calibration:
If you would like to play this game as an AR game, please follow the additional calibration guidelines below.
**TODO:** add projector calibration guidelines

Once everything is calibrated, simply run *FinalProject_Model.py* using your preferred method (with an IDE, from the terminal, etc.) to play our game!

## Specifications of Systems We Tested On
It is possible that for some unforseen reasons, our game will not run successfully on your system even though it ran successfully on ours. Here are some details about the systems we used for testing:
- Machine: Dell Latitude 5401 with 30 fps webcam
- OS: Ubuntu 16.04.6 LTS and 18.04.4 LTS (dual-booted, not a virtual machine)
- Software: 
  - Python 3.7.4
  - Pygame 1.9.6
  - OpenCV 4.2.0



# The Game: Development and Results

## Implementation
**TODO**: Add details about the program architecture. Also add program snippets and descriptions of what they do (image filtration, contour capture).

Here is a flow diagram of our setup that gives an overview of the different steps that the program must take in order to run the game.
![Flow Diagram](https://i.imgur.com/MzxoOLf.jpg)

## See It in Action!
**TODO**: Embed Youtube video of the game being played.



# Our Story and Context

## Narrative
**TODO**: Add details about the full development process and the reasons behind decisions we made.

## Ethical Considerations
Even in something as seemingly simple as our game, there can be unintended, negative consequences that arise when the game is deployed in real-world scenarios. Therefore, as developers, we have a responsibility to think very intentionally about where things can go wrong, and we must do our best to protect against these potential issues. We must also have humility and be willing to accept that sometimes, even with our best efforts, things can still go wrong. When issues are exposed unexpectedly after deployment, we must have processes in place that allow for rapid mitigation.

There are some areas of concern that we were able to identify for this project. One concern has to do with video capture. Whenever videos are taken, especially when people are captured in the videos, privacy concerns become relevant. For our game to work, it must take video capture of the projection of the game, and a human player must place blocks on this projection. To mitigate any concerns regarding this, the video capture will strictly be live. No components of the video will be saved, either locally or on the web. We will also include a notice informing users that their video will be recorded but we will not save it or do anything with it other than use it for the gameplay. This notice is located toward the top of the website/readme under "Important Disclosure" and is also included in the header comment in the main *FinalProject_Model.py* file.

Another concern with computer games is the negative impact they can have on people's health. However, we think that our game is better than others in this respect, especially since it involves problem-solving, forces users to interact with their physical environments, and requires them to move around more than most other games do. When we eventually create the full game based on our original idea, we think one action we can take to mitigate the potential negative consequences is to limit the number of levels or force the game to end after a certain number of rounds, after which the user would need to close the game windows and restart the program in order to play again. 



# Additional Information

### Built With
OpenCV - Detect and process obstacles  
Pygame - Game engine

### Acknowledgments
**TODO**: Acknowledge anyone whose code was used, inspiration, etc.

We'd like to thank the [Puppet.io](https://devpost.com/software/puppet-io) team at MakeHarvard 2020 for providing us with inspiration for this project.

### Authors
Jackie Zeng  
Rohil Agarwal

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
