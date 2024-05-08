# maha-suspension-imbibition

## Procedure
1. Prepare liquid or bead suspension according to specification. Choose tube size to use for experiment (usually 400um).
2. Wash tube with HCL washing procedure to remove debris and impurities. Wipe slide with RainX to make water stay in a high droplet.
3. Record settings: camera window captures entire tube (including start where liquid goes in), sharp focus on tube/liquid (zoom in to set), high framerate (800 fps), good lighting (backlight), low exposure (400us), high shutter speed.
4. Record video by putting a drop of liquid (~0.25 mL) on the slide using a pipette, touching the tube to the drop of liquid, and letting capillary action drive the liquid through the tube. Make sure the tube doesn't move when the liquid first enters.
5. Trim video to include only time where the liquid front is on the screen (zero frame should be where the liquid first enters the tube, important to set the zero time point).
6. Convert to .avi using `ffmpeg -i input.mov -an -vcodec rawvideo -y output.avi`.
7. Rotate (transform -> rotate) in Fiji to straighten the tube in the video.
8. Crop (rectangle, image -> crop) in Fiji to include only liquid in the tube and the walls. The crop should begin where the liquid enters the tube (important to set zero distance point), and end near the end of the tube (exact ending doesn't matter).
8. Specify .avi video filepath and run `position.py` code to generate CSV data.
9. Specify .csv filepath and run `plot.py` to visualize the data.

## Other Links
[Google Docs](https://docs.google.com/document/d/1G9nOMdb0bA5Rw09efVxBG6Fvj6A5k7cHJllYa6dr6L0/edit?usp=sharing)

[Dropbox](https://www.dropbox.com/home/suspension_flow)
