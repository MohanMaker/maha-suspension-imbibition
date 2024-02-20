# maha-suspension-imbibition

## Notes
1. Prepare liquid or bead suspension according to specification
2. Wash tube in soap (to increase hydrophilicity) and wipe slide with RainX (to make water stay in a high droplet)
3. Record settings: sharp focus, high framerate (60 fps), good lighting (backlight), high shutter speed (1/4000)
4. Record video by putting a drop of liquid on the slide (~0.3 mL), touching the tube to the drop of liquid, and letting capillary action drive the liquid through the tube
5. Trim video in QuickTime Player to include only time where the liquid front is on the screen
6. Convert to .avi using `ffmpeg -i input.mov -an -vcodec rawvideo -y output.avi`
7. Rotate and crop in Fiji to include only liquid, tube, and walls
8. Specify .avi video filepath and run `position.py` code to generate CSV data
9. Specify .csv filepath and run `plot.py` to visualize the data