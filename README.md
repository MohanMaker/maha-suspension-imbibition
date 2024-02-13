# maha-suspension-imbibition

## Notes
1. Prepare tube by washing in soap (increases hydrophilicity)
2. Record settings: sharp focus, high framerate (60 fps), good lighting (backlight), high shutter speed (1/4000)
3. Record video by touching tube to a drop of liquid, letting capillary action drive the liquid through the tube
4. Trim video in QuickTime Player to include only time where the liquid front is on the screen
5. Convert to .avi using `ffmpeg -i input.mov -an -vcodec rawvideo -y output.avi`
6. Rotate and crop in Fiji to include only liquid, tube, and walls
7. Specify .avi video filepath and run `position.py` code to generate CSV data
8. Specify .csv filepath and run `plot.py` to visualize the data