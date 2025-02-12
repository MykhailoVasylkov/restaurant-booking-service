from django import template

register = template.Library()

@register.filter
def optimized_cloudinary_url(image_url):
    """Automatically adds F_auto, q_auto to URL images"""
    if image_url:
        return image_url.replace("/upload/", "/upload/w_1000,h_800,c_limit,f_auto,q_auto/")
    return image_url