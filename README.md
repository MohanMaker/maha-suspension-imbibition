# maha-suspension-imbibition

## Notes
1. Prepare liquid or bead suspension according to specification. Choose tube size to use for experiment.
2. Wash tube in soap (to increase hydrophilicity) and wipe slide with RainX (to make water stay in a high droplet).
3. Record settings: camera window captures entire tube (including start where liquid goes in), sharp focus on tube/liquid (zoom in to set), high framerate (60 fps), good lighting (backlight), high shutter speed (1/4000).
4. Record video by putting a drop of liquid on the slide (~0.25 mL) using a pipette, touching the tube to the drop of liquid, and letting capillary action drive the liquid through the tube.
5. Trim video in QuickTime Player to include only time where the liquid front is on the screen (first entering the tube to leaving the frame, important to set zero time point).
6. Convert to .avi using `ffmpeg -i input.mov -an -vcodec rawvideo -y output.avi`.
7. Rotate (transform -> rotate) in Fiji to make the tube straight in the video.
8. Crop (rectangle, image -> crop) in Fiji to include only liquid in the tube without the walls. The crop should begin where the liquid enters the tube (important to set zero distance point), and end near the end of the tube (exact ending doesn't matter).
8. Specify .avi video filepath and run `position.py` code to generate CSV data.
9. Specify .csv filepath and run `plot.py` to visualize the data.