from django import template
from ..models import QuestionImage

register = template.Library()

@register.filter('get_image_from_question')
def get_image_from_question(question_id):
    try:
        img = QuestionImage.objects.get(question=question_id).image.url
    except QuestionImage.DoesNotExist:
        img = '/img/default.jpeg'
    return img


