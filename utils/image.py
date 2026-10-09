import pygame

def scale_to_fit(image: pygame.Surface, box: tuple[int, int]) -> pygame.Surface:
    w, h = image.get_size()
    ratio = min(box[0] / w, box[1] / h)
    new_size = (round(w * ratio), round(h * ratio))
    return pygame.transform.smoothscale(image, new_size)