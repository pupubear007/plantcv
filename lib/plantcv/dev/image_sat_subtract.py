### Image subtraction (saturation)
def image_sat_subtract(img1, img2, device, debug):
  # This is a function used to subtract one image from another image (img1 - img2)
  # The numpy subtraction function '-' is used. This is a modulo operation rather than the cv2.subtract fxn which is a saturation operation
  # img1 = input image
  # img2 = input image used to subtract from img1
  # device = device number. Used to count steps in the pipeline
  # debug = True/False. If True; print output image
  # ddepth = -1 specifies that the dimensions of output image will be the same as the input image
  s_subed_img = cv2.subtract(img1, img2)
  device += 1
  if debug:
    print_image(s_subed_img, str(device) + '_s_subtracted' + '.png')
  return device, s_subed_img
