## GPS Track Animation with GPS


This repo has all you need to animate GPS tracks using QGIS. Follow the simple steps below.


### Here's a concise guide: Steps to Animate GPS Tracks in QGIS

- Prepare GPS Data:
    - Ensure your GPS data includes time-stamped coordinates in a supported format (e.g., GPX, CSV).
    - Import the data into QGIS as a vector layer.

- Enable Temporal Control:
    - In QGIS, activate the Temporal Panel from View > Panels > Temporal.
    - Configure your layer's temporal properties by setting the date/time field under Layer Properties > Temporal.

- Symbolize the Tracks:
    - Customize the style of your tracks to enhance visualization. 
    - Use lines or point symbols with varying sizes or colors to represent movement intensity or speed.

- Animate the Tracks:
    - Open the Temporal Panel, set the time range, and adjust the step interval.
    - Use the play button to animate the tracks, observing movements along the timeline.
      
- Export the Animation:
    - Install the Time Manager plugin or use the Temporal Controller.
    - Export the animation as a video or series of images using Project > Export > Export as Animation.

 
![track](https://github.com/martinsbuchi2/GPS-tracking-with-QGIS/blob/main/bikeTrack.gif)
