# What is this?

Our project is a game that combines CV and AR into the gameplay. The human player would be able to add obstacles to the game environment by placing them in front of a separate game display screen, OpenCV would detect the obstacles, and these obstacles would be generated through pygame as a component that other features in the game could interact with. This idea is based off of [Puppet.io](https://devpost.com/software/puppet-io), a project we were impressed by at MakeHarvard 2020.

![Game Diagram](https://raw.githubusercontent.com/sd2020spring/DepthProject-jackie-rohil/master/SoftDes%20-%20Final%20Project%20Media/GameDiagramReview1.jpg?token=ANHOE3Y4FTU2QQ4E4GECACC6WONAU)



# Instructions
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

To get started, clone this respository onto your device.

## Prerequisites
To be able to run this game, you must have OpenCV installed. 
- For Ubuntu, use the command `$ pip install opencv-python` or click [here](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html) for instructions
- For Windows, click [here](https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html) for instructions

## How to Run Our Game
**TODO**: List descriptions of each file, what they do, and what order to run them in. 



# The Game: Development and Results

## Implementation
**TODO**: Add details about the program architecture. Also add program snippets and descriptions of what they do (image filtration, contour capture).

Here is a flow diagram of our setup that gives an overview of the different steps that the program must take in order to run the game.
![Flow Diagram](https://github.com/sd2020spring/DepthProject-jackie-rohil/blob/master/System%20Diagram.jpg)

## See It in Action!
**TODO**: Embed Youtube video of the game being played.



# Our Story and Context

## Narrative
**TODO**: Add details about the full development process and the reasons behind decisions we made.

## Ethical Considerations
**TODO**: There may be more considerations that we missed, so we should take some time to think about these and add to this section.
Even in something as seemingly simple as a ball drop game, there can be unintended, negative consequences that arise when the game is deployed in real-world scenarios. Therefore, as developers, we have a responsibility to think very intentionally about where things can go wrong, and we must do our best to protect against these potential issues. We must also have humility and be willing to accept that sometimes, even with our best efforts, things can still go wrong. When issues are exposed unexpectedly after deployment, we must have processes in place that allow for rapid mitigation.
There are some areas of concern that we were able to identify for this project. One concern has to do with video capture. Whenever videos are taken, especially when people are captured in the videos, privacy concerns become relevant. For our game to work, it must take video capture of the projection of the game, and a human player must place blocks on this projection. To mitigate any concerns regarding this, the video capture will strictly be live. No components of the video will be saved, either locally or on the web. We will also include a notice informing users that their video will be recorded but we will not save it or do anything with it other than use it for the gameplay. 
Another concern is that people can get addicted to games. We do not know what we can do to ensure that this does not happen. However, we do think that our game is better than others in this respect, especially since it involves problem-solving and forces users to interact with their physical environments. The best action we think we can take is to limit the number of levels. 



# Additional Information

### Built With
OpenCV - Detect and process obstacles  
Pygame - Game engine

### Acknowledgments
**TODO**: Acknowledge anyone whose code was used, inspiration, etc
We'd like to thank the [Puppet.io](https://devpost.com/software/puppet-io) team at MakeHarvard 2020 for providing us with inspiration for this project.

### Authors
Jackie Zeng  
Rohil Agarwal

### License
This project is licensed under the MIT License - see the LICENSE.md file for details
