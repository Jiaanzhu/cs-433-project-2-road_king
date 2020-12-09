import torch
import torchvision


def rotate_45(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(30, 60))
    crop = torchvision.transforms.CenterCrop(size=280)
    resize = torchvision.transforms.Resize(size=400, interpolation=3)
    transform = torchvision.transforms.Compose([rotate, crop, resize])
    return transform(ts)


def rotate_90(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(90, 90))
    return rotate(ts)


def rotate_135(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(120, 150))
    crop = torchvision.transforms.CenterCrop(size=280)
    resize = torchvision.transforms.Resize(size=400, interpolation=3)
    transform = torchvision.transforms.Compose([rotate, crop, resize])
    return transform(ts)


def rotate_180(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(180, 180))
    return rotate(ts)


def rotate_225(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(210, 240))
    crop = torchvision.transforms.CenterCrop(size=280)
    resize = torchvision.transforms.Resize(size=400, interpolation=3)
    transform = torchvision.transforms.Compose([rotate, crop, resize])
    return transform(ts)


def rotate_270(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(270, 270))
    return rotate(ts)


def rotate_315(ts):
    rotate = torchvision.transforms.RandomRotation(degrees=(300, 330))
    crop = torchvision.transforms.CenterCrop(size=280)
    resize = torchvision.transforms.Resize(size=400, interpolation=3)
    transform = torchvision.transforms.Compose([rotate, crop, resize])
    return transform(ts)


def random_rotate(ts, p=0.9):
    """
    Random apply rotations with 5 pre-defined degrees
    """
    rand = torch.rand(1).item()
    p = p / 9
    if rand <= 1.5 * p:
        ts = rotate_45(ts)
    elif 1.5 * p < rand < 2.5 * p:
        ts = rotate_90(ts)
    elif 2.5 * p < rand <= 4 * p:
        ts = rotate_135(ts)
    elif 4 * p < rand <= 5 * p:
        ts = rotate_180(ts)
    elif 5 * p < rand <= 6.5 * p:
        ts = rotate_225(ts)
    elif 6.5 * p < rand <= 7.5 * p:
        ts = rotate_270(ts)
    elif 7.5 * p < rand <= 9 * p:
        ts = rotate_315(ts)
    else:
        ts = ts
    return ts