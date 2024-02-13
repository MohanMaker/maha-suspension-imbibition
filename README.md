# maha-suspension-imbibition

## Notes
1. Prepare tube by washing in soap (increases hydrophilicity) and record video by touching the tube to a drop of water
2. Record settings: high framerate, good lighting, high shutter speed
3. Trim video in QuickTime to include only portions where the liquid front is on the screen
4. Convert to .avi using `ffmpeg -i input.mov -an -vcodec rawvideo -y output.avi`
5. Rotate and crop in Fiji to include only liquid, tube, and walls
6. Specify .avi video filepath and run `position.py` code to generate CSV data
7. Specify .csv filepath and run `plot.py` to visualize the data