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
    augmenting._name = "GaussianBlur"
    return augmenting



