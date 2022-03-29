from imgaug import augmenters as iaa

def gaussianBlur(guassian_intensity_from, guassian_intensity_to):
    # If guassian_intensity_from/to is an integer then make it a float
    if isinstance(guassian_intensity_from, int):
        guassian_intensity_from = float(guassian_intensity_from)
    if isinstance(guassian_intensity_to, int):
        guassian_intensity_to = float(guassian_intensity_to)

    # Checking for parameter errors
    if guassian_intensity_from is None or guassian_intensity_to is None:
        raise ValueError("guassian_intensity_from and guassian_intensity_to cannot be None.")
    if not isinstance(guassian_intensity_from, float) or not isinstance(guassian_intensity_to, float):
        raise ValueError("guassian_intensity_from and guassian_intensity_to must be a float.")
    if guassian_intensity_from < 0 or guassian_intensity_to < 0:
        raise ValueError("guassian_intensity_from and guassian_intensity_to must be greater than 0.")
    if guassian_intensity_from > 3.0 or guassian_intensity_to > 3.0:
        raise ValueError("guassian_intensity_from and guassian_intensity_to must be less than 3.0.")
    if guassian_intensity_from > guassian_intensity_to:
        raise ValueError("guassian_intensity_from must be less than guassian_intensity_to.")

    # Creating the guassian blur augmentation
    augmenting = iaa.GaussianBlur(sigma=(guassian_intensity_from, guassian_intensity_to))
    return augmenting


def rotation(rotation_from, rotation_to):
    # If rotation_from/to is an integer then make it a float
    if isinstance(rotation_from, int):
        rotation_from = float(rotation_from)
    if isinstance(rotation_to, int):
        rotation_to = float(rotation_to)

    # Checking for parameter errors
    if rotation_from is None or rotation_to is None:
        raise ValueError("rotation_from and rotation_to cannot be None.")
    if not isinstance(rotation_from, float) or not isinstance(rotation_to, float):
        raise ValueError("rotation_from and rotation_to must be a float.")
    if rotation_from < 0 or rotation_to < 0:
        raise ValueError("rotation_from and rotation_to must be greater than 0.")
    if rotation_from > 360 or rotation_to > 360:
        raise ValueError("rotation_from and rotation_to must be less than 360.")
    if rotation_from > rotation_to:
        raise ValueError("rotation_from must be less than rotation_to.")

    # Creating the rotation augmentation
    augmenting = iaa.Affine(rotate=(rotation_from, rotation_to))
    return augmenting


def guassianBlur_and_rotation(guassian_intensity_from, guassian_intensity_to, rotation_from, rotation_to):
    sequential = iaa.Sequential()
    sequential.add(gaussianBlur(guassian_intensity_from, guassian_intensity_to))
    sequential.add(rotation(rotation_from, rotation_to))
    return sequential


def pad(left, right, top, bottom):
    # If left/right/top/bottom is an float then make it an integer
    if isinstance(left, float):
        left = int(left)
    if isinstance(right, float):
        right = int(right)
    if isinstance(top, float):
        top = int(top)
    if isinstance(bottom, float):
        bottom = int(bottom)

    # Checking for parameter errors
    # If left/right/top/bottom is not and integer then raise an error
    if not isinstance(left, int) or not isinstance(right, int) or not isinstance(top, int) or not isinstance(bottom, int):
        raise ValueError("left, right, top, and bottom must be integers.")
    # If left/right/top/bottom is less than 0 then raise an error
    if left < 0 or right < 0 or top < 0 or bottom < 0:
        raise ValueError("left, right, top, and bottom must be greater than 0.")
    # If left/right/top/bottom is all 0 then raise an error
    if left == 0 and right == 0 and top == 0 and bottom == 0:
        raise ValueError("At least one of left, right, top, and bottom must be greater than 0.")


    left_default_minimum_pad = 5
    right_default_minimum_pad = 5
    top_default_minimum_pad = 5
    bottom_default_minimum_pad = 5
    # Changing default if parameters is lower than default.
    if left < left_default_minimum_pad:
        left_default_minimum_pad = 0
    if right < right_default_minimum_pad:
        right_default_minimum_pad = 0
    if top < top_default_minimum_pad:
        top_default_minimum_pad = 0
    if bottom < bottom_default_minimum_pad:
        bottom_default_minimum_pad = 0

    # Creating Pad parameters from function parameters.
    left = (left_default_minimum_pad, left)
    right = (right_default_minimum_pad, right)
    top = (top_default_minimum_pad, top)
    bottom = (bottom_default_minimum_pad, bottom)

    # Creating the padding augmentation
    augmenting = iaa.Pad(px=(top, right, bottom, left))

    return augmenting


def scale(zoom_out, zoom_in):
    # If zoom_out is int then make it a float
    if isinstance(zoom_out, int):
        zoom_out = float(zoom_out)
    # If zoom_in is int then make it a float
    if isinstance(zoom_in, int):
        zoom_in = float(zoom_in)

    # Checking for parameter errors
    # If zoom_out/in is not a float then raise an error
    if not isinstance(zoom_out, float) or not isinstance(zoom_in, float):
        raise ValueError("zoom_out and zoom_in must be floats.")
    # If zoom_out/in is less than 0 then raise an error
    if zoom_out < 0 or zoom_in < 0:
        raise ValueError("zoom_out and zoom_in must be greater than 0.")

    # Creating the scale augmentation
    augmenting = iaa.Affine(scale=(zoom_out, zoom_in))
    return augmenting
